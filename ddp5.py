#Buat variabel list dengan value 
namaKendaraan = "Motor scoopy"
jenisKendaraan = "Matic"
ccKendaraan = 125
warnaKendaraan = "Hijau"
rodaKendaraan = 2
hargaKendaraan = 20,48 
tipeKendaraan = "Motor"
merkKendaraan = "Honda"

listKendaraan = [namaKendaraan, jenisKendaraan, ccKendaraan, warnaKendaraan, rodaKendaraan]
print(listKendaraan)

listKendaraan.append((hargaKendaraan, tipeKendaraan))
print(listKendaraan)

listKendaraan.insert( 2, merkKendaraan)
print(listKendaraan)


#Membuat program python match case
pilih = int(input("""Selamat datang diaplikasi menghitung
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran 
3. Untuk menghitung luas segitiga 
                  
masukan pilihan anda"""))

match pilih:
    case 1 :
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukan sisi persegi:"))
        luasPersegi = sisi*sisi
        print("luas persegi yang sisinya",sisi, "adalah", luasPersegi )
        
    case 2 :
        print("Kamu memilih 2 untuk menghitung luas lingkaran")
        jarijari = int(input("masukan jari jari:"))
        luasLingkaran = 3.14 * jarijari * jarijari
        print("luas lingkaran yang jari jarinya",jarijari, "adalah", luasLingkaran )

    case 3 :
        print("Kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("masukan alas segitiga:"))
        tinggi =int(input("masukan tinggi segitinga"))
        luasSegitiga = 0.5 * alas * tinggi
        print("luas segitiga dengan alas ",alas, "dan tinggi",tinggi, "adalah", luasSegitiga )

    case _ :
        print("Anda salah pilih")