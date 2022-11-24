print ("~~~~~~~~~~/('V')\~~~~~~~~~~")
print ("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print ("~~~~~~~~~~/('V')\~~~~~~~~~~")
print ()
print ("pilihlah salah satu bangun ruang yang ingin dihitung volumenya:")
print ("1. Limas")
print ("2. Bola")
print ("3. Prisma")
print ("4. Kerucut")
print ()
pilihan = int(input("masukkan pilihan Anda: "))

if pilihan == 1:
    panjang = int(input("Masukkan panjang sisi alas limas: "))
    tinggi = int(input("Masukkan tinggi limas: "))

    rumuslimas = (panjang*panjang*tinggi/3)

    print ("Volume limas tersebut adalah", rumuslimas)

elif pilihan == 2:
    jari = int(input("Masukkan panjang jari-jari bola: "))

    rumusbola = ((4/3)*3.14*(jari**3))
               
    print ("Volume bola tersebut adalah", rumusbola)

elif pilihan == 3:
    print("Pilihlah salah satu dari pilhan di bawah: ")
    print ("1. Prisma Segitiga")
    print ("2. Prisma Segiempat")
    print ("3. Prisma Segilima")

    pilihank = int(input("Tentukan pilihan Anda: "))

    if pilihank == 1:
        panjangp = int(input("Masukkan panjang sisi alas prisma: "))
        tinggiap = int(input("Masukkan tinggi alas prisma: "))
        tinggips = int(input("Masukkan tinggi prisma segitiga: "))

        rumusprismasegitiga = ((tinggiap*panjangp/2)*tinggips)
        print ("Volume prisma segitiga tersebut adalah", rumusprismasegitiga)

    elif pilihank == 2:
        panjangp = int(input("Masukkan panjang sisi alas prisma: "))
        tinggiap = int(input("Masukkan tinggi alas prisma: "))
        tinggips = int(input("Masukkan tinggi prisma segiempat: "))

        rumusprismasegiempat = ((panjangp*tinggiap)*tinggips)
        print ("Volume prisma segiempat tersebut adalah", rumusprismasegiempat)

    elif pilihank == 3:
        panjangp = int(input("Masukkan panjang sisi alas prisma: "))
        tinggiap = int(input("Masukkan tinggi alas prisma: "))
        tinggips = int(input("Masukkan tinggi prisma segilima: "))

        rumusprismasegilima = (((5*panjangp*tinggiap)/2)*tinggips)
        print ("Volume prisma segilima tersebut adalah", rumusprismasegilima)
                
elif pilihan == 4:
    jarik = int(input("Masukkan jari-jari kerucut: "))
    tinggik = int(input("Masukkan tinggi kerucut: "))

    rumuskerucut = ((jarik*jarik*tinggik*3.14)/3)
    print ("Volume kerucut tersebut adalah", rumuskerucut)
    
