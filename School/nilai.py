print (">>>>>>==========================")
td = int(input("Tanda tangan dosen di nilai :"))
tm = int(input("Tanda tangan mahasiswa senior yang menjadi panitia dinilai :"))
tkm = int(input("Tanda tangan karyawan serta mahasiswa senior lain dinilai :"))
print (">>>>>>==========================")
nilai = (td + tm + tkm ) * 10

if nilai >= 80:
    print("Lulus")
elif nilai >= 60:
    print("Hukuman ringan")
else:
    print("Tugas berat")
    
