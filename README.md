# 🎓 UTS Data Science: Analisis Data Student Academic Status (Final ANOVA Version)

## 🧠 Business Understanding

Lembaga pendidikan tinggi sering menghadapi masalah **dropout mahasiswa** dan **kelulusan tidak tepat waktu**, yang berdampak pada reputasi dan efisiensi operasional institusi. Analisis data akademik dan sosial ekonomi mahasiswa dapat membantu mendeteksi pola risiko dini dan menjadi dasar kebijakan akademik adaptif.

**Tujuan:**

1. Mengidentifikasi faktor-faktor yang berhubungan dengan status akademik mahasiswa.
2. Memberikan insight berbasis data untuk pengambilan keputusan akademik.

---

## ⚙️ Data Collection

**Sumber Data:**
Dataset: _Predict Students Dropout and Academic Success_ — UCI Machine Learning Repository
💎 [https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

**Deskripsi Singkat:**

- Jumlah baris: 4424 mahasiswa
- Jumlah fitur: 37 (demografis, sosial ekonomi, akademik)
- Target: `Target` (Dropout / Enrolled / Graduate)

**Insight:**
Dataset memenuhi kriteria UTS (≥20 fitur dan ≥2000 baris) dan siap untuk analisis statistik dan visualisasi.

---

## 📊 Data Visualization

### a. Bar Chart — Distribusi Status Mahasiswa

**Alasan:** Menampilkan proporsi jumlah mahasiswa berdasarkan kategori _Dropout_, _Enrolled_, dan _Graduate_.
**Insight:** Mayoritas mahasiswa berada pada kategori **Graduate**.
**Interpretasi:** Distribusi tidak seimbang (_class imbalance_) menunjukkan dominasi kelompok Graduate yang dapat memengaruhi hasil analisis komparatif.

### b. Boxplot — Admission Grade per Target

**Alasan:** Membandingkan distribusi nilai masuk antar kategori _Target_.
**Insight:** Median _admission grade_ tertinggi dimiliki oleh kelompok **Graduate**.
**Interpretasi:** Nilai masuk berperan penting terhadap keberhasilan studi.

### c. Heatmap Korelasi

**Alasan:** Mengidentifikasi hubungan antar fitur numerik.
**Insight:** Korelasi tinggi antara `Curricular units 1st sem (approved)` dan `Curricular units 1st sem (grade)` menunjukkan konsistensi performa akademik.
**Interpretasi:** Fitur dengan korelasi kuat dapat direduksi melalui PCA.

### d. PCA 2D Visualization

**Alasan:** Menampilkan cluster berdasarkan dua komponen utama PCA.
**Insight:** Kelompok **Graduate** tampak terpisah dari **Dropout**.
**Interpretasi:** Variabel akademik memiliki kemampuan diskriminatif terhadap status akhir mahasiswa.

---

## 🧹 Data Processing and Techniques (Advance Preprocessing)

### a. Handling Missing Values

**Teknik:** `KNNImputer` untuk numerik dan _mode imputation_ untuk kategorikal.
**Insight:** Menjaga integritas dataset dan mengurangi bias akibat data kosong.

### b. Handling Outliers

**Teknik:** _IQR trimming_ dan _Winsorization_ (5th–95th percentile).
**Insight:** Mengurangi pengaruh nilai ekstrem tanpa menghapus data signifikan.

### c. Feature Scaling

**Teknik:** `StandardScaler`.
**Insight:** Menyamakan skala fitur numerik untuk menjaga keseimbangan kontribusi variabel.

### d. Encoding Categorical Variables

**Teknik:** _One-Hot Encoding_.
**Insight:** Mengubah kategori menjadi numerik agar dapat digunakan dalam analisis statistik.

### e. Feature Reduction

**Teknik:** PCA (10 komponen utama).
**Insight:** Dua komponen utama pertama menjelaskan sebagian besar variansi data (~90%).

---

## 📈 Statistical Analysis (Final Hypothesis Testing)

### 🧩 Hipotesis Penelitian

**Hipotesis Uji Parametrik (ANOVA):**

- H₀: Tidak ada perbedaan rata-rata _admission_grade_ antara mahasiswa **Dropout**, **Enrolled**, dan **Graduate**.
- H₁: Ada perbedaan signifikan rata-rata _admission_grade_ antar kelompok tersebut.

**Hipotesis Uji Non-Parametrik (Mann–Whitney U):**

- H₀: Distribusi _admission_grade_ mahasiswa **Dropout** dan **Graduate** sama.
- H₁: Distribusi _admission_grade_ berbeda signifikan antara kedua kelompok.

---

### a. Levene Test — Homogenitas Varians

**Hasil:** p = 0.00015
**Interpretasi:** Varians antar kelompok **tidak homogen**, sehingga ANOVA perlu dikonfirmasi dengan uji non-parametrik tambahan.

### b. One-Way ANOVA

**Hasil:** F(2, 4421) = 45.6, p = 1.14e-17
**Keputusan:** Karena p < 0.05, **tolak H₀** → terdapat perbedaan signifikan rata-rata _admission_grade_ antar kelompok.
**Effect Size (η²):** 0.06 → efek moderat.

### c. Kruskal–Wallis Test

**Hasil:** p = 1.20e-16
**Interpretasi:** Hasil signifikan, memperkuat hasil ANOVA meskipun asumsi homogenitas tidak terpenuhi.

### d. Mann–Whitney U Test

**Hasil:** p = 1.95e-15
**Keputusan:** Karena p < 0.05, **tolak H₀** → mahasiswa **Graduate** memiliki nilai masuk yang signifikan lebih tinggi daripada **Dropout**.

### e. Spearman Correlation

**Hasil:** ρ = 0.209, p ≈ 3.82e-44
**Interpretasi:** Korelasi positif lemah namun signifikan antara _admission_grade_ dan performa akademik semester pertama.
Mahasiswa dengan nilai masuk tinggi cenderung mempertahankan performa akademik yang baik.

---

## ✅ Kesimpulan Akhir

1. **H₀ ditolak pada uji ANOVA dan Mann–Whitney**, menunjukkan adanya perbedaan signifikan nilai masuk antar kategori mahasiswa.
2. **Nilai masuk (admission_grade)** berpengaruh nyata terhadap status akhir mahasiswa — terutama antara _Dropout_ dan _Graduate_.
3. **Hasil uji non-parametrik (Kruskal–Wallis, Mann–Whitney)** mengonfirmasi bahwa hasil ANOVA tetap valid meskipun varians tidak homogen.
4. **Korelasi Spearman** menunjukkan hubungan positif antara nilai masuk dan performa semester pertama.
5. Secara keseluruhan, mahasiswa dengan nilai masuk tinggi memiliki peluang kelulusan lebih besar dan risiko _dropout_ lebih rendah.

---

## 👥 Author

**Daniel Siahaan, Jessica Pasaribu, Novrael Marbun – UTS Data Science 2025**
**Kelompok:** 41425078*41425079_41425080
**Judul:** \_Student Academic Status Analysis — Predicting Dropout, Enrolled, and Graduate*
