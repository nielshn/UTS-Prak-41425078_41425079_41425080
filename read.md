# LAPORAN PRAKTIKUM UTS DATA SCIENCE

## Kelompok 26

| NIM      | Nama                         |
| -------- | ---------------------------- |
| 41425078 | Daniel Siahaan               |
| 41425079 | Jessica Pasaribu             |
| 41425080 | Novrael Gabriel Louis Marbun |

---

### FAKULTAS VOKASI

### INSTITUT TEKNOLOGI DEL

### 2025

---

## **1. Pendahuluan**

### **1.1 Latar Belakang**

Perkembangan teknologi dan digitalisasi dalam bidang pendidikan telah menghasilkan beragam data akademik mahasiswa. Data ini menyimpan informasi berharga yang dapat dianalisis untuk memahami faktor-faktor yang memengaruhi keberhasilan studi, tingkat kelulusan, dan risiko putus kuliah (_dropout_). Melalui penerapan _data science_, analisis terhadap data pendidikan dapat dilakukan secara sistematis untuk menghasilkan wawasan berbasis bukti (_evidence-based insights_) guna mendukung pengambilan keputusan strategis di institusi pendidikan.

Proyek ini berfokus pada penerapan metode _data science_ untuk menganalisis dataset akademik mahasiswa dengan meninjau hubungan antara nilai masuk (_admission grade_) dan status akhir mahasiswa (_Dropout_, _Enrolled_, _Graduate_). Analisis dilakukan melalui tahapan utama: _data collection_, _data preprocessing_, _data visualization_, dan _statistical analysis_.

### **1.2 Tujuan**

1. Mengimplementasikan tahapan analisis data ilmiah terhadap dataset mahasiswa.
2. Melakukan visualisasi dan analisis statistik untuk menemukan pola dan hubungan antar variabel.
3. Menentukan apakah terdapat perbedaan signifikan nilai _admission grade_ antar kelompok status mahasiswa.
4. Memberikan rekomendasi berbasis data yang dapat membantu lembaga pendidikan dalam memahami faktor keberhasilan studi mahasiswa.

### **1.3 Rumusan Masalah**

1. Apakah terdapat perbedaan signifikan pada nilai _admission grade_ antar kategori status mahasiswa (_Graduate_, _Dropout_, _Enrolled_)?
2. Apakah terdapat hubungan antara nilai masuk dengan performa akademik semester pertama mahasiswa?
3. Faktor akademik mana yang paling berpengaruh terhadap status akhir mahasiswa berdasarkan hasil analisis statistik?

---

## **2. Metodologi Penelitian**

### **2.1 Alur Penelitian**

Penelitian ini mengikuti alur _data science pipeline_ sebagai berikut:

1. **Data Collection** – Memuat dan memeriksa dataset mahasiswa dari repositori terbuka.
2. **Data Preprocessing** – Melakukan penanganan _missing values_, _outlier_, _scaling_, dan _encoding_.
3. **Data Visualization** – Mengeksplorasi pola dan hubungan antar variabel menggunakan grafik.
4. **Statistical Analysis** – Melakukan uji parametrik (ANOVA) dan non-parametrik (Mann-Whitney, Spearman) untuk validasi hubungan data.

### **2.2 Sumber Data**

Dataset diambil dari **UCI Machine Learning Repository**, berjudul _“Predict Students Dropout and Academic Success”_. Dataset ini berisi data demografis, akademik, dan sosial ekonomi mahasiswa.

**Karakteristik dataset:**

- Jumlah observasi: ±4424 baris
- Jumlah fitur: 37 kolom
- Atribut mencakup: usia, status perkawinan, mode pendaftaran, _admission grade_, nilai per semester, dan _target_ akhir.

**Alasan Pemilihan Dataset:** Dataset ini kredibel, lengkap, serta memenuhi kriteria UTS (≥20 fitur dan ≥2000 baris data) dan relevan dengan analisis keberhasilan studi mahasiswa.

---

## **3. Hasil dan Pembahasan**

