# Date and time

import datetime as dt #as itu sebagai dan dt itu merubah "datetime" ke "dt" menggunakan as

tanggal = int(input("tanggal \t:"))
bulan   = int(input("bulan \t\t:"))
tahun   = int(input("tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah :{tanggal_lahir}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
print(f"ini adalah umur hari {umur_hari}")
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah :{umur_tahun} tahun, {umur_bulan_sisa} bulan,")