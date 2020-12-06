sayuran = ["Bayam" , "Kangkung", "Wortel" , "Selada"]

def tambahSayur():
    sayur = input("Masukkan nama sayur yang ingin ditambahkan : ")
    sayuran.append(sayur)
    return sayuran

def hapusSayur():
    sayurHapus = input("Masukkan nama sayur yang ingin dihapus : ")
    sayuran.remove(sayurHapus)
    return sayuran

def sayurRead():
    print (sayuran)

print ("Apa yang Program bisa lakukan untukmu : ")
print ("A. Tambah data sayur")
print ("B. Hapus data sayur")
print ("C. Tampilkan data sayur")
print ("D. Keluar")


while True:
    print()
    pilihan = input("Pilihan Anda : ")

    if  ( pilihan == "A" or pilihan == "a") :
        tambahSayur()
    elif (pilihan == "B" or pilihan == "b") :
        menghapusSayur()
    elif (pilihan == "C" or pilihan == "c") :
        sayurRead()
    elif (pilihan == "D" ) :
        break
    else:
        print ("incorrect input")
        continue
