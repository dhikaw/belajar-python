n = int(input("Masukkan Angka n : "))
hasil = n % 2

def ganjilgenap(hasil):
    if hasil == 1:
        print("Bilangan Ganjil")
    else:
        print("Bilangan Genap")

ganjilgenap(hasil)