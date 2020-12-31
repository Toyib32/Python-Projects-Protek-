print("----------- Menambahkan data Mahasiswa -----------")
file = open("namaDanNIM.txt", "a")
# Lakukan input
i = True
while ( i == True) :
    nim = input("Masukkan NIM : ")
    namaMhs = input("Masukkan Nama Mhs : ")
    alamat = input("Masukkan Alamat : ")

    file.write(nim + "|" + namaMhs + "|" + alamat + "\n")  
    ulangi = input("Ulangi input lagi (y/n) : ")
    
    if (ulangi == "y") :
        i = True
    elif  (ulangi == "n"):
        i = False
    else :
        print ("Maaf! data yang anda masukkan tidak valid. silahkan ulangi kembali")
        continue
file.close()

