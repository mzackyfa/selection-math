print (">>>>>>==========================")
n = int (input("Prestasi yang dicapai oleh pencatur :"))

if n >= 75:
    print("Mendapat Gelar Grandmaster")
elif n >= 50:
    print("Mendapat Gelar Master")
else:
    print("Tidak Mendapat Gelar")
    
print (">>>>>>==========================")

menang = 1
seri = 0.5
kalah = 0
p = input("Menang/Seri/Kalah : ")
if p == "menang":
    print("Mendapat nilai :", menang)
elif p == "seri":
    print("Mendapat nilai:", seri)
else:
    print("Mendapat nilai:", kalah)
print (">>>>>>==========================")
