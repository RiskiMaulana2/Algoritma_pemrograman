## --- Nested IF ---

# if kondisi_utama:
#     if kondisi_lanjutan:
#         # Aksi jika kedua kondisi bernilai True
#     else:
#         # Aksi jika kondisi_utama True, tetapi kondisi_lanjutan False
# else:
#     # Aksi jika kondisi_utama False

status_akun = "aktif"  # pilihan: "aktif", "terblokir"
saldo = 750000
nominal_tarik = 500000

if status_akun == "aktif":
    if nominal_tarik <= saldo:
        if nominal_tarik >= 50000:
            saldo = saldo - nominal_tarik
            print(f"Penarikan berhasil: Rp{nominal_tarik:,}")
            print(f"Sisa saldo: Rp{saldo:,}")
        else:
            print("Gagal: Penarikan minimal Rp50,000.")
    else:
        print("Gagal: Saldo tidak mencukupi.")
else:
    print("Akses ditolak: Akun sedang terblokir.")

## --- Nested While ---

i = 1
while i <= 2:
    j = 1
    while j <= 3:
        print("Teknologi Informasi")
        j += 1
    print("\n")  # Mencetak baris baru (\n) saat inner loop selesai
    i += 1

## --- Nested While ---

i = 1
N = 1

while i <= 2:
    j = 1
    while j <= 3:
        print(N)
        N = N + 2
        j += 1
    i += 1

## --- Nested FOR ---

for i in range(1, 3):         # Outer loop (baris 1 s.d. 2)
    for j in range(1, 4):     # Inner loop (kolom 1 s.d. 3)
        print(f"[{i},{j}]", end=" ")
    print()  # Pindah baris

## --- For in While ---

# for_in_while.py
sesi = 1

while sesi <= 2:  # Outer while: mengontrol nomor sesi
    print(f"Sesi ke-{sesi}:")
    
    # Inner for: mencetak nomor antrean pada sesi tersebut
    for antrean in range(1, 4):
        print(f"  Melayani pasien nomor: {antrean}")
        
    sesi += 1
    print("---")