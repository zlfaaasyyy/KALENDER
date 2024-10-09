import calendar 

tahun = int(input("Masukkan tahun: "))
bulan_awal = int(input("Masukkan bulan awal: "))
bulan_akhir = int(input("Masukkan bulan akhir: "))

for bulan in range(bulan_awal, bulan_akhir + 1):
    print(calendar.month(tahun,bulan))