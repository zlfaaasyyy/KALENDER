# KALENDER
## FUNGSI 6
Deskripsi
Fungsi ini berfungsi untuk melakukan pengecekan apakah suatu tanggal merupakan hari kerja atau akhir pekan, dan juga untuk mendapatkan nama hari dalam Bahasa Indonesia.

```python
import calendar
```
- **Deskripsi**: Kode ini mengimpor modul calendar, yang menyediakan berbagai fungsi untuk bekerja dengan kalender.

###
```python
hari_dalam_indonesia = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
```
- **Deskripsi**: List ini menyimpan nama-nama hari dalam Bahasa Indonesia dari Senin hingga Minggu. Setiap hari diindeks dari 0 (Senin) hingga 6 (Minggu).

###
```python
bulan_dalam_indonesia = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4,
    "Mei": 5, "Juni": 6, "Juli": 7, "Agustus": 8,
    "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}
```
- **Deskripsi**: Dictionary ini mengonversi nama bulan dalam Bahasa Indonesia menjadi angka yang digunakan dalam fungsi-fungsi kalender di Python (`calendar`). Januari = 1, Februari = 2, dan seterusnya.

### Fungsi `validasi_tanggal`
```python
def validasi_tanggal(tahun, bulan, hari):
```
- **Deskripsi**: Fungsi ini memvalidasi apakah suatu tanggal tertentu valid berdasarkan tahun, bulan, dan hari.
- **Parameter**:
  - `tahun` (*int*): tahun.
  - `bulan`: bulan (bisa dalam bentuk string/nama atau angka).
  - `hari` (*int*): tanggal.
- **Langkah-langkah**:
  - Mengonversi bulan dari string ke angka menggunakan fungsi `konversi_bulan_int`.
  - Menggunakan fungsi `calendar.monthrange` untuk mendapatkan jumlah hari dalam bulan tertentu pada tahun tersebut.
  - Memeriksa apakah hari yang diberikan berada dalam rentang jumlah hari yang valid.
  - Jika tanggal tidak valid, program menampilkan pesan error dan mengembalikan nilai `False`.
 
### Fungsi `hari_kerja`
```python
def hari_kerja(tahun, bulan, hari):
```
- **Deskripsi**: Memeriksa apakah suatu hari adalah hari kerja (Senin-Jumat).
- **Parameter**:
  - `tahun` (*int*): tahun.
  - `bulan`: bulan (bisa dalam bentuk string/nama atau angka).
  - `hari` (*int*): tanggal.
- **Langkah-langkah**:
  - Memvalidasi apakah tanggal yang diberikan valid menggunakan `validasi_tanggal`.
  - Mengonversi bulan ke angka jika perlu.
  - Menggunakan fungsi `calendar.weekday` untuk mendapatkan indeks hari (0 untuk Senin, 6 untuk Minggu).
  - Memeriksa apakah indeks hari kurang dari 5 (Senin hingga Jumat) dan mengembalikan hasilnya.
- **Output**:
  - Menampilkan apakah hari tersebut adalah hari kerja atau libur.

### Fungsi `akhir_pekan`
```python
def akhir_pekan(tahun, bulan, hari):
```
- **Deskripsi**: Fungsi ini mengecek apakah hari tertentu adalah akhir pekan (Sabtu-Minggu).
- **Parameter**:
  - `tahun` (*int*): tahun.
  - `bulan`: bulan (bisa dalam bentuk string/nama atau angka).
  - `hari` (*int*): tanggal.
- **Langkah-langkah**:
  - Memvalidasi tanggal.
  - Mengonversi bulan ke angka jika perlu.
  - Memanggil fungsi `hari_kerja` untuk memeriksa apakah hari tersebut adalah hari kerja.
  - Jika bukan hari kerja, maka hasilnya adalah akhir pekan.
- **Output**:
  - Menampilkan apakah hari tersebut adalah akhir pekan atau hari kerja.

### Fungsi `nama_hari`
```python
def nama_hari(tahun, bulan, hari):
```
- **Deskripsi**: Fungsi ini mengembalikan nama hari dalam Bahasa Indonesia untuk suatu tanggal.
- **Parameter**:
  - `tahun` (*int*): tahun.
  - `bulan`: bulan (bisa dalam bentuk string/nama atau angka).
  - `hari` (*int*): tanggal.
- **Langkah-langkah**:
  - Memvalidasi tanggal.
  - Mengonversi bulan ke angka jika perlu.
  - Menggunakan fungsi `calendar.weekday` untuk mendapatkan indeks hari.
  - Mencari nama hari dari List `hari_dalam_indonesia` berdasarkan indeks.
- **Output**:
  - Menampilkan dan mengembalikan nama hari.

### Fungsi `konversi_bulan_int`
```python
def konversi_bulan_int(bulan):
```
- **Deskripsi**: Fungsi ini mengonversi nama bulan dari string menjadi angka, atau mengembalikan angka langsung jika inputnya sudah dalam bentuk integer.
- **Parameter**:
  - `bulan`: bulan (bisa dalam bentuk string/nama atau angka).
- **Langkah-langkah**:
  - Jika bulan sudah berupa integer, langsung dikembalikan.
  - Jika bulan berupa string, fungsi akan mengubah huruf pertamanya menjadi huruf kapital dan mencocokkan nama bulan dengan yang ada di dictionary.
  - Jika nama bulan tidak ditemukan, akan muncul error.
  - Jika tipe data selain string atau integer diberikan, fungsi akan mengembalikan error tipe.
 
### Fungsi `bulan_dalam_indonesia_inverse`
```python
def bulan_dalam_indonesia_inverse(bulan_int):
```
- **Deskripsi**: Fungsi ini mencari nama bulan berdasarkan angka bulannya.
- **Parameter**:
  - `bulan_int`: bulan (bisa dalam bentuk string/nama atau angka).
- **Langkah-langkah**:
  - Melakukan iterasi melalui dictionary `bulan_dalam_indonesia`.
  - Jika ditemukan bulan yang sesuai dengan angka yang diberikan, fungsi mengembalikan nama bulannya.
  - Jika tidak ditemukan, fungsi mengembalikan `None`.
