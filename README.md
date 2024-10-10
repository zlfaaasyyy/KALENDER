# KALENDER
Kalender adalah salah satu package Python yang menyediakan berbagai fungsi terkait penanggalan. Package ini membantu kita untuk bekerja dengan kalender, menentukan hari libur, dan sebagainya. Beberapa fitur utamanya adalah menampilkan bulan atau tahun dalam bentuk kalender, menentukan hari dalam minggu untuk tanggal tertentu, dan menghitung hari kerja.

# FUNGSI 1
Dokumentasi Program

Deskripsi

Program ini berfungsi untuk menampilkan kalender dari sebuah bulan di tahun tertentu yang diinputkan oleh pengguna. Pengguna dapat memasukkan nama bulan dalam bahasa Indonesia atau angka bulan (1-12). Program akan memvalidasi input dan menampilkan kalender untuk bulan tersebut.

Dependensi

Program ini menggunakan modul calendar bawaan dari Python untuk menghasilkan tampilan kalender. Modul ini tidak memerlukan instalasi tambahan.

Struktur Kode

	1.	Import Modul:
	•	import calendar: Mengimpor modul calendar yang digunakan untuk menampilkan kalender.
	2.	Inisialisasi Kamus Nama Bulan:
	•	nama_bulan adalah kamus yang menyimpan pasangan nama bulan (dalam bahasa Indonesia) dan angka bulan (1-12).
	3.	Input dari Pengguna:
	•	Program meminta dua input dari pengguna:
	•	Tahun dalam bentuk angka (int).
	•	Nama bulan atau angka bulan (bisa berupa string nama bulan dalam bahasa Indonesia atau angka dari 1 hingga 12).
	4.	Validasi Input:
	•	Jika Input Bulan Berupa Angka:
	•	Menggunakan fungsi isdigit() untuk memeriksa apakah input bulan adalah angka.
	•	Jika benar, angka tersebut dikonversi ke tipe integer dan diperiksa apakah berada dalam rentang 1 hingga 12.
	•	Jika valid, program menampilkan kalender untuk bulan tersebut.
	•	Jika tidak valid, program menampilkan pesan kesalahan.
	•	Jika Input Bulan Berupa Nama Bulan:
	•	Input diubah menjadi huruf kecil dengan lower() untuk menghindari masalah kapitalisasi.
	•	Nama bulan tersebut dicek apakah ada di dalam kamus nama_bulan.
	•	Jika nama bulan ditemukan dalam kamus, angka bulan yang sesuai digunakan untuk menampilkan kalender.
	•	Jika tidak valid, program menampilkan pesan kesalahan.
	5.	Output:
	•	Jika input valid, kalender bulan yang diminta ditampilkan menggunakan fungsi calendar.month(tahun, bulan).
	•	Jika input tidak valid, program menampilkan pesan kesalahan yang relevan.

Kode/Codingan Lengkap

import calendar

# Kamus nama bulan dalam bahasa Indonesia
nama_bulan = {
    "januari": 1,
    "februari": 2,
    "maret": 3,
    "april": 4,
    "mei": 5,
    "juni": 6,
    "juli": 7,
    "agustus": 8,
    "september": 9,
    "oktober": 10,
    "november": 11,
    "desember": 12
}

# Meminta input tahun dan bulan dari pengguna
tahun = int(input("Masukkan tahun: "))
inputan_bulan = input("Masukkan nama bulan atau angka bulan (1-12) : ")

# Validasi apakah input bulan adalah angka
if inputan_bulan.isdigit():
    bulan = int(inputan_bulan)
   
    # Memastikan bulan berada dalam rentang yang valid
    if 1 <= bulan <= 12:
        kal = calendar.month(tahun, bulan)
        print(kal)
    else:
        print("Bulan tidak valid. Silakan masukkan angka antara 1 dan 12.")
else:
    # Mengubah inputan menjadi huruf kecil
    inputan_bulan = inputan_bulan.lower()
    
    # Memeriksa apakah nama bulan ada di dalam kamus
    if inputan_bulan in nama_bulan:
        bulan = nama_bulan[inputan_bulan]
        
        # Menampilkan kalender
        kal = calendar.month(tahun, bulan)
        print(kal)
    else:
        print("Nama bulan tidak valid. Silakan coba lagi.")

Penjelasan Tambahan

	•	Fungsi calendar.month(tahun, bulan): Fungsi ini menampilkan kalender dalam bentuk string untuk bulan tertentu dalam format bulan dan tahun yang diberikan. Misalnya, calendar.month(2024, 10) akan menampilkan kalender untuk Oktober 2024.
	•	Fungsi input(): Digunakan untuk mengambil input dari pengguna. Karena inputan dari fungsi input() selalu berupa string, jika diperlukan, konversi ke tipe data lain seperti integer perlu dilakukan (seperti yang dilakukan pada input tahun).

Pesan Kesalahan

	•	Jika input bulan berupa angka di luar rentang 1-12, program akan menampilkan: "Bulan tidak valid. Silakan masukkan angka antara 1 dan 12."
	•	Jika nama bulan yang dimasukkan tidak ada dalam kamus nama_bulan, program akan menampilkan: "Nama bulan tidak valid. Silakan coba lagi."

Penggunaan

Program ini ideal digunakan untuk menampilkan kalender dari bulan tertentu di tahun tertentu dengan format yang rapi. Ini dapat menjadi bagian dari aplikasi yang melibatkan penjadwalan atau manajemen waktu.
