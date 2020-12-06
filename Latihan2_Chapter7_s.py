import os
# blok try-except
try :
    file = input("Masukkan Nama File: ")
    if os.path.exists(file):
        mode = "a"
    else :
        mode = "r"

    dataFile = open(file, mode)

    jikaData = True
    while(jikaData == True):
        data = input("Data yang mau ditambahkan: ")
        dataFile.write("\n" + data)

        jawabUser = input("Mau lagi ? (y/n) : ")
        if (jawabUser == "y"):
            jikaData = True
        elif (jawabUser == "n"):
            jikaData = False
        else :
            print("Input Tidak valid")
            break
    dataFile.close()

except FileNotFoundError :
    print("Maaf!.. File Tidak Ditemukan")
