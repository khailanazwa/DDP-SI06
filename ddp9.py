# Membuat sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke fahrenheit

def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)

# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulau. Fungsi ini harua mengembalikan true jika bilangan tersebut genap, dan false jika bilangan tersebut ganjil

def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

# Butlah fungsi untuk melihat keterangan lulus atau tidak

def skor(nilai):
    if nilai >= 70:
        print('lulus')
    else:
        print('gagal')

skor(80)
scor(60)

# Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens

def bil_ganjil(ganjil):
    for i in range(1, ganjil+1, 2):
        print(i, end='')
    bil_ganjil(20)