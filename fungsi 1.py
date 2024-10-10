import calendar

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

def tampilkan_kalender():
    while True:
        try:
            
            if inputan_bulan.isdigit():
                bulan = int(inputan_bulan)
                if 1 <= bulan <= 12:
                    print(calendar.month(tahun, bulan))
                    break
                else:
                    print("Bulan tidak valid. Silahkan masukkan angka antara 1 dan 12.")
            elif inputan_bulan in nama_bulan:
                bulan = nama_bulan[inputan_bulan]
                print(calendar.month(tahun, bulan))
                break
            else:
                print("Nama bulan tidak valid. Silahkan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silahkan coba lagi.")


tampilkan_kalender()
