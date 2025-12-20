panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))
volume = panjang * lebar * tinggi
print("Volume Balok =", volume, "m³")

#excersise 2
import math

r = float(input("Masukkan jari-jari: "))
volume = (4/3) * math.pi * r**3
print("Volume Bola =", volume, "m³")

#excersise 3
import math

r = float(input("Masukkan jari-jari: "))
t = float(input("Masukkan tinggi: "))

volume = math.pi * r**2 * t
print("Volume Tabung =", volume, "m³")

#excersise 4
a = float(input("Masukkan nilai A: "))
b = float(input("Masukkan nilai B: "))
c = float(input("Masukkan nilai C: "))

diskriminan = b**2 - 4*a*c
print("Nilai Diskriminan =", diskriminan)

#excersise 5
import math

latA = math.radians(float(input("Latitude Titik A: ")))
lonA = math.radians(float(input("Longitude Titik A: ")))
latB = math.radians(float(input("Latitude Titik B: ")))
lonB = math.radians(float(input("Longitude Titik B: ")))

dlat = latB - latA
dlon = lonB - lonA

a = math.sin(dlat/2)**2 + math.cos(latA) * math.cos(latB) * math.sin(dlon/2)**2
c = 2 * math.asin(math.sqrt(a))

jarak = 6371 * c
print("Jarak antara dua titik =", jarak, "km")


