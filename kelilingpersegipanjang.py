l = int(input("Masukkan Luas : "))
p = int(input("Masukkan Panjang : "))

def luas(p,l):
    print("Luas :", p*l)

def keliling(p,l):
    print("Keliling :", 2*(p+l))

luas(p,l)
keliling(p,l)