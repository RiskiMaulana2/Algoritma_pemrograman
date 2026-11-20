## --- MEMBUAT FUNGSI ---

def hello_world ():
    # menampilkan hello world
    print("hello world")
    print("Kepada Riski Maulana")
    print("Dan juga kepada Maulana Achmad")

hello_world()

## --- Fungsi dengan argumen ---

## def nama_fungsi(argumen)
#      Badan fungsi

def hello_world(nama):
    #fungsi hello world menerima
    print(f"Selamat datang di Dunia, {nama}")

hello_world("maul")

def tambah(x,y):
    # fungsi tambah
    hasil = x + y
    print(f"{x} + {y} = {hasil}")

tambah(1,8)

def say_hi(list_peserta):
    #fungsi say hi
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Selamat datang {peserta}")

kumpulan_mahasiswa = ["Riski", "Maulana", "Achmad"]

say_hi(kumpulan_mahasiswa)

# template fungsi kembalian
# def nama_fungsi(argumen):
#       badan fungsi
#       return output

# fungsi kuadrat

def kuadrat(input_angka):
    output_kuadrat = input_angka ** 2
    return output_kuadrat

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

def fungsi_tambah(angka_1, angka_2):
    # fungsi return dengan multi input
    return angka_1 + angka_2

a = fungsi_tambah(10, 8)
print(a)

def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")

# Default argument

# def fungsi(argument):
# def fungsi(argument = nilai default):

# contoh 1
def say_hello(nama = "Ojul"):
    print(f"Hello {nama}")

say_hello("Ucup")
say_hello()

# contoh 2
def sapa_dia(nama, pesan = "Apa kabar?"):
    # fungsi dengan satu input biasa, dan satu default arg
    print(f"hai {nama}, {pesan}")

sapa_dia("Nanda","Selamat pagi")
sapa_dia("Budi")

# contoh 3
def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# contoh 4
def faktorial(input_1=1,input_2=2,input_3=3,input_4=4):
    hasil = input_1 * input_2 * input_3 * input_4
    return hasil

print(faktorial())
print(faktorial(input_3 = 10))


import math

# a. Fungsi menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# b. Fungsi menghitung volume persegi panjang (balok)
def volume_persegi_panjang(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# c. Fungsi menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

# d. Fungsi menghitung volume bola
def volume_bola(jari_jari):
    return (4/3) * math.pi * (jari_jari ** 3)


# --- PROGRAM UTAMA (INPUT & OUTPUT) ---

print("=== a. Luas Persegi Panjang ===")
p = float(input("Masukkan panjang : "))
l = float(input("Masukkan lebar   : "))
print(f"Luas persegi panjang = {luas_persegi_panjang(p, l)}\n")

print("=== b. Volume Persegi Panjang (Balok) ===")
p_balok = float(input("Masukkan panjang : "))
l_balok = float(input("Masukkan lebar   : "))
t_balok = float(input("Masukkan tinggi  : "))
print(f"Volume balok = {volume_persegi_panjang(p_balok, l_balok, t_balok)}\n")

print("=== c. Luas Lingkaran ===")
r_lingkaran = float(input("Masukkan jari-jari : "))
print(f"Luas lingkaran = {luas_lingkaran(r_lingkaran):.2f}\n")

print("=== d. Volume Bola ===")
r_bola = float(input("Masukkan jari-jari : "))
print(f"Volume bola = {volume_bola(r_bola):.2f}")
