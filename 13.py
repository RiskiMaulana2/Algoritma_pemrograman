bilangan = 0

def ubah_bilangan(data):
    bilangan = data
    return bilangan

x = ubah_bilangan(10)
print(x)                                                 

#[] => list
#{} => dictionary             

def rekap_denda(data):
    hasil = {}
    tarif_denda = 2000
    
    for item in data:
        nama = item["nama"]
        denda = item["hari_terlambat"] * tarif_denda
        
        if nama not in hasil:
            hasil[nama] = {"total_buku": 0, "total_denda": 0}    
        hasil[nama]["total_buku"] += 1
        hasil[nama]["total_denda"] += denda
    return hasil

# Pengujian
peminjaman = [
    {"nama": "Rina", "judul": "Algoritma Dasar", "hari_terlambat": 2},
    {"nama": "Bima", "judul": "Struktur Data", "hari_terlambat": 0},
    {"nama": "Rina", "judul": "Basis Data", "hari_terlambat": 4},
    {"nama": "Sari", "judul": "Jaringan Komputer", "hari_terlambat": 1},
    {"nama": "Bima", "judul": "Pemrograman Web", "hari_terlambat": 3}
]
print(rekap_denda(peminjaman))

def rekap_lembur(data):
    hasil = {}
    upah_lembur = 25000

    for item in data :
        nama = item["nama"]
        jam_kerja = item["jam_kerja"]

        jam_lembur = 0

        if jam_kerja >8:
              jam_lembur = jam_kerja - 8
        else:
             jam_lembur = 0
        lembur = jam_lembur*upah_lembur 

        if nama not in hasil:
            hasil[nama] = {"total_jam_kerja": 0, "total_uang_lembur": 0}    
            hasil[nama]["total_jam_kerja"]+= jam_kerja
            hasil[nama]["total_uang_lembur"]+= lembur
    return hasil
    
absensi = [ {"nama": "Dina", "jam_kerja": 9},
            {"nama": "Riko", "jam_kerja": 8},
            {"nama": "Dina", "jam_kerja": 10},
            {"nama": "Santi", "jam_kerja": 7},
            {"nama": "Riko", "jam_kerja": 11}  ] 

for nama, ringkasan in rekap_lembur(absensi).items():
    print(f"{nama}: {ringkasan}")