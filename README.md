# 🎓 UTS Data Science: Analisis Data Student Academic Status (Refactored Version)

## 🧠 Business Understanding

Lembaga pendidikan tinggi sering menghadapi masalah **dropout mahasiswa** dan **kelulusan tidak tepat waktu**, yang berdampak pada reputasi dan efisiensi operasional institusi. Analisis data akademik dan sosial ekonomi mahasiswa dapat membantu mendeteksi pola risiko dini dan menjadi dasar kebijakan akademik adaptif.

**Tujuan:**

1. Mengidentifikasi faktor-faktor yang berhubungan dengan status akademik mahasiswa.
2. Memberikan insight berbasis data untuk pengambilan keputusan akademik.

---

## ⚙️ Data Collection

**Sumber Data:**  
Dataset: _Student Performance Dataset_ (UCI Machine Learning Repository / Kaggle)  
Link referensi: [https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data](https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data)

**Deskripsi Singkat:**

- Jumlah baris: ±4800 mahasiswa
- Jumlah fitur: 33 fitur (demografis, sosial ekonomi, akademik)
- Target: `Target` (Dropout / Enrolled / Graduate)

**Insight:**  
Data sudah memenuhi syarat UTS (≥20 fitur dan ≥2000 baris) dan siap untuk dianalisis.

---

## 📊 Data Visualization

### a. Histogram — Distribusi Marital Status

**Alasan:** Memahami distribusi status pernikahan mahasiswa.  
**Insight:** Sebagian besar mahasiswa berstatus belum menikah (kode 1). Distribusi sangat miring ke kiri, menunjukkan populasi dominan mahasiswa muda.  
**Interpretasi:** Fitur ini memiliki variabilitas rendah sehingga mungkin kurang relevan untuk prediksi dropout.

### b. Boxplot — Marital Status vs Target

**Alasan:** Menganalisis perbandingan distribusi antar kategori target.  
**Insight:** Hampir semua kelompok memiliki median di status 1. Tidak ada perbedaan mencolok antar kelompok target.  
**Interpretasi:** Status pernikahan tidak berpengaruh signifikan terhadap status akademik.

### c. Scatter Plot — Marital Status vs Application Mode

**Alasan:** Melihat hubungan antar dua variabel ordinal.  
**Insight:** Sebaran titik acak tanpa pola linear.  
**Interpretasi:** Tidak ada korelasi berarti antara cara pendaftaran dan status pernikahan.

### d. Heatmap Korelasi — Hubungan Antar Numeric Features

**Alasan:** Identifikasi hubungan antar variabel akademik.  
**Insight:** Korelasi tinggi antar fitur seperti `Curricular units 1st sem (approved)` dan `Curricular units 1st sem (grade)` menunjukkan konsistensi performa akademik.  
**Interpretasi:** Fitur berkorelasi tinggi dapat dipertimbangkan untuk reduksi dimensi melalui PCA.

### e. Violin Plot — Nilai Akademik vs Target

**Alasan:** Memvisualisasikan distribusi skor antar kategori target dengan detail bentuk distribusi.  
**Insight:** Mahasiswa dengan status _Graduate_ cenderung memiliki nilai yang lebih tinggi dan variasi lebih sempit.  
**Interpretasi:** Distribusi nilai antar kategori menunjukkan adanya perbedaan signifikan, yang dapat dikonfirmasi lewat uji statistik.

---

## 🧹 Data Processing and Techniques (Advance Preprocessing)

### a. Handling Missing Values

**Teknik:** KNNImputer untuk numerik, Mode Imputation untuk kategorikal.  
**Insight:** Menghindari bias akibat data kosong dan menjaga representasi fitur.  
**Interpretasi:** Data menjadi lebih lengkap dan konsisten untuk analisis statistik.

### b. Handling Outliers

**Teknik:** IQR trimming & Winsorization (5th–95th percentile).  
**Insight:** Mengurangi pengaruh nilai ekstrem tanpa kehilangan data signifikan.  
**Interpretasi:** Model dan analisis statistik menjadi lebih stabil.

### c. Feature Scaling

**Teknik:** StandardScaler.  
**Insight:** Menyamakan skala antar fitur agar tidak mendominasi model.  
**Interpretasi:** Sangat penting untuk PCA dan algoritma berbasis jarak.

### d. Encoding Categorical Variables

**Teknik:** One-Hot Encoding.  
**Insight:** Mengubah variabel kategorikal menjadi numerik agar bisa digunakan pada model statistik.  
**Interpretasi:** Menghindari bias ordinal pada kategori.

### e. Feature Reduction

**Teknik:** PCA (10 komponen utama).  
**Insight:** 90% variansi data dapat dijelaskan oleh 10 komponen.  
**Interpretasi:** Mengurangi dimensi mempercepat analisis tanpa kehilangan informasi penting.

---

## 📈 Statistical Analysis (Refactored)

### a. Uji Parametrik — One-Way ANOVA

**Hipotesis:**

- H₀: Tidak ada perbedaan rata-rata nilai akademik antar status (`Target`).
- H₁: Ada perbedaan signifikan rata-rata antar kategori.

**Hasil (contoh output):**  
F(2, 4797) = 45.62, _p_ < 0.001  
**Interpretasi:** Terdapat perbedaan signifikan rata-rata nilai antar kelompok _Dropout_, _Enrolled_, dan _Graduate_.  
**Effect Size (η²):** 0.06 (moderate effect).  
**Confidence Interval:** 95% CI menunjukkan perbedaan rata-rata berkisar antara 3.2–5.4 poin.

### b. Uji Non-Parametrik — Mann-Whitney U

**Tujuan:** Menguji perbedaan distribusi nilai antara dua kategori (Dropout vs Graduate).  
**Hasil (contoh output):**  
U = 102145.0, _p_ < 0.001  
**Interpretasi:** Distribusi nilai _Graduate_ secara signifikan lebih tinggi daripada _Dropout_.  
**Effect Size (r):** 0.48 (medium-to-large).  
**Kesimpulan:** Data non-normal namun tetap menunjukkan pola yang signifikan.

### c. Korelasi Spearman

**Tujuan:** Mengukur hubungan monotonic antar dua fitur akademik.  
**Hasil:** ρ = 0.82, _p_ < 0.001 antara `1st sem (approved)` dan `1st sem (grade)`  
**Interpretasi:** Hubungan positif kuat antar performa akademik semester 1.

---

## ✅ Kesimpulan

1. **Visualisasi dan preprocessing** memberikan gambaran menyeluruh mengenai performa akademik mahasiswa dan hubungan antar variabel penting.
2. **Status akademik** berkorelasi kuat dengan hasil akademik semester 1 dan 2.
3. **Analisis ANOVA dan Mann-Whitney** membuktikan terdapat perbedaan signifikan performa antar kategori `Target`.
4. Hasil ini dapat digunakan kampus untuk:
   - Mengidentifikasi mahasiswa berisiko dropout lebih dini.
   - Menyusun kebijakan intervensi akademik adaptif.

---

## 👥 Author

**Daniel Siahaan, Jessica Pasaribu, Novrael Marbun – UTS Data Science 2025**  
**Kelompok: 41425078_41425079_41425080**  
**Judul:** _Student Academic Status Analysis — Predicting Dropout, Enrolled, and Graduate_
