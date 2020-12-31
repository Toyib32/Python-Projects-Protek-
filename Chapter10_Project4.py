# lakukan input

cari = input("Masukkan NIM yang mau dicari : ")
file = open("namaDanNIM.txt", "r")
isiFile = file.readlines()

for i in range(len(isiFile)) :
    Mahasiswa = isiFile[i]
    a,b,c = Mahasiswa.split("|")
    if (a == cari) :
        data = "Ada"
        print("Data Mahasiswa")
        print("NIM   : ", a)
        print("Nama   : ", b)
        print("Alamat   :", c)
        break
    else :
        data = "Tidak Ada"
if (data=="Tidak Ada") :
    print ("Data mahasiswa tidak ditemukan")
