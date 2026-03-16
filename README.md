# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang sangat baik dalam mencetak lulusan berkualitas. Namun, di balik keberhasilan tersebut, institusi ini menghadapi tantangan besar berupa tingginya angka mahasiswa yang tidak menyelesaikan pendidikannya alias *dropout*. Angka *dropout* yang tinggi ini berdampak negatif pada citra institusi dan stabilitas finansial. Oleh karena itu, Jaya Jaya Institut membutuhkan sebuah sistem peringatan dini (*early warning system*) yang dapat mendeteksi potensi mahasiswa *dropout* secepat mungkin agar pihak kampus dapat memberikan bimbingan atau intervensi khusus.

### Permasalahan Bisnis
Permasalahan utama yang ingin diselesaikan dalam proyek ini adalah:
1. Tingginya persentase mahasiswa yang mengalami *dropout* (mencapai sekitar 32% dari total mahasiswa).
2. Pihak institusi belum mengetahui secara pasti faktor-faktor utama (baik dari sisi demografi, akademik, maupun sosio-ekonomi) yang menjadi penyebab dominan mahasiswa melakukan *dropout*.
3. Belum adanya sistem terotomatisasi yang bisa membantu staf akademik memprediksi status mahasiswa (Dropout, Enrolled, atau Graduate) di masa depan.

### Cakupan Proyek
Proyek ini mencakup siklus penuh *Data Science* (*End-to-End*), meliputi:
1. **Data Preparation & Exploratory Data Analysis (EDA):** Membersihkan data, melakukan *encoding*, serta menganalisis korelasi antar variabel untuk menemukan akar masalah *dropout*.
2. **Data Modeling:** Membangun dan mengevaluasi model *Machine Learning* klasifikasi. Model yang dipilih adalah **Random Forest Classifier** karena kemampuannya memberikan *Feature Importance* dan akurasi yang tinggi pada data tabular.
3. **Business Dashboard:** Membuat visualisasi interaktif menggunakan Looker Studio untuk memantau performa mahasiswa dan metrik-metrik penyebab *dropout*.
4. **Machine Learning Prototype:** Mengembangkan aplikasi prediksi berbasis web menggunakan Streamlit yang mendukung prediksi tunggal maupun prediksi massal (menggunakan *file* CSV).


### Persiapan

Sumber data: Dataset "Students' Performance" yang berisi rekam jejak demografi, finansial, dan akademik mahasiswa dari Jaya Jaya Institut (Tersedia dalam format `.csv`).

Setup Environment:

pergi ke direkttori projek 
jalankan
'pip install -r requairement.txt'

## Business Dashboard
Business Dashboard telah dibangun menggunakan **Looker Studio** untuk memberikan kemudahan bagi manajemen Jaya Jaya Institut dalam memonitor profil mahasiswa. Dashboard ini menyoroti beberapa faktor paling krusial penyebab *dropout* berdasarkan hasil analisis data, yaitu:
- **Tunggakan Uang Kuliah:** Visualisasi *Stacked Bar Chart* yang menunjukkan bahwa mayoritas mahasiswa yang menunggak pembayaran uang kuliah berujung pada status *Dropout*.
- **Kepemilikan Beasiswa:** *Donut Chart* yang mendemonstrasikan bahwa sangat sedikit mahasiswa pemegang beasiswa yang mengalami *dropout*, sehingga beasiswa terbukti menjadi *safety net* yang baik.
- **Performa Akademik:** Perbandingan rata-rata nilai dan jumlah SKS yang lulus pada Semester 1 dan 2.

**Link Dashboard:** [[dashboard](https://lookerstudio.google.com/reporting/304d1210-ba16-423c-8c7e-cca8ff810e99)] 

## Menjalankan Sistem Machine Learning
Prototype sistem Machine Learning dibangun menggunakan **Streamlit**. Aplikasi ini memiliki dua fitur utama:
1. **Prediksi Tunggal:** User dapat memasukkan 6 parameter terpenting (seperti Status Uang Kuliah, Beasiswa, dan Nilai Semester) melalui *form interface* untuk memprediksi status satu mahasiswa.
2. **Prediksi Massal:** User dapat mengunggah *file* data mentah (`.csv`) berisi 36 kolom dari ratusan mahasiswa sekaligus. Sistem akan memproses dan mengeluarkan *output* file yang dapat diunduh lengkap dengan hasil prediksinya.

**Link Dashboard:** [[Streamlit](https://student-dropout-prediction-kwsuvky7f8zhlrdn2ky7pd.streamlit.app/)] 

## Conclusion
Dari hasil proses analisis data dan pemodelan yang telah dilakukan, dapat ditarik beberapa kesimpulan utama:

- Angka dropout di Jaya Jaya Institut sangat memprihatinkan, yakni mencapai ~32.1%.

- Berdasarkan analisis Feature Importance dari model Random Forest dan pengamatan EDA, faktor finansial merupakan prediktor paling kuat terjadinya dropout. Mahasiswa yang menunggak uang kuliah memiliki risiko dropout hingga 86.6%.

- Beasiswa adalah penangkal yang efektif. Mahasiswa tanpa beasiswa memiliki tingkat dropout 38.7%, sedangkan mereka yang memiliki beasiswa angka dropout-nya turun drastis menjadi hanya 12.2%.

- Tanda bahaya akademik terlihat sejak Semester 1. Mahasiswa yang berakhir dropout rata-rata memiliki nilai dan jumlah kelulusan SKS yang sangat rendah sejak awal perkuliahan, jauh dibandingkan mahasiswa yang berhasil lulus.

### Rekomendasi Action Items
Untuk menekan tingginya angka dropout, Jaya Jaya Institut direkomendasikan untuk menerapkan langkah-langkah strategis berikut:

- Membangun Sistem Notifikasi Finansial (Financial Early Warning): Mengintegrasikan prototipe Machine Learning ke sistem administrasi untuk memberikan notifikasi otomatis (flagging) kepada mahasiswa yang mulai menunggak pembayaran, agar segera dicarikan solusi cicilan atau bantuan.

- Optimalisasi dan Pemerataan Beasiswa: Memperbesar kuota atau mencari mitra sponsor untuk memberikan subsidi/beasiswa tambahan yang diprioritaskan bagi mahasiswa berprestasi yang sedang mengalami kesulitan finansial.

- Program Mentoring Akademik Semester 1: Mewajibkan mahasiswa yang mendapatkan nilai IP/SKS di bawah standar aman pada Semester 1 untuk mengikuti bimbingan konseling dan program tutoring agar mereka tidak semakin tertinggal di semester berikutnya.