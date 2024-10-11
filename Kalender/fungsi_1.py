import calendar

nama_bulan = {
    "januari": 1,
    "january": 1,
    "februari": 2,
    "february": 2,
    "march": 3,
    "maret": 3,
    "april": 4,
    "mei": 5,
    "may": 5,
    "juni": 6,
    "june": 6,
    "juli": 7,
    "july": 7,
    "agustus": 8,
    "august": 8,
    "september": 9,
    "oktober": 10,
    "october": 10,
    "november": 11,
    "desember": 12,
    "december": 12
}

def dapatkan_kalender(tahun, bulan):
    return calendar.month(tahun, bulan)

def tampilkan_kalender(tahun, inputan_bulan):
    try:
        if isinstance(inputan_bulan, int):
            bulan = inputan_bulan
            if 1 <= bulan <= 12:
                return dapatkan_kalender(tahun, bulan)
            else:
                raise ValueError("Bulan harus antara 1 dan 12.")
        
        elif isinstance(inputan_bulan, str):
            bulan = nama_bulan[inputan_bulan.lower()]  
            return dapatkan_kalender(tahun, bulan)
        
        else:
            raise TypeError("Input bulan harus berupa angka atau nama bulan.")

    except KeyError:
        return f"Nama bulan '{inputan_bulan}' tidak valid. Masukkan nama bulan yang benar."
    except ValueError as ve:
        return str(ve)
    except TypeError as te:
        return str(te)