### **3.1 Data Collection & Loading**

Dataset dibaca menggunakan `pd.read_csv` dengan delimiter `;` dan encoding UTF-8. Nama kolom dinormalisasi menjadi _snake_case_. Dataset berukuran **4424×37** dengan kombinasi fitur numerik dan kategorikal. Tidak ditemukan duplikasi signifikan.

**Insight:** Dataset valid dan siap untuk proses analisis lebih lanjut.

---

### **3.2 Exploratory Data Analysis (EDA)**

1️⃣ **Distribusi Target** – Diagram batang menunjukkan mayoritas mahasiswa berstatus _Graduate_ → indikasi _class imbalance_.
2️⃣ **Statistik Deskriptif** – Menunjukkan variasi tinggi pada nilai akademik.
3️⃣ **Korelasi Numerik** – Korelasi kuat antara nilai semester 1 dan semester 2 menandakan konsistensi performa akademik mahasiswa.

---

### \*\*3.3 Data Preprocessing (Advanced Techniques)

Tahap preprocessing dilakukan untuk meningkatkan kualitas dan konsistensi data sebelum analisis statistik. Berikut tahapan yang dilakukan sesuai notebook ANOVA:

1️⃣ **Handling Missing Values (KNN Imputer)**
Nilai kosong diisi menggunakan metode _K-Nearest Neighbors (KNN) Imputer_, yang menghitung nilai berdasarkan tetangga terdekat dengan karakteristik serupa. Teknik ini menghasilkan imputasi yang lebih representatif dibandingkan metode rata-rata sederhana.

2️⃣ **Handling Outliers (IQR Trimming & Winsorization)**
Outlier pada kolom _admission_grade_ ditangani dengan dua tahap: _IQR trimming_ untuk menghapus nilai ekstrem di luar rentang interkuartil, dan _winsorization_ pada persentil ke-5 hingga ke-95 untuk membatasi pengaruh nilai ekstrem tanpa menghapus data penting.

3️⃣ **Feature Scaling (Standardization)**
Data numerik dinormalisasi menggunakan _StandardScaler_ agar semua fitur memiliki rata-rata 0 dan standar deviasi 1. Tahap ini penting untuk menjaga keseimbangan kontribusi setiap fitur pada analisis PCA dan uji statistik.

4️⃣ **Encoding Categorical Variables (One-Hot Encoding)**
Fitur kategorikal dikonversi ke bentuk numerik dengan _One-Hot Encoding_ untuk mencegah bias ordinal dan memastikan kompatibilitas dalam analisis berbasis numerik.

5️⃣ **Feature Reduction (Principal Component Analysis – PCA)**
Reduksi dimensi dilakukan menggunakan PCA untuk mempercepat analisis tanpa kehilangan informasi penting. Dua komponen utama pertama berhasil menjelaskan sebagian besar variasi data dan digunakan dalam visualisasi 2D.

---

### **3.4 Data Visualization**

| Jenis Visualisasi                                      | Alasan Pemilihan                                                                                                                                                                                                                              | Insight Utama                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bar Chart – Distribusi Status Mahasiswa**            | Dipilih untuk menampilkan proporsi jumlah mahasiswa dalam tiap kategori status akhir (_Dropout_, _Enrolled_, _Graduate_). Visualisasi ini memberikan gambaran cepat mengenai keseimbangan kelas dan dominasi kelompok tertentu dalam dataset. | Mayoritas mahasiswa berada pada kategori **Graduate**, diikuti oleh **Enrolled**, sedangkan **Dropout** adalah kelompok paling sedikit. Distribusi yang tidak seimbang (_class imbalance_) ini menunjukkan bahwa sebagian besar mahasiswa berhasil menyelesaikan studi, sehingga perlu perhatian khusus saat melakukan analisis komparatif dan uji statistik. |
| **Boxplot (Admission Grade per Target)**               | Menampilkan median, rentang antar kuartil (IQR), serta mendeteksi outlier dengan jelas. Cocok untuk membandingkan distribusi nilai antar kategori target.                                                                                     | Mahasiswa **Graduate** memiliki median _admission grade_ lebih tinggi dibanding **Dropout**, menandakan perbedaan performa akademik awal yang signifikan.                                                                                                                                                                                                     |
| **Scatter Plot (Admission Grade vs Application Mode)** | Efektif untuk mengidentifikasi pola atau korelasi antara dua variabel numerik.                                                                                                                                                                | Tidak ditemukan hubungan linear antara mode pendaftaran dan nilai masuk, menunjukkan bahwa faktor administratif tidak berpengaruh kuat terhadap performa akademik.                                                                                                                                                                                            |
| **Heatmap Korelasi**                                   | Memberikan gambaran umum mengenai kekuatan hubungan antar fitur numerik.                                                                                                                                                                      | Korelasi tinggi antara nilai akademik semester 1 dan 2 menunjukkan konsistensi performa mahasiswa sepanjang periode awal perkuliahan.                                                                                                                                                                                                                         |

---

## **3.5 Statistical Analysis (Refactored)**

### **a. Uji Parametrik — One-Way ANOVA & Levene Test**

**Tujuan:**
Menilai apakah rata-rata _admission_grade_ berbeda signifikan antar kategori _Target_ (Dropout, Enrolled, Graduate).

**Hipotesis:**

- **H₀:** Tidak ada perbedaan rata-rata _admission_grade_ antara ketiga kelompok.
- **H₁:** Terdapat perbedaan signifikan rata-rata _admission_grade_ antar kelompok.

**Hasil:**

- **Levene Test:** p = 0.00015 → varians antar grup **tidak homogen**.
- **ANOVA:** p = 1.14×10⁻¹⁷ → **signifikan (p < 0.05)**.

**Keputusan:** Karena nilai p < 0.05, maka **H₀ ditolak** dan **H₁ diterima**.
Artinya, terdapat **perbedaan signifikan rata-rata _admission_grade_** antara mahasiswa Dropout, Enrolled, dan Graduate.

**Interpretasi:**
Mahasiswa _Graduate_ memiliki nilai _admission_grade_ lebih tinggi dibandingkan kelompok _Dropout_. Hasil ini menunjukkan bahwa kemampuan akademik awal berkontribusi terhadap peluang keberhasilan studi mahasiswa.

**Effect Size (η²) ≈ 0.06 → efek moderat.**
Efek moderat ini menandakan bahwa _admission_grade_ menjelaskan sebagian variasi status akademik mahasiswa secara bermakna.

---

### **b. Uji Non-Parametrik — Kruskal–Wallis dan Mann–Whitney U**

**Kruskal–Wallis Test:** p = 1.19×10⁻¹⁶ → signifikan (p < 0.05).
**Mann–Whitney U (Dropout vs Graduate):** p = 1.95×10⁻¹⁵ → signifikan.

**Interpretasi:**
Temuan ini memperkuat hasil ANOVA bahwa terdapat perbedaan distribusi nilai masuk antar kelompok. Mahasiswa _Graduate_ memiliki _admission_grade_ yang lebih tinggi dibanding _Dropout_.

---

### **c. Korelasi Spearman**

**ρ = 0.209, p = 3.82×10⁻⁴⁴ → korelasi positif lemah namun signifikan** antara _admission_grade_ dan _curricular_units_1st_sem_grade_.

**Interpretasi:**
Mahasiswa dengan nilai masuk tinggi cenderung mempertahankan performa akademik yang baik pada semester pertama. Hubungan ini mendukung hipotesis bahwa kualitas akademik awal berdampak pada keberhasilan studi.

---

## **5. Pembahasan (Refactored)**

Berdasarkan hasil uji statistik dan analisis visual, diperoleh beberapa temuan penting:

1️⃣ **Perbedaan Signifikan Nilai Akademik Antar Kategori Mahasiswa.**
Uji ANOVA menghasilkan p = 1.14×10⁻¹⁷, yang menunjukkan adanya perbedaan signifikan rata-rata _admission_grade_ antara mahasiswa Dropout, Enrolled, dan Graduate. Karena asumsi homogenitas varians tidak terpenuhi (Levene Test p = 0.00015), maka dilakukan verifikasi menggunakan uji non-parametrik Kruskal–Wallis dan Mann–Whitney U. Keduanya menghasilkan hasil yang signifikan, sehingga memperkuat keputusan untuk menolak H₀.
Dengan demikian, mahasiswa yang memiliki _admission_grade_ tinggi secara konsisten lebih mungkin untuk lulus (_Graduate_) dibandingkan yang memiliki nilai rendah (_Dropout_).

2️⃣ **Konsistensi Performa Akademik Awal.**
Hasil korelasi Spearman (ρ = 0.209, p < 0.001) menunjukkan hubungan positif antara _admission_grade_ dan nilai akademik semester pertama. Ini berarti performa awal mahasiswa menjadi indikator penting terhadap kesuksesan studi selanjutnya.

3️⃣ **Dampak Preprocessing terhadap Validitas Hasil.**
Tahapan _IQR trimming_, _winsorization_, _standardization_, dan _encoding_ berperan penting dalam meningkatkan reliabilitas hasil. Data yang sudah dibersihkan menghasilkan distribusi lebih normal dan hasil uji statistik yang lebih stabil serta akurat.

**Interpretasi Umum:**
Faktor akademik awal terbukti berpengaruh signifikan terhadap keberhasilan studi mahasiswa. Uji ANOVA dan Kruskal–Wallis menunjukkan adanya perbedaan yang bermakna pada nilai masuk antar kelompok, sementara korelasi Spearman menegaskan hubungan positif antara performa awal dan kelulusan. Oleh karena itu, hasil ini dapat digunakan oleh institusi pendidikan untuk mengembangkan sistem deteksi dini mahasiswa berisiko _dropout_.

---

## **4. Kesimpulan (Updated)**

1. Berdasarkan hasil **ANOVA (p = 1.14×10⁻¹⁷)** dan **Kruskal–Wallis (p = 1.19×10⁻¹⁶)**, hipotesis nol (**H₀**) ditolak — terdapat **perbedaan signifikan rata-rata _admission_grade_** antar kategori mahasiswa.
2. **Mahasiswa dengan nilai masuk tinggi** cenderung memiliki peluang lebih besar untuk menyelesaikan studi (kategori _Graduate_).
3. Korelasi Spearman menunjukkan **hubungan positif lemah namun signifikan** antara nilai masuk dan performa akademik semester pertama.
4. Tahapan preprocessing terbukti mendukung validitas hasil uji statistik.

**Kesimpulan Akhir:**
Terdapat bukti kuat bahwa _admission_grade_ berperan penting dalam menentukan status akhir mahasiswa. Hipotesis alternatif (**H₁**) diterima: _nilai masuk berpengaruh signifikan terhadap keberhasilan studi mahasiswa_.

---

## **5. Rekomendasi dan Pengembangan Lanjutan**

- Menambahkan analisis regresi logistik untuk prediksi probabilitas _dropout_.
- Mengembangkan model pembelajaran mesin (Random Forest, XGBoost) dengan validasi kinerja.
- Menerapkan dashboard interaktif untuk memantau performa akademik mahasiswa secara real-time.

---

## **6. Daftar Pustaka**

1. UCI Machine Learning Repository: _Predict Students Dropout and Academic Success_. [https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)
2. Field, A. (2018). _Discovering Statistics Using IBM SPSS Statistics_ (5th ed.). SAGE Publications.
3. Montgomery, D. C. (2017). _Design and Analysis of Experiments_. John Wiley & Sons.

---

## **7. Lampiran**

- Gambar 1. Bar Chart Distribusi Target Mahasiswa
- Gambar 2. Boxplot Admission Grade per Target
- Gambar 3. Heatmap Korelasi Numerik
- Gambar 4. PCA 2D Plot
- Gambar 5. Output Uji Statistik (Levene, ANOVA, Kruskal-Wallis, Mann-Whitney, Spearman)
