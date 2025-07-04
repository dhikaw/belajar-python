n = int(input("Masukkan Angka n : "))
hasil = n % 2
jumlah = 0

if hasil == 1:
    for i in range(1,n+1, 2):
        jumlah += i
else:
    print("Bukan Ganjil")

print(jumlah)