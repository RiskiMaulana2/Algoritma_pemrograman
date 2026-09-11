# OPERASI LOGIKA ATAU BOOLEAN
# not,or,and,xor
print("===NOT===")
a = True
b = not a
print("data a =",a)
print("-----------NOT")
print("data b =",b)

#OR (akan bernilai true jika minimal 1 true)
print("===OR===")
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)

#and (akan bernilai true jika keduanya true)
a = False
b = False
hasil = a and b
print(hasil)
a = True
b = False
hasil = a and b
print(hasil)
a = True 
b = True
hasil = a and b
print(hasil)

#xor (akan true jika salah satu true, sisanya false)
a = False
b = False
hasil = a ^ b
print(hasil)
a = True
b = False
hasil = a ^ b
print(hasil)
a = True 
b = True
hasil = a ^ b
print(hasil)

#Latihan logika dan komperasi
#program untuk mengecek bilangan < 3 / >10
#++++++++++ 3 ---------- 10 +++++++++++

angka = int(input("masukkan angka: "))
iskurangdari = angka < 3
islebihdari = angka > 10
hasil = iskurangdari or islebihdari
print(hasil)
angka = int(input("masukkan angka: "))
iskurangdari = angka < 10
islebihdari = angka > 3
hasil = iskurangdari and islebihdari
print(hasil)

#if dan else statement
#1. if nya
#2. kondisinya(syarat)
#3. aksi
#program Riski BISA
#program if inline
nama = input("masukkan nama: ")
if nama == "riski" : print("bisa")
#program if indentation
if nama == "riski":
    print("HEBAT!!")
    print("BISA!!")
print("akhir dari program")
#else statement
if nama == "riski":
    print("HEBAT!!")
else:
    print("BISA!!!")

#ELIF = else if statement
nama = input("masukkan nama: ")
# if kondisi: 
        #aksi true 
# elif kondisi: 
        # aksi true 
# elif kondisi: 
        # aksi true 
# else: 
        #aksi
if nama == "riski":
    print("bisa")
elif nama == "maulana":
    print("hebat")
elif nama == "achmad":
    print("goodgame")
else:
    print("wellplayed")
print("end")

#LATIHAN
usia = int(input("masukkan usia anda: "))
# iskurangdari = angka < 12
# islebihdari = angka > 0
# hasil = iskurangdari and islebihdari
# print(hasil)
if usia >= 0 and usia <=12:
    print("anak-anak")
elif usia >=13 and usia <=17:
    print("remaja")
elif usia >= 18 and usia <=59:
    print("dewasa")
else:
    print("lansia")
