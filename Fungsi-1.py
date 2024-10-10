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