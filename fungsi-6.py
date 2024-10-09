import calendar

hari_dalam_indonesia = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

def is_weekday(year, month, day):
    """Mengembalikan True jika hari adalah hari kerja (Senin-Jumat), False jika tidak."""
    weekday = calendar.weekday(year, month, day)
    return weekday < 5

def is_weekend(year, month, day):
    """Mengembalikan True jika hari adalah akhir pekan (Sabtu-Minggu), False jika tidak."""
    return not is_weekday(year, month, day)

def get_day_name(year, month, day):
    """Mengembalikan nama hari dalam Bahasa Indonesia."""
    weekday = calendar.weekday(year, month, day)
    return hari_dalam_indonesia[weekday]

day = int(input("Masukkan Tanggal (angka): "))
month = int(input("Masukkan Bulan (angka): "))
year = int(input("Masukkan Tahun (angka): "))

if is_weekday(year, month, day):
    print(f"{day}/{month}/{year} adalah hari kerja ({get_day_name(year, month, day)})")
else:
    print(f"{day}/{month}/{year} adalah hari libur ({get_day_name(year, month, day)})")