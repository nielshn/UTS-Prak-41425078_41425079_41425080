"""# Improved admission analysis script
# - Keeps original copy of data for BEFORE analyses
# - Shows categorical columns that will be encoded and lists created dummy columns
# - Produces before/after visualizations (hist, box, KDE, QQ)
# - Produces correlation heatmaps before and after preprocessing
# - Keeps admission_grade_raw for statistical tests and interpretation

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy import stats
import statsmodels.api as sm

sns.set(style='whitegrid')

# CONFIG
DATA_PATH = 'data.csv'
OUT_DIR = 'analysis_outputs'
os.makedirs(OUT_DIR, exist_ok=True)

# helper: normalize column names to snake_case
def to_snake(s):
    return (str(s).strip().lower()
            .replace(' ', '_').replace('(', '').replace(')', '')
            .replace('/', '_').replace('-', '_').replace('__','_'))

# Load data and keep original copy
print('Loading dataset...')
df = pd.read_csv(DATA_PATH, sep=';', encoding='utf-8-sig')
df.columns = [to_snake(c) for c in df.columns]
print('Data shape:', df.shape)

# keep original for BEFORE analyses
df_orig = df.copy()
# ensure numeric admission grade column
if 'admission_grade' in df_orig.columns:
    df_orig['admission_grade_raw'] = pd.to_numeric(df_orig['admission_grade'], errors='coerce')
else:
    raise KeyError("Kolom 'admission_grade' tidak ditemukan dalam data.csv")

# Basic info
print('\nColumns sample:', df_orig.columns.tolist()[:30])
print('\nTarget distribution:')
if 'target' in df_orig.columns:
    print(df_orig['target'].value_counts(dropna=False))
else:
    raise KeyError("Kolom 'target' tidak ditemukan dalam data.csv")

# ----- EDA BEFORE PREPROCESSING -----
print('\nRunning BEFORE preprocessing EDA for admission_grade_raw...')
col = 'admission_grade_raw'
# descriptive per target
print('\nDescriptive stats by target:')
print(df_orig.groupby('target')[col].describe())

# save a few plots (hist + box + KDE + QQs)
plt.figure(figsize=(14,4))
plt.subplot(1,3,1)
sns.histplot(df_orig[col].dropna(), kde=True)
plt.title('Admission grade (raw) - overall')

plt.subplot(1,3,2)
sns.boxplot(x='target', y=col, data=df_orig)
plt.title('Boxplot admission_grade_raw per target')

plt.subplot(1,3,3)
for t in df_orig['target'].unique():
    sns.kdeplot(df_orig.loc[df_orig['target']==t, col].dropna(), label=t)
plt.title('KDE per target')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'before_admission_overview.png'), dpi=150)
plt.close()

# QQ plots
unique_targets = df_orig['target'].unique()
plt.figure(figsize=(12, 4 * int(np.ceil(len(unique_targets)/3))))
for i,t in enumerate(unique_targets):
    plt.subplot(int(np.ceil(len(unique_targets)/3)), 3, i+1)
    sm.qqplot(df_orig.loc[df_orig['target']==t, col].dropna(), line='s', ax=plt.gca())
    plt.title(f'QQ: {t}')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'before_admission_qq.png'), dpi=150)
plt.close()

# ----- PREPROCESSING -----
print('\nPreprocessing: detect categorical features and encode (keeping original copy)')
df_proc = df_orig.copy()

# Numeric columns
numeric_cols = df_proc.select_dtypes(include=[np.number]).columns.tolist()
# Candidate categorical: object dtype OR small-unique integers
cat_cols = df_proc.select_dtypes(include=['object']).columns.tolist()
int_cands = [c for c in df_proc.select_dtypes(include=[np.integer]).columns if df_proc[c].nunique() <= 10]
int_cands = [c for c in int_cands if c != 'target']
cat_cols = sorted(list(set(cat_cols + int_cands)))
print('Categorical candidate columns to encode:', cat_cols)

# We'll keep raw admission grade and also create scaled version (admission_grade_scaled)
adm_raw = 'admission_grade_raw'
# fill small NA if any for scaling
df_proc[adm_raw] = df_proc[adm_raw].fillna(df_proc[adm_raw].median())

# Scale numeric columns (but do not replace raw columns). We'll create <col>_scaled.
scale_exclude = ['target', adm_raw]
num_to_scale = [c for c in numeric_cols if c not in scale_exclude]
print('Numeric columns to scale count:', len(num_to_scale))
if len(num_to_scale) > 0:
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df_proc[num_to_scale].fillna(0))
    for i,c in enumerate(num_to_scale):
        df_proc[c + '_scaled'] = scaled[:,i]
# scale admission separately and keep both
df_proc['admission_grade_scaled'] = StandardScaler().fit_transform(df_proc[[adm_raw]])

# Encoding: one-hot for categorical candidates (exclude target)
encode_cols = [c for c in cat_cols if c != 'target']
print('Encode cols:', encode_cols)
if encode_cols:
    df_proc_enc = pd.get_dummies(df_proc, columns=encode_cols, drop_first=True)
else:
    df_proc_enc = df_proc.copy()

# Report encoded features
encoded_report = {}
for c in encode_cols:
    dummies = [col for col in df_proc_enc.columns if col.startswith(c + "_")]
    encoded_report[c] = len(dummies)

print('\nEncoded columns report:')
for k,v in encoded_report.items():
    print(f" - {k}: {v} dummy columns created")

# Save a small CSV of processed head for inspection
df_proc_enc.head(5).to_csv(os.path.join(OUT_DIR, 'processed_head_sample.csv'), index=False)

# ----- CORRELATION MATRICES: BEFORE vs AFTER -----
print('\nGenerating correlation heatmaps (before vs after)')
num_before = df_orig.select_dtypes(include=[np.number]).copy()
corr_before = num_before.corr()
num_after = df_proc_enc.select_dtypes(include=[np.number]).copy()
corr_after = num_after.corr()

plt.figure(figsize=(16,6))
plt.subplot(1,2,1)
mask = np.triu(np.ones_like(corr_before, dtype=bool))
sns.heatmap(corr_before, mask=mask, cmap='vlag', center=0, cbar_kws={'shrink':0.6})
plt.title('Correlation - BEFORE preprocessing')

plt.subplot(1,2,2)
mask2 = np.triu(np.ones_like(corr_after, dtype=bool))
# limit annotation size by plotting only a subset if matrix huge; but we still save full heatmap
sns.heatmap(corr_after, mask=mask2, cmap='vlag', center=0, cbar_kws={'shrink':0.6})
plt.title('Correlation - AFTER preprocessing')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'corr_before_after.png'), dpi=150)
plt.close()

# ----- VISUAL COMPARISON: admission raw vs scaled -----
print('\nGenerating before/after comparison plots for admission grade')
plt.figure(figsize=(14,10))
plt.subplot(2,2,1)
sns.histplot(df_orig[adm_raw].dropna(), kde=True, color='C0')
plt.title('Admission (raw) - overall')

plt.subplot(2,2,2)
sns.histplot(df_proc_enc['admission_grade_scaled'].dropna(), kde=True, color='C1')
plt.title('Admission (scaled) - overall')

plt.subplot(2,2,3)
sns.boxplot(x='target', y=adm_raw, data=df_orig)
plt.title('Boxplot admission_grade_raw per target')

plt.subplot(2,2,4)
sns.boxplot(x='target', y='admission_grade_scaled', data=df_proc_enc)
plt.title('Boxplot admission_grade_scaled per target')
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'before_after_admission.png'), dpi=150)
plt.close()

# KDE per target (raw vs scaled)
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
for t in df_orig['target'].unique():
    sns.kdeplot(df_orig.loc[df_orig['target']==t, adm_raw].dropna(), label=t)
plt.title('KDE admission_grade_raw per target')
plt.legend()

plt.subplot(1,2,2)
for t in df_proc_enc['target'].unique():
    sns.kdeplot(df_proc_enc.loc[df_proc_enc['target']==t, 'admission_grade_scaled'].dropna(), label=t)
plt.title('KDE admission_grade_scaled per target')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, 'kde_before_after_admission.png'), dpi=150)
plt.close()

# ----- STATISTICAL TESTS (use raw values for interpretability) -----
print('\nRunning statistical tests on admission_grade_raw by target')
from scipy.stats import levene, f_oneway, kruskal, mannwhitneyu
groups = [df_orig[df_orig['target']==g][adm_raw].dropna() for g in df_orig['target'].unique()]
levene_stat, levene_p = levene(*groups)
print('Levene p:', levene_p)
try:
    f_stat, f_p = f_oneway(*groups)
    print('ANOVA p:', f_p)
except Exception as e:
    print('ANOVA failed:', e)
kw_stat, kw_p = kruskal(*groups)
print('Kruskal-Wallis p:', kw_p)
# Mann-Whitney between Graduate and Dropout if both present
if set(['Graduate','Dropout']).issubset(set(df_orig['target'].unique())):
    g1 = df_orig[df_orig['target']=='Graduate'][adm_raw].dropna()
    g2 = df_orig[df_orig['target']=='Dropout'][adm_raw].dropna()
    u_stat, u_p = mannwhitneyu(g1, g2)
    print('Mann-Whitney Graduate vs Dropout p:', u_p)

# Spearman correlation example (admission vs first-sem curricular grade if present)
curr_cols = [c for c in df_orig.columns if 'curricular_units_1st_sem_grade' in c]
if curr_cols:
    rho, p_spear = stats.spearmanr(df_orig[adm_raw].fillna(0), df_orig[curr_cols[0]].fillna(0))
    print(f'Spearman correlation admission vs {curr_cols[0]}: rho={rho:.3f}, p={p_spear:.3g}')

# ----- SAVE processed dataset sample and encoded features list -----
report_path = os.path.join(OUT_DIR, 'encoding_report.txt')
with open(report_path, 'w', encoding='utf-8') as fh:
    fh.write('Categorical columns encoded:\n')
    for c in encode_cols:
        fh.write(f" - {c}: {encoded_report.get(c,0)} dummies\n")
    fh.write('\nSample of dummy columns (first 100):\n')
    dcols = [col for col in df_proc_enc.columns if any(col.startswith(c + '_' for c in encode_cols)]
    fh.write('\n'.join(dcols[:100]))

# Save processed full (if size okay) - optional
try:
    df_proc_enc.to_csv(os.path.join(OUT_DIR, 'processed_full_sample.csv'), index=False)
except Exception:
    pass

print('\nAll outputs saved to', OUT_DIR)
print('Files:', os.listdir(OUT_DIR)[:50])

print('\nDone.')"""