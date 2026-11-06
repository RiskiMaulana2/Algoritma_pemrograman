#program 10.1
#LIST
#Menggunakan Kurung Siku []
data_list = [10,2,4,3,2]
print(data_list)

#TUPLES
data_tuples = (7,8,10,11)
print(data_tuples)
print(data_tuples[1])

#tidak dapat menambahkan data menggunakan
#data_tuples[1] = "riski"
#data_tuples.append(1)

#SETS (HIMPUNAN)
data_sets = {3,4,5,3,4,8}
print(data_sets)
#print(data_sets[0]) #not true

#program 10.2
##DICTIONARY
data_list = ["riski","maulana","achmad"]
print(data_list[0])

data_dict = {
    "Nama" : "Riski maulana",
    "umur" : "20",
    "tinggi badan" : "165",
    "berat badan" : "55",
    "hobi" : "sepak bola"}
print(data_dict["Nama"])
print(data_dict["tinggi badan"])
print(data_dict["hobi"])

#program 10.3
## Operasi Dictionary dengan Data Personal
data_dict = {
    "nama": "Budi Santoso",
    "hobi": "Membaca Buku",
    "umur": 20
}

# Panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# Mengecek key exist atau tidak
KEY = "hobi"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# Mengakses value (read) dengan get
print(data_dict["nama"])
print(data_dict.get("nama"))
print(data_dict.get("tinggi", "key tidak ada"))

# Mengupdate data
data_dict["nama"] = "Budi Pratama"
print(data_dict)

data_dict["tinggi_badan"] = 175
print(data_dict)

data_dict.update({"nama": "Budi Santoso"})
print(data_dict)

data_dict.update({"berat_badan": 65}) # akan ditambah jika tidak ada
print(data_dict)

# Menghapus data
del data_dict["berat_badan"]
print(data_dict)

#program 10.4
## Looping Dictionary - Data Mahasiswa Universitas Tidar

# Membuat dictionary dengan data Universitas Tidar
data_mahasiswa = {
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi",
    "fakultas": "Teknik",
    "semester": 4,
    "biaya_ukt": 4500000
}

# 1. Looping biasa (hanya mengambil key)
print("1.Looping Key")
for key in data_mahasiswa:
    print(key)

print("2. Looping Keys menggunakan .keys()")
keys = data_mahasiswa.keys()
print(keys)
for key in data_mahasiswa.keys():
    print(data_mahasiswa.get(key))

print("3. Looping Values menggunakan .values()")
values = data_mahasiswa.values()
print(values)
for value in data_mahasiswa.values():
    print(value)

print("4. Looping Items (Key dan Value) menggunakan .items()")
items = data_mahasiswa.items()
print(items)

# Menampilkan tuple (key, value)
for item in data_mahasiswa.items():
    print(item)

# Menampilkan key dan value dengan format f-string yang rapi
print("Format Output Data Universitas Tidar")
for key, value in data_mahasiswa.items():
    print(f"Key: {key:<12} | Value: {value}")



#Latihan
#1. Tuple 
mahasiswa = (
    "Riski Maulana","2605060052","Teknologi Informasi"
)
print(mahasiswa[1])
print(mahasiswa[2])

#mahasiswa[2] = "Teknologi Informasi"

nilai_angka = {10,4,3,2,4,10,7,5}
print(nilai_angka)

#2.Manipulasi Dictionary
data_mahasiswa = {
    "nim" : "240101",
    "nama" : "budi santoso",
    "prodi" : "Teknologi Informasi"
}
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa.update({"angkatan" : "2026"})
print(data_mahasiswa)

del data_mahasiswa["nim"]
print(data_mahasiswa)

#3. looping pada dictionary
# a. Membuat dictionary 'keranjang'
keranjang = {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}

# Menyiapkan variabel untuk menghitung total belanja
total_belanja = 0

# b. Perulangan untuk menampilkan setiap barang dan harganya
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")
    total_belanja += harga  # Menjumlahkan total belanja

# c. Menampilkan total belanja
print(f"Total belanja: Rp {total_belanja}")