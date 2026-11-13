#program 11.1 Multi keys & Nesting dictionary
import datetime
mahasiswa1 = {
    "nama" : "Riski Maulana Achmad",
    "nim" : "260052",
    "sks_lulus" : 130,
    "beasiswa" : False,
    "lahir" : datetime.datetime(2006,11,11)
}
mahasiswa2 = {
    'nama': 'M mayqi irfansyah',
    'nim': '260053',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2006, 10, 10)  # tahun, bulan, tanggal
}

mahasiswa3 = {
    'nama': 'vixel perdana',
    'nim': '260054',
    'sks_lulus': 100,
    'beasiswa': True,
    'lahir': datetime.datetime(2007, 5, 10)  # tahun, bulan, tanggal
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-" * 50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")


#program 11.2
import datetime

# Template dictionary mahasiswa
mahasiswa_template = {
    "nama": "nama",
    "nim": "00000000",
    "sks lulus": 0,
    "lahir": datetime.datetime(1111, 1, 11),
}

data_mahasiswa = {}

print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-" * 20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)

# Input data mahasiswa
mahasiswa["nama"] = input("Nama Mahasiswa: ")
mahasiswa["nim"] = input("NIM Mahasiswa: ")
mahasiswa["sks lulus"] = int(input("SKS Lulus: "))

TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))

mahasiswa["lahir"] = datetime.datetime(
    TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR
)
print(mahasiswa)

#program 11.3
import datetime
import os
import random
import string

# Template dict mahasiswa
mahasiswa_template = {
    "nama": "nama",
    "nim": "00000000",
    "sks lulus": 0,
    "lahir": datetime.datetime(1111, 1, 11),
}

data_mahasiswa = {}

while True:
  os.system("cls")  # Gunakan "cls" jika menggunakan Windows
  
  print(f"{'SELAMAT DATANG':^20}")
  print(f"{'DATA MAHASISWA':^20}")
  print("-" * 20)

  mahasiswa = dict.fromkeys(mahasiswa_template.keys())
  mahasiswa["nama"] = input("Nama Mahasiswa: ")
  mahasiswa["nim"] = input("NIM Mahasiswa: ")
  mahasiswa["sks lulus"] = int(input("SKS Lulus: "))

  TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
  BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
  TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))

  mahasiswa["lahir"] = datetime.datetime(
      TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR
  )

  # Membuat key acak sepanjang 6 karakter huruf kapital
  KEY = "".join((random.choice(string.ascii_uppercase) for i in range(6)))
  data_mahasiswa.update({KEY: mahasiswa})

  print(
      f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10}"
      f" {'Tanggal Lahir':<10}"
  )
  print("-" * 60)

  for KEY in data_mahasiswa:
    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks lulus"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
    print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

  print("\n")
  is_done = input("Mau tambah lagi bro (y/n)? ")
  if is_done == "n":
    break

print("\nAkhir dari program, terima kasih")

#latihan
import datetime
import os
import random
import string

# Template dict buku
buku_template = {
    "judul buku": "judul",
    "penulis": "penulis",
    "tahun terbit": 0000,
    "tanggal pinjam": datetime.datetime(1111, 1, 11),
    "status": "TERSEDIA",
}

data_buku = {}

while True:
  # os.system("cls")  # Gunakan "cls" untuk Windows
  os.system("clear")  # Gunakan "clear" untuk Linux/Mac

  print(f"{'SELAMAT DATANG':^25}")
  print(f"{'MANAJEMEN PERPUSTAKAAN':^25}")
  print("-" * 30)

  buku = dict.fromkeys(buku_template.keys())
  buku["judul buku"] = input("Judul Buku        : ")
  buku["penulis"] = input("Penulis Buku      : ")
  buku["tahun terbit"] = int(input("Tahun Terbit      : "))

  print("--- Tanggal Terakhir Pinjam ---")
  T_PINJAM = int(input("Tanggal (1-31)    : "))
  B_PINJAM = int(input("Bulan (1-12)      : "))
  TH_PINJAM = int(input("Tahun (YYYY)      : "))
  buku["tanggal pinjam"] = datetime.datetime(TH_PINJAM, B_PINJAM, T_PINJAM)

  status_pilihan = input("Status Buku (1: Tersedia, 2: Tidak): ")
  if status_pilihan == "1":
    buku["status"] = "TERSEDIA"
  else:
    buku["status"] = "TIDAK"

  # Generate Key Unik untuk Buku (Multi-keys/Nesting key)
  KEY = "".join((random.choice(string.ascii_uppercase) for i in range(5)))
  data_buku.update({KEY: buku})

  # Menampilkan tabel data buku
  print(
      f"\n{'KEYS':<6} {'JUDUL BUKU':<15} {'PENULIS':<12} {'TAHUN':<6}"
      f" {'TGL PINJAM':<12} {'STATUS':<10}"
  )
  print("-" * 70)

  for KEY in data_buku:
    JUDUL = data_buku[KEY]["judul buku"]
    PENULIS = data_buku[KEY]["penulis"]
    TAHUN = data_buku[KEY]["tahun terbit"]
    TGL = data_buku[KEY]["tanggal pinjam"].strftime("%x")
    STATUS = data_buku[KEY]["status"]
    print(f"{KEY:<6} {JUDUL:<15} {PENULIS:<12} {TAHUN:<6} {TGL:<12} {STATUS:<10}")

  print("\n")
  is_done = input("Tambah buku lagi? (y/n): ")
  if is_done.lower() == "n":
    break

print("\nProgram Selesai. Terima kasih!")