import datetime as dt

nama1 = {
    'nama' : 'fakhri',
    'umur' : 18,
    'panggilan' : False,
    'lahir' : dt.datetime(2025,1,6)
}


nama2= {
    'nama' : 'bayo',
    'umur' : 18,
    'panggilan' : True,
    'lahir' : dt.datetime(2025,1,6)
}


nama3 = {
    'nama' : 'bale',
    'umur' : 15,
    'panggilan' : False,
    'lahir' : dt.datetime(2022,10,5)
}

data_nama = {
    'nama001' : nama1,
    'nama002' : nama2,
    'nama003' : nama3
}
print(f"{'key':<6} {'nama':<17} {'umur':<3} {'panggilan':^9} {'lahir':<10}") # "<" ljust
print("-"*50)


for nama in data_nama:
    KEY = nama
    
    NAMA = data_nama[KEY] ['nama']
    UMUR = data_nama[KEY] ['umur']
    PANGGILAN = data_nama[KEY] ['panggilan']
    LAHIR = data_nama[KEY] ['lahir'].strftime("%x")
    
    print(f"{KEY:<6} {NAMA:<17} {UMUR:<3} {PANGGILAN:^9} {LAHIR:<10}") # "<" ljust