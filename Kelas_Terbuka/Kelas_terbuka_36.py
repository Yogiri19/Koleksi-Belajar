# program list buku


list_buku = []
while True:
    print("\nmasukan data buku")
    judul = input("judul buku \t:")
    penulis = input ("nama penulis \t:")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n", "="*10, "Data Buku", "="*10) 
    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
        
        print("\n\n", "="*20)
        
    print("PROGRAM SELESAI")\
        

        
        