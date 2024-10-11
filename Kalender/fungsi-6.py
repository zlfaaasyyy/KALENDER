import calendar

# Daftar nama hari dalam Bahasa Indonesia
hari_dalam_indonesia = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

# Dictionary untuk mengonversi nama bulan (bahasa Indonesia) menjadi angka
bulan_dalam_indonesia = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4,
    "Mei": 5, "Juni": 6, "Juli": 7, "Agustus": 8,
    "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}

def validasi_tanggal(tahun, bulan, hari):
    bulan = konversi_bulan_int(bulan)
    jumlah_hari = calendar.monthrange(tahun, bulan)[1]
    if 1 <= hari <= jumlah_hari:
        return True
    else:
        print(f"Tanggal {hari} tidak valid untuk bulan {bulan_dalam_indonesia_inverse(bulan)} di tahun {tahun}.")
        return False

def hari_kerja(tahun, bulan, hari):
    if not validasi_tanggal(tahun, bulan, hari):
        return None
    bulan = konversi_bulan_int(bulan)
    indeks_hari = calendar.weekday(tahun, bulan, hari)
    hari_kerja_result = indeks_hari < 5
    print(f"{hari}/{bulan}/{tahun} adalah {'hari kerja' if hari_kerja_result else 'hari libur'}")
    return hari_kerja_result

def akhir_pekan(tahun, bulan, hari):
    if not validasi_tanggal(tahun, bulan, hari):
        return None
    bulan = konversi_bulan_int(bulan)
    akhir_pekan_result = not hari_kerja(tahun, bulan, hari)
    print(f"{hari}/{bulan}/{tahun} adalah {'akhir pekan' if akhir_pekan_result else 'hari kerja'}")
    return akhir_pekan_result

def nama_hari(tahun, bulan, hari):
    if not validasi_tanggal(tahun, bulan, hari):
        return None
    bulan = konversi_bulan_int(bulan)
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

def bulan_dalam_indonesia_inverse(bulan_int):
    for nama_bulan, angka_bulan in bulan_dalam_indonesia.items():
        if angka_bulan == bulan_int:
            return nama_bulan
