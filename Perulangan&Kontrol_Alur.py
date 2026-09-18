#Perulangan (loop)

angka = 1
print(angka)
angka = angka +1
print(angka)
angka = angka +1
print(angka)

#for kondisi:
#    aksi
#dengan list

angka2 = [0,1,2,3,4,5]
print(angka2)
for i in angka2:
    print(i)

#dengan range 
angka3 = range(6)
print(angka3)
for i in angka3:
    print(i)

#dengan range angka tertentu
angka4 = range(2,6)
print(angka4)
for i in angka4:
    print(i)

#menggunakan string
data_str = "riski"
for huruf in data_str:
    print(huruf)

#while loop
#while kondisi:
#    aksi ini
#    aksi itu
angka = 1
while angka < 5:
    print(f"angka sekarang adalah {angka}") #f digunakan untuk memanggil variabel (angka)
    angka = angka + 1
#angka = 10
#while angka > 5:
   #print("ipin lari ipin!!")

#pass
angka = 1
while angka < 5:
    angka = angka + 1
    if angka == 3:
        pass#ini tidak akan dieksekusi
    print(angka)
    
#continue
angka = 1
print(f"angka sekarang adalah {angka}")
while angka < 5:
    angka = angka + 1
    if angka == 3:
        print("gokil")
        continue
    print(f"angka sekarang adalah {angka}")

#break
angka = 1
print(f"angka sekarang adalah {angka}")
while angka < 5:
    angka = angka + 1
    if angka == 3:
        print("gokil")
        break
    print(f"angka sekarang adalah {angka}")

#latihan membuat segitiga
#menggunakan for
sisi = 4
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

#menggunakan while
sisi = 4
count = 1
while count <= sisi:
    print("*" * count)
    count += 1

    if count > sisi:
        break

# Bilangan ganjil dan genap 1 sampai 50

print("Bilangan ganjil:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i)

print("\nBilangan genap:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Bilangan prima 1 sampai 100

print("Bilangan prima:")

for angka in range(2, 101):
    prima = True

    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break

    if prima:
        print(angka)