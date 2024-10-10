# KALENDER
### Fungsi 6
### Dokumentasi program

##### 
```python
hari_dalam_indonesia = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
```
- **Deskripsi**: List `hari_dalam_indonesia` menyimpan nama-nama hari dalam Bahasa Indonesia dari Senin hingga Minggu. Digunakan untuk mengonversi hasil dari fungsi `calendar.weekday()` ke nama hari dalam Bahasa Indonesia.

#####
```python
bulan_dalam_indonesia = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4,
    "Mei": 5, "Juni": 6, "Juli": 7, "Agustus": 8,
    "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}
```
- **Deskripsi**: Kamus `bulan_dalam_indonesia` digunakan untuk memetakan nama-nama bulan dalam Bahasa Indonesia ke angka bulan yang sesuai. Misalnya, "Januari" dikonversi menjadi 1, "Februari" menjadi 2, dan seterusnya.

#####
```python
def is_weekday(year, month, day):
```
- **Deskripsi**: Fungsi ini mengecek apakah hari tertentu adalah hari kerja (Senin-Jumat).
- **Parameter**:
  - `year` (*int*): tahun.
  - `month`: bulan (bisa dalam bentuk nama atau angka).
  - `day` (*int*): tanggal.
- Fungsi `calendar.weekday(year, month, day)` mengembalikan nilai integer dari 0 hingga 6:
  - 0 adalah Senin, 1 adalah Selasa, dan seterusnya hingga 6 untuk Minggu.
- Jika nilai yang dikembalikan oleh `calendar.weekday()` lebih kecil dari 5, artinya itu adalah hari kerja.
- **Output**:
  - Menampilkan apakah hari tersebut hari kerja atau akhir pekan dalam format `DD/MM/YYYY`.
  - Mengembalikan `True` jika hari adalah hari kerja, dan `False` jika tidak.

#####
```python
def is_weekend(year, month, day):
```
- **Deskripsi**: Fungsi ini mengecek apakah hari tertentu adalah akhir pekan (Sabtu-Minggu).
- **Parameter**:
  - `year` (*int*): tahun.
  - `month`: bulan (bisa dalam bentuk nama atau angka).
  - `day` (*int*): tanggal.
- Fungsi ini menggunakan `is_weekday()` untuk menentukan apakah hari tersebut adalah hari kerja. Jika bukan, maka itu akhir pekan.
- **Output**:
  - Menampilkan apakah hari tersebut akhir pekan atau hari kerja dalam format `DD/MM/YYYY`.
  - Mengembalikan `True` jika hari adalah akhir pekan, dan `False` jika tidak.

#####
```python
def get_day_name(year, month, day):
```
- **Deskripsi**: Fungsi ini mengembalikan nama hari dalam Bahasa Indonesia untuk tanggal tertentu.
- **Parameter**:
  - `year` (*int*): tahun.
  - `month`: bulan (bisa dalam bentuk nama atau angka).
  - `day` (*int*): tanggal.
- Fungsi `calendar.weekday(year, month, day)` mengembalikan nilai integer dari 0 hingga 6, yang kemudian digunakan untuk mengambil nama hari dari list `hari_dalam_indonesia`.
- **Output**:
  - Menampilkan nama hari dalam Bahasa Indonesia untuk tanggal tertentu.
  - Mengembalikan nama hari sebagai string.

#####
```python
def convert_month_to_int(month):
```
- **Deskripsi**: Fungsi ini mengonversi nama bulan (string) menjadi angka.
- Jika input `month` adalah angka, fungsi langsung mengembalikannya.
- Jika input adalah string, misalnya "Oktober", fungsi akan mengecek apakah string tersebut ada di dalam kamus `bulan_dalam_indonesia`. Jika ada, akan dikonversi ke angka bulan yang sesuai.
- Jika string bulan tidak valid, maka fungsi akan melemparkan error `ValueError`.
- Jika tipe data yang diterima bukan string atau integer, akan melemparkan `TypeError`.
