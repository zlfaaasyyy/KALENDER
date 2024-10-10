import calendar

# Daftar nama hari dalam Bahasa Indonesia
hari_dalam_indonesia = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

# Dictionary untuk mengonversi nama bulan (bahasa Indonesia) menjadi angka
bulan_dalam_indonesia = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4,
    "Mei": 5, "Juni": 6, "Juli": 7, "Agustus": 8,
    "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}

def hari_kerja(tahun, bulan, hari):
    bulan = konversi_bulan_int(bulan)
    # menggunakan calendar.weekday untuk mendapatkan indeks hari (0 untuk Senin, dst)
    indeks_hari = calendar.weekday(tahun, bulan, hari)
    hari_kerja_result = indeks_hari < 5  # Senin-Jumat
    print(f"{hari}/{bulan}/{tahun} adalah {'hari kerja' if hari_kerja_result else 'hari libur'}")
    return hari_kerja_result

def akhir_pekan(tahun, bulan, hari):
    bulan = konversi_bulan_int(bulan)
    akhir_pekan_result = not hari_kerja(tahun, bulan, hari)  # Jika bukan hari kerja
    print(f"{hari}/{bulan}/{tahun} adalah {'akhir pekan' if akhir_pekan_result else 'hari kerja'}")
    return akhir_pekan_result

def nama_hari(tahun, bulan, hari):
    bulan = konversi_bulan_int(bulan)
    # Dapatkan indeks hari (0=Senin, 1=Selasa, dst.)
    indeks_hari = calendar.weekday(tahun, bulan, hari)
    nama_hari = hari_dalam_indonesia[indeks_hari]
    print(f"Nama hari: {nama_hari}")
    return nama_hari

def konversi_bulan_int(bulan):
    if isinstance(bulan, int):
        return bulan
    elif isinstance(bulan, str):
        bulan = bulan.capitalize()
        if bulan in bulan_dalam_indonesia:
            return bulan_dalam_indonesia[bulan]
        else:
            raise ValueError("Nama bulan tidak valid.")
    else:
        raise TypeError("Bulan harus berupa nama atau angka.")