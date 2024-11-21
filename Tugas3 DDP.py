 # MENULISAKAN PROFIL PRIBADI
Nama = "Khaila Nazwa"
Nim = "0110124149"
Kelas = "SI06"
No_Tlp = "085862949634"
Alamat = """ Jl. Curug Dengdeng RT.01 RW02
           kelurahan.Caringin Kecamatan. Caringin 
           Kabupaten. Bogor """
print("nama:",Nama)
print("nim:",Nim)
print("no_tlpn:",No_Tlp)
print("alamat:",Alamat)
print("==========================================================")

# MENULISAKAN PROFIL TEMAN
Nama = "Zhahara N Sukirman"
Nim = "0110124206"
Kelas = "SI04"
No_Tlp = "089531007588"
Alamat = """ Lingkungan Cipayung,
        Rt/Rw 04/01 Kelurahan Abadijaya,
        Kecamatan Sukmajaya Kota Depok """
print("nama:",Nama)
print("Kelas",Kelas)
print("nim:",Nim)
print("no_tlpn:",No_Tlp)
print("alamat:",Alamat)
print("=========================================================")

# MENCARI NILAI BERAT BADAN IDEAL
TB= int(input("masukan tinggi badan:"))
bb_ideal= (TB - 100) -(TB - 100) * 0,15
print("Berat Badan Saya :",bb_ideal)
print("=========================================================")

# MENGHITUNG CELCIUS KE  FAHREINHEIT 
celcius= int(input("masukan nilai celcius:"))
Rumus= (9/5 * celcius) + 32
print("hasil dari celcius ke fahreinheit :",Rumus)
print("=============================================================")

# MENCARI LUAS DAN KELILING TABUNG
phi = 22/7
r = int(input("Masukan jari-jari tabung: "))
t = int(input("Masukan tinggi tabung: "))

luas = 2 * phi * r * (r + t)
keliling = 2 * phi * r

print("Hasil dari luas tabung yakni: ", luas)
print("Hasil dari keliling tabung yakni: ", keliling)

