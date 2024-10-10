# KALENDER
Kalender adalah salah satu package Python yang menyediakan berbagai fungsi terkait penanggalan. Package ini membantu kita untuk bekerja dengan kalender, menentukan hari libur, dan sebagainya. Beberapa fitur utamanya adalah menampilkan bulan atau tahun dalam bentuk kalender, menentukan hari dalam minggu untuk tanggal tertentu, dan menghitung hari kerja.

## FUNGSI 1
Dokumentasi Program

### Deskripsi

Program ini berfungsi untuk menampilkan kalender dari sebuah bulan di tahun tertentu yang diinputkan oleh pengguna. Pengguna dapat memasukkan nama bulan dalam bahasa Indonesia atau angka bulan (1-12). Program akan memvalidasi input dan menampilkan kalender untuk bulan tersebut.

### Dependensi

Program ini menggunakan modul calendar bawaan dari Python untuk menghasilkan tampilan kalender. Modul ini tidak memerlukan instalasi tambahan.

```python
Kode/Codingan Lengkap
import calendar

### Kamus nama bulan dalam bahasa Indonesia
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

### Meminta input tahun dan bulan dari pengguna
def tampilkan_kalender():
    while True:
        try:
            
            ### Validasi apakah input bulan adalah angka
            if inputan_bulan.isdigit():
                bulan = int(inputan_bulan)
                
                ### Memastikan bulan berada dalam rentang yang valid
                if 1 <= bulan <= 12:
                    print(calendar.month(tahun, bulan))
                    break
                else:
                    print("Bulan tidak valid. Silahkan masukkan angka antara 1 dan 12.")
            
            ### Memeriksa apakah nama bulan ada di dalam kamus
            elif inputan_bulan in nama_bulan:
                bulan = nama_bulan[inputan_bulan]
                ### Menampilkan kalender
                print(calendar.month(tahun, bulan))
                break
            else:
                print("Nama bulan tidak valid. Silahkan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silahkan coba lagi.")


tampilkan_kalender()

```
### Penjelasan Tambahan

	•	Fungsi calendar.month(tahun, bulan): Fungsi ini menampilkan kalender dalam bentuk string untuk bulan tertentu dalam format bulan dan tahun yang diberikan. Misalnya, calendar.month(2024, 10) akan menampilkan kalender untuk Oktober 2024.
	
###  Pesan Kesalahan

	•	Jika input bulan berupa angka di luar rentang 1-12, program akan menampilkan: "Bulan tidak valid. Silakan masukkan angka antara 1 dan 12."
	•	Jika nama bulan yang dimasukkan tidak ada dalam kamus nama_bulan, program akan menampilkan: "Nama bulan tidak valid. Silakan coba lagi."

### Penggunaan

Program ini ideal digunakan untuk menampilkan kalender dari bulan tertentu di tahun tertentu dengan format yang rapi. Ini dapat menjadi bagian dari aplikasi yang melibatkan penjadwalan atau manajemen waktu.
