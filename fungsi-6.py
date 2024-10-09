import calendar

# Daftar nama hari dalam Bahasa Indonesia
hari_dalam_indonesia = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

def is_weekday(year, month, day):
    """Mengembalikan True jika hari adalah hari kerja (Senin-Jumat), False jika tidak."""
    weekday = calendar.weekday(year, month, day)
    is_weekday_result = weekday < 5
    print(f"{day}/{month}/{year} adalah {'hari kerja' if is_weekday_result else 'hari libur'}")
    return is_weekday_result

def is_weekend(year, month, day):
    """Mengembalikan True jika hari adalah akhir pekan (Sabtu-Minggu), False jika tidak."""
    is_weekend_result = not is_weekday(year, month, day)
    print(f"{day}/{month}/{year} adalah {'akhir pekan' if is_weekend_result else 'hari kerja'}")
    return is_weekend_result

def get_day_name(year, month, day):
    """Mengembalikan nama hari dalam Bahasa Indonesia."""
    weekday = calendar.weekday(year, month, day)
    day_name = hari_dalam_indonesia[weekday]
    print(f"Nama hari: {day_name}")
    return day_name