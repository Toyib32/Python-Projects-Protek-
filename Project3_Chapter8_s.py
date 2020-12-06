nama = []
i = True

while(i == True) :
    namaInput = input("Masukkan Nama Anda : ")
    nama.append(namaInput)

    lanjutan = input("Masukkan nama panjang lagi? (y/n) : ")

    if(lanjutan == "y"):
        i = True

    elif(lanjutan == "n"):
        i = False

    else:
        print ("incorrect input! silahkan masukkan ulang input sesuai petunjuk")
        break
print ()
nama.sort()

for x in range(len(nama)) :
    print(nama[x], "(" , len(nama[x]), "karakter ) " ) 
