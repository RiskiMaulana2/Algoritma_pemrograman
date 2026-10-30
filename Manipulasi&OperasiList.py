listData=["riski",1,2]
listData.remove("riski")
listData.__len__
print(listData)


# --- Program 9.1: Pembuatan List ---
data_angka = [1, 5, 2, 3]
data_string = ["ucup", "adit", "siti"]
data_boolean = [True, False, True, True]
data_campuran = [1, "bakwan", 2, "cireng", "ucup", True, "adit", False]
print(data_angka)
print(data_string)
print(data_boolean)
print(data_campuran)
# --- 1. Menggunakan range(start, stop, step) ---
data_range = range(0, 10, 2)  # Membuat range dari 0 sampai <10 dengan kelipatan 2
print("Data range:", data_range)

data_list = list(data_range)  # Mengubah range menjadi bentuk list
print("Hasil konversi range ke list:", data_list)


# --- 2. Membuat list dengan for loop (List Comprehension) ---
# Mengalikan setiap elemen dengan 2
list_for = [i * 2 for i in range(0, 10)]
print("List comprehension biasa:", list_for)


# --- 3. Membuat list dengan for loop dan kondisi if ---
# Contoh A: Menyaring elemen dengan kondisi if (misal: i != 5)
list_for_if_1 = [i for i in range(0, 10) if i != 5]
print("List dengan kondisi i != 5:", list_for_if_1)

# Contoh B: Menyaring angka genap (i % 2 == 0)
list_for_if_2 = [i for i in range(0, 10) if i % 2 == 0]
print("List angka genap:", list_for_if_2)

# Contoh C: Menyaring angka ganjil (i % 2 != 0)
list_for_if_3 = [i for i in range(0, 10) if i % 2 != 0]
print("List angka ganjil:", list_for_if_3)


# --- Program 9.2: Manipulasi List ---
data = ["Ucup", "Adit", "Dudung"]
data.insert(1, "Asep")  # Menambah di posisi tertentu
data.append("Ririn")  # Menambah di akhir
data_baru = ["Luffy", "Zoro", "Nami"]
data.extend(data_baru)  # Menggabungkan list
data[2] = "jarwo"  # Mengubah data
data.remove("Ucup")  # Menghapus berdasarkan nilai
data.pop()  # Menghapus elemen terakhir
print(data)

# --- Program 9.3: Operasi List (Count, Index, Sort, Reverse) ---
data_angka_ops = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]
jumlah_4 = data_angka_ops.count(4)
data_angka_ops.sort()
data_angka_ops.reverse()
print(data_angka_ops)

# --- Program 9.4: Nested List ---
peserta_0 = ["Rendi", 25, "Laki-laki"]
peserta_1 = ["Joni", 10, "Laki-laki"]
peserta_2 = ["Eka", 50, "Wanita"]
list_peserta = [peserta_0, peserta_1, peserta_2]

for peserta in list_peserta:
  print(f"Nama\t: {peserta[0]}")
  print(f"Umur\t: {peserta[1]}")
  print(f"Gender\t: {peserta[2]}\n")


#Latihan 1
kendaraan = ["motor", "mobil", "sepeda", "bus"]

# a. Tambahkan 'truk' di akhir list
kendaraan.append("truk")

# b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, "becak")

# c. Hapus data yang berada paling belakang
kendaraan.pop()

# d. Ubah elemen 'sepeda' menjadi 'skuter'
kendaraan[2] = "skuter"

# e. Tampilkan informasi jumlah total data
print(f"Total data kendaraan: {len(kendaraan)}")
print(f"Hasil akhir list: {kendaraan}")

#Latihan 2
# Diberikan list skor ujian berikut:
angka = [75, 80, 90, 75, 85, 100, 65]

# a. Cari tahu di indeks ke berapa skor 100 berada.
index_100 = angka.index(100)
print(f"a. Skor 100 berada di indeks ke: {index_100}")

# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75.
jumlah_75 = angka.count(75)
print(f"b. Jumlah siswa yang mendapatkan skor 75 adalah: {jumlah_75}")

# c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar.
angka.sort()
print(f"c. Urutkan dari terkecil hingga terbesar: {angka}")

# d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil.
angka.reverse()
print(f"d. Urutan dari terbesar ke terkecil: {angka}")

#Latihan 3
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

# Menggabungkan menggunakan fungsi extend
menu_utama.extend(menu_tambahan)
print(f"Data gabungan menu: {menu_utama}")

#Latihan 4
# Diberikan data nested list berupa informasi nama barang dan harganya
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik
harga_pensil = data_barang[1][1]
print(f"a. Harga dari Pensil adalah: {harga_pensil}")

# b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format yang diminta
print("\nb. Daftar Nama dan Harga Barang:")
for barang in data_barang:
  print(f"Nama: {barang[0]}, Harga: {barang[1]}")