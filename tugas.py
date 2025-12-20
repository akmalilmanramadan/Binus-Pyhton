angka = int(input("Masukkan sebuah angka: "))

if angka % 2 == 0:
    print("Angka tersebut adalah Genap")
else:
    print("Angka tersebut adalah Ganjil")

#excersise 2
usia = int(input("Masukkan usia: "))

if usia < 0:
    print("Usia tidak boleh negatif")
elif usia <= 1:
    print("Kategori: Baby")
elif usia <= 3:
    print("Kategori: Toddler")
elif usia <= 5:
    print("Kategori: Preschooler")
elif usia <= 12:
    print("Kategori: Child")
elif usia <= 17:
    print("Kategori: Teenager")
elif usia <= 21:
    print("Kategori: Young Adult")
elif usia <= 30:
    print("Kategori: Pre-adult")
elif usia <= 50:
    print("Kategori: Adult")
elif usia <= 70:
    print("Kategori: Pre-elderly")
else:
    print("Kategori: Elderly")

#excersise 3
print("Menu Konversi Suhu")
print("1. Celsius ke Fahrenheit")
print("2. Celsius ke Kelvin")
print("3. Fahrenheit ke Celsius")
print("4. Fahrenheit ke Kelvin")
print("5. Kelvin ke Celsius")
print("6. Kelvin ke Fahrenheit")

pilihan = int(input("Pilih menu (1-6): "))
suhu = float(input("Masukkan nilai suhu: "))

if pilihan == 1:
    hasil = (suhu * 9/5) + 32
    print("Hasil:", hasil, "F")
elif pilihan == 2:
    hasil = suhu + 273.15
    print("Hasil:", hasil, "K")
elif pilihan == 3:
    hasil = (suhu - 32) * 5/9
    print("Hasil:", hasil, "C")
elif pilihan == 4:
    hasil = (suhu - 32) * 5/9 + 273.15
    print("Hasil:", hasil, "K")
elif pilihan == 5:
    hasil = suhu - 273.15
    print("Hasil:", hasil, "C")
elif pilihan == 6:
    hasil = (suhu - 273.15) * 9/5 + 32
    print("Hasil:", hasil, "F")
else:
    print("Pilihan tidak valid")

#excersise 4
a = float(input("Masukkan sisi A: "))
b = float(input("Masukkan sisi B: "))
c = float(input("Masukkan sisi C: "))

# Cek apakah membentuk segitiga
if a + b <= c or a + c <= b or b + c <= a:
    print("Bukan segitiga")
else:
    if a == b == c:
        print("Segitiga Sama Sisi (Equilateral)")
    elif a == b or a == c or b == c:
        print("Segitiga Sama Kaki (Isosceles)")
    else:
        print("Segitiga Sembarang (Scalene)")

    # Bonus: Cek segitiga siku-siku
    sisi = sorted([a, b, c])
    if sisi[0]**2 + sisi[1]**2 == sisi[2]**2:
        print("Segitiga Siku-siku (Right-angled)")
#excersise 5
import math

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

if a == 0:
    print("Ini bukan persamaan kuadrat")
else:
    D = b**2 - 4*a*c
    print(f"Persamaan: {a}x² + {b}x + {c} = 0")
    print("Nilai diskriminan:", D)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("Memiliki akar berbeda")
        print("x1 =", x1)
        print("x2 =", x2)
    elif D == 0:
        x = -b / (2*a)
        print("Memiliki akar kembar")
        print("x =", x)
    else:
        print("Memiliki akar imajiner")
        print("x1 = (-b + √D) / 2a")
        print("x2 = (-b - √D) / 2a")
