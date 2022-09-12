import time

## Fungsi Iteratif
def fungsiDeretAjaib(angka):
    if angka < 6:
        return angka
    else:
        return fungsiDeretAjaib(angka-2) + fungsiDeretAjaib(angka//2)
    
for i in range(1,100):
    hasilIteratif = fungsiDeretAjaib(7)

start = time.time()
hasil = hasilIteratif
end = time.time()

print("Hasil dari Fungsi iteratif : ")
print("Hasil :",hasil)
print("Duration :",end-start)
print("")

## Fungsi Rekursif
import time
def deret_ajaib(angkaAwal):
    if angkaAwal <= 5:
        return angkaAwal
    else:
        return deret_ajaib(angkaAwal-3) * deret_ajaib(angkaAwal/2)

angkaAwal = 6
start = time.time()
hasil = deret_ajaib(angkaAwal)
end = time.time()

print("Hasil dari Fungsi Rekursif : ")
print("Hasil :",hasil)
print("Duration :",end-start)