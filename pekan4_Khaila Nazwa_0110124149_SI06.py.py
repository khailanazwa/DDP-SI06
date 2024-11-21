#Bilangan ganjil dan bilangan genap
angka = int(input("Masukan Bilangan Bulat:"))

if angka % 2 == 0:
 print("Bilangan Genap")
elif angka % 2 != 0:
 print("Bilangan Ganjil")
else:
 print("input tidak valid")


#Nilai Ujian
nilai = int(input("Masukan Nilai ujian:"))

if nilai >= 75:
 print("lulus")
else :
 print("tidak lulus")


#Cek usia dan status
usia = int(input("masukan usia anda:"))

if usia >= 18:
 print("dewasa")
elif usia < 18 and usia > 13:
 print("remaja")
else :
 print("anak anak")


#Status keanggotaan
keanggotaan = input("Masukan jumlah pembelian:")

if keanggotaan == "gold" or keanggotaan == "silver" :
 print("Selamat! anda mendapatkan diskon")
else :
 print ("Silahkan pergi")


#Pembelian diskon
Pembelian = int(input("masukan jumlah pembelian:"))
harga_peritem =1000
total = harga_peritem * Pembelian
hargadiskon = harga_peritem * Pembelian *(10/100)
hargatotal = harga_peritem * Pembelian

if Pembelian > 100 :
 print(f"Anda beruntung! mendapatkan diskon 10% jadi yang harus anda bayar adalah {total}")
else :
 print(f"total yang harus dibayar anda yaitu {total}") 