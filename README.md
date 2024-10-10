# KALENDER
Kalender adalah salah satu package Python yang menyediakan berbagai fungsi terkait penanggalan. Package ini membantu kita untuk bekerja dengan kalender, menentukan hari libur, dan sebagainya. Beberapa fitur utamanya adalah menampilkan bulan atau tahun dalam bentuk kalender, menentukan hari dalam minggu untuk tanggal tertentu, dan menghitung hari kerja.

### FUNGSI 1
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

### Fungsi 2
Dokumentasi program

#####
```python
tampilkan_bulan_range(tahun, bulan_awal, bulan_akhir):
```
- **Deskripsi**: Menampilkan bulan dalam satu tahun.
- **Parameter**:
  - `tahun` (*int*): Tahun yang ingin ditampilkan kalendernya. Contoh: 2024.
  - `bulan_awal` (*int*): Bulan pertama dalam rentang (1 = Januari, 2 = Februari, dst.). Bulan ini harus berada dalam range 1 hingga 12.
  - `bulan_akhir` (*int*): Bulan terakhir dalam rentang (1 = Januari, 2 = Februari, dst.). Bulan ini juga harus berada dalam range 1 hingga 12, dan tidak boleh lebih kecil dari `bulan_awal`.
- **Return Value**: String : Fungsi mengembalikan representasi kalender dari bulan-bulan dalam rentang yang diberikan. Setiap bulan akan dipisahkan oleh baris kosong.

### FUNGSI 3
Deskripsi

Kode ini berfungsi untuk menampilkan kalender lengkap dari tahun yang ditentukan oleh pengguna, dalam rentang antara tahun awal dan tahun akhir. Dengan menggunakan modul calendar, program meminta pengguna untuk memasukkan dua tahun, lalu mencetak kalender untuk setiap tahun dalam rentang tersebut. Hal ini berguna untuk perencanaan acara, pembelajaran tentang hari-hari tertentu, dan sebagai referensi cepat untuk melihat tanggal penting dalam beberapa tahun sekaligus.

### IMPORT CALENDER
import calendar
   
Kode ini mengimpor modul calendar, yang menyediakan berbagai fungsi untuk bekerja dengan kalender.

### DEFINISI FUNGSI
def tampilkan_kalender_range(start_year, end_year)
   
Fungsi ini, tampilkan_kalender_range, menerima dua argumen: start_year dan end_year. Fungsi ini akan menampilkan kalender untuk setiap tahun dalam rentang yang ditentukan.

### LOOP UNTUK SETIAP TAHUN
for year in range(start_year, end_year + 1):

print(calendar.calendar(year))

Dalam loop ini, range(start_year, end_year + 1) menghasilkan semua tahun dari start_year hingga end_year (inklusif). Untuk setiap tahun, fungsi calendar.calendar(year) dipanggil, yang menghasilkan string yang merepresentasikan kalender tahun tersebut, lalu mencetaknya.

### INPUT TAHUN
start_year = int(input("Masukkan tahun awal: "))
   
end_year = int(input("Masukkan tahun akhir: "))
   
Di sini, kode meminta pengguna untuk memasukkan tahun awal dan tahun akhir. Input yang diberikan oleh pengguna dikonversi menjadi tipe integer.

### MEMANGGIL FUNGSI
tampilkan_kalender_range(start_year, end_year)
   
Terakhir, fungsi tampilkan_kalender_range dipanggil dengan argumen yang diberikan oleh pengguna.

### CONTOH PENGGUNAAN
Jika pengguna memasukkan 2020 sebagai tahun awal dan 2022 sebagai tahun akhir, kode akan mencetak kalender untuk tahun 2020, 2021, dan 2022.

### INFO TAMBAHAN
Kode ini memungkinkan pengguna untuk melihat kalender dari satu tahun ke tahun lainnya dengan mudah menggunakan fungsi dari modul calendar di Python.

### Fungsi 4
fungsi ini berfungsi untuk mengambil dan menampilkan hari libur nasional di Indonesia berdasarkan tahun dan bulan yang ditentukan.

### Instal PIP holidays
Fungsi ini memanfaatkan library holidays untuk mendapatkan data hari libur dan calendar untuk format tanggal. Oleh karena itu, untuk menjalankan fungsi ini, kita perlu menginstal library holidays terlebih dahulu menggunakan PIP.

### Mengimpor Library
```import holidays``` ```import calendar```

Untuk menggunakan modul/library tersebut, bisa kita panggil dengan metode import(). Dimana import holidays, yang menyediakan informasi tentang hari libur nasional di berbagai negara, termasuk Indonesia. Dan import calendar, yang menyediakan fungsi terkait kalender, seperti nama bulan dan hari dalam sebulan.

### Fungsi ambil_hari_libur
```ambil_hari_libur(tahun,bulan)```

Fungsi ini mengambil hari libur nasional untuk bulan dan tahun tertentu.

Dalam fungsi ini kami menggunakan beberapa parameter :
- tahun (int): Tahun yang ingin diperiksa
- bulan (int): Bulan yang ingin diperiksa

### Mengembalikan hasil :
Mengembalikan dictionary hari_libur_bulanan, yang berisi hari libur nasional untuk bulan dan tahun yang diminta.

### Fungsi tampilkan_hari_libur
```tampilkan_hari_libur(tahun,bulan)```

Fungsi ini menampilkan daftar hari libur nasional dalam format yang mudah dibaca.

Beberapa paramter yang kami gunakan dalam fungsi ini :
- tahun (int): Tahun untuk menampilkan hari libur.
- bulan (int): Bulan untuk menampilkan hari libur (1-12).

### Pemanggilan Fungsi 
Memanggil fungsi ambil_hari_libur untuk mendapatkan hari libur yang relevan berdasarkan tahun dan bulan yang diberikan.

### Mengembalikan Hasil
Mengembalikan list hasil yang berisi informasi tentang hari libur atau pesan yang menyatakan tidak ada hari libur.

### FUNGSI 5

Fungsi ini digunakan untuk memeriksa apakah suatu tahun adalah tahun kabisat (leap year) atau bukan. Tahun kabisat adalah tahun yang jumlah harinya 366, terjadi setiap 4 tahun sekali, kecuali pada tahun yang kelipatan 100 tetapi bukan kelipatan 400.

### Memasukkan tahun
tahun (int): Memasukkan angka tahun yang akan diperiksa apakah merupakan tahun kabisat atau bukan.

### Mengecek tahun adalah kabisat atau bukan
```python
def cek_tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
```
Menghitung apakah tahun yang diinput termasuk kabisat, dengan menggunakan rumus di atas.

### Mengembalikan fungsi
Pengembalian:

string: Fungsi akan mengembalikan pesan dalam bentuk string yang menyatakan apakah tahun yang diberikan adalah tahun kabisat atau bukan.

### Syarat-syarat suatu tahun termasuk kabisat
Tahun kabisat terjadi jika memenuhi salah satu dari dua kondisi berikut:

1. Tahun habis dibagi 4 dan tidak habis dibagi 100.
2. Tahun habis dibagi 400.
