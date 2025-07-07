# Buka file
with open("data.txt", "r") as file:
    # Baca semua baris jadi list
    baris = file.readlines()

# Lewati baris pertama (header)
for data in baris[1:]:
    nama, umur = data.strip().split(",")
    umur = int(umur)  # Konversi ke int

    if umur > 20:
        print(f"{nama} ({umur} tahun)")
