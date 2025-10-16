# 🎓 UTS Data Science: Analisis Data Student Academic Status (Final ANOVA Version)

## 🧠 Business Understanding

Lembaga pendidikan tinggi sering menghadapi masalah **dropout mahasiswa** dan **kelulusan tidak tepat waktu**, yang berdampak pada reputasi dan efisiensi operasional institusi. Analisis data akademik dan sosial ekonomi mahasiswa dapat membantu mendeteksi pola risiko dini dan menjadi dasar kebijakan akademik adaptif.

**Tujuan:**

1. Mengidentifikasi faktor-faktor yang berhubungan dengan status akademik mahasiswa.
2. Memberikan insight berbasis data untuk pengambilan keputusan akademik.

---

## ⚙️ Data Collection

**Sumber Data:**
Dataset: *Predict Students Dropout and Academic Success* (UCI Machine Learning Repository)
Link referensi: [https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

**Deskripsi Singkat:**

* Jumlah baris: 4424 mahasiswa
* Jumlah fitur: 37 fitur (demografis, sosial ekonomi, akademik)
* Target: `Target` (Dropout / Enrolled / Graduate)

**Insight:**
Data memenuhi kriteria UTS (≥20 fitur dan ≥2000 baris) dan siap untuk analisis statistik dan visualisasi.

---

## 📊 Data Visualization

### a. Histogram — Distribusi Target Mahasiswa

**Alasan:** Untuk memahami proporsi status akademik mahasiswa.
**Insight:** Sebagian besar mahasiswa berada pada kategori **Graduate**.
**Interpretasi:** Dataset bersifat tidak seimbang (class imbalance) sehingga perlu diperhatikan saat analisis inferensial.

### b. Boxplot — Admission Grade per Target

**Alasan:** Menganalisis perbandingan nilai masuk antar kelompok status mahasiswa.
**Insight:** Median nilai masuk mahasiswa **Graduate** lebih tinggi dibanding **Dropout**.
**Interpretasi:** Mengindikasikan bahwa nilai masuk berperan penting terhadap keberhasilan studi.

### c. Heatmap Korelasi — Hubungan Antar Numeric Features

**Alasan:** Mengidentifikasi hubungan antar variabel akademik.
**Insight:** Korelasi tinggi antara `Curricular units 1st sem (approved)` dan `Curricular units 1st sem (grade)` menunjukkan konsistensi performa akademik.
**Interpretasi:** Fitur dengan korelasi tinggi dapat digunakan untuk reduksi dimensi (PCA).

### d. PCA 2D Visualization

**Alasan:** Melihat pola cluster antar kategori target.
**Insight:** Kelompok **Graduate** relatif terpisah dari **Dropout** pada ruang PCA.
**Interpretasi:** Variabel akademik memiliki kemampuan diskriminatif terhadap status akhir mahasiswa.

---

## 🧹 Data Processing and Techniques (Advance Preprocessing)

### a. Handling Missing Values

**Teknik:** `KNNImputer` untuk numerik dan mode imputation untuk kategorikal.
**Insight:** Menghindari bias akibat data kosong dan menjaga integritas dataset.

### b. Handling Outliers

**Teknik:** IQR trimming & Winsorization (5th–95th percentile).
**Insight:** Mengurangi pengaruh nilai ekstrem tanpa menghapus data penting.
**Interpretasi:** Membuat distribusi data lebih stabil untuk analisis statistik.

### c. Feature Scaling

**Teknik:** `StandardScaler`.
**Insight:** Menyamakan skala antar fitur numerik.
**Interpretasi:** Diperlukan untuk analisis PCA dan perbandingan antar variabel.

### d. Encoding Categorical Variables

**Teknik:** One-Hot Encoding.
**Insight:** Mengubah fitur kategorikal menjadi representasi numerik.
**Interpretasi:** Memungkinkan semua fitur digunakan dalam model statistik.

### e. Feature Reduction

**Teknik:** PCA (10 komponen utama).
**Insight:** 90% variansi data dapat dijelaskan oleh 10 komponen.
**Interpretasi:** Reduksi dimensi meningkatkan efisiensi analisis tanpa kehilangan informasi penting.

---

## 📈 Statistical Analysis (Real Results)

### a. Levene Test — Homogenitas Varians

**Hasil:** p = 0.00015
**Interpretasi:** Varians antar kelompok tidak homogen, sehingga ANOVA perlu dikonfirmasi dengan uji non-parametrik tambahan.

### b. Uji Parametrik — One-Way ANOVA

**Hasil:** p = 1.14e-17
**Interpretasi:** Terdapat perbedaan signifikan pada *admission_grade* antar kategori `Target` (**Dropout**, **Enrolled**, **Graduate**).
Mahasiswa dengan nilai masuk lebih tinggi cenderung memiliki status **Graduate**.
**Effect Size (η²):** 0.06 → efek moderat.

### c. Uji Non-Parametrik — Kruskal-Wallis Test

**Hasil:** p = 1.20e-16
**Interpretasi:** Hasil signifikan, memperkuat temuan ANOVA meskipun varians antar kelompok tidak homogen.

### d. Uji Non-Parametrik — Mann-Whitney U Test

**Hasil:** p = 1.95e-15
**Interpretasi:** Distribusi *admission_grade* mahasiswa **Graduate** secara signifikan lebih tinggi dibanding **Dropout**.
**Kesimpulan:** Perbedaan nyata antar kelompok tetap konsisten di uji non-parametrik.

### e. Korelasi Spearman

**Hasil:** ρ = 0.209, p ≈ 0.0
**Interpretasi:** Terdapat korelasi positif lemah namun signifikan antara *admission_grade* dan *curricular_units_1st_sem_grade*.
Mahasiswa dengan nilai masuk lebih tinggi cenderung memiliki performa akademik lebih baik di semester pertama.

---

## ✅ Kesimpulan Akhir

1. **Nilai masuk (admission_grade)** memiliki pengaruh signifikan terhadap status akhir mahasiswa.
2. Hasil **ANOVA** dan **Kruskal-Wallis** menunjukkan perbedaan nyata antar kategori *Dropout*, *Enrolled*, dan *Graduate*.
3. **Mann-Whitney U** memperkuat hasil bahwa mahasiswa *Graduate* memiliki nilai masuk lebih tinggi dibanding *Dropout*.
4. **Korelasi Spearman** menunjukkan hubungan positif antara nilai masuk dan performa akademik semester pertama.
5. Temuan ini dapat digunakan sebagai dasar pengembangan sistem deteksi dini risiko *dropout* dan intervensi akademik adaptif di perguruan tinggi.

---

## 👥 Author

**Daniel Siahaan, Jessica Pasaribu, Novrael Marbun – UTS Data Science 2025**
**Kelompok:** 41425078_41425079_41425080
**Judul:** *Student Academic Status Analysis — Predicting Dropout, Enrolled, and Graduate*
