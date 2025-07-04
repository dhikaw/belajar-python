x = int(input("Masukkan angka : "))
y = int(input("Masukkan angka : "))
operasi = str(input("Masukkan operasi : "))

if operasi == "+":
    print(x + y)
elif operasi == "-":
    print(x - y)
elif operasi == "x":
    print(x * y)
elif operasi == "/": 
    print(x / y)
else:
    print("Tidak Valid")

print()