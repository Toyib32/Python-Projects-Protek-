buah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}

def jumlahBuah (namaBuah) :
    jumlah = int(input('Berapa Kg (dalam satuan KiloGram) : '))
    hargan = buah.get(namaBuah, 0)*jumlah
    return hargan

def beliBuah(buahyib) :
    print('Daftar Buah : ')

    for a,b in buah.items() :
        print ('- ' ,a, ' : ' , b)

    total =[]
    lanjutTidak = True

    while (lanjutTidak == True) :
        namaBuah = input('\nNama buah yang akan anda beli apa : ').lower()

        if (namaBuah not in buahyib.keys ()) :
            print ('Maaf buah yang anda masukkan tidak invalid dengan daftar buah yang ada ' )
            continue
        else :
            try :
                harga = jumlahBuah (namaBuah)
                total.append(harga)
                pilihan = input('Mau beli buah yang lain atau tidak mumpung ada promo (y/n) ? ').lower()

                if (pilihan == 'y') :
                    lanjutTidak = True
                elif (pilihan == 'n'):
                    lanjutTidak = False
                else :
                    print ('Inputan Tidak Valid')
                    break
            except TypeError :
                print ('Tuhkan salah input an nya, kan cuman ada (y/n), jangan yang lain')
                continue
            except ValueError :
                print ('\nInputan Invalid Coba Lagi di Ulangi Siapa tau bisa ^_^')
                continue
    print ('=================================')
    print ('Total Harga Buah yang di beli : ' , sum(total))

def nambahBuah(buahyib) :
    namaBuahBaru = input('Masukkan nama buah : ').lower()

    while True :
        try :
            if(namaBuahBaru in buahyib.keys() ):
                print (' Buah ', namaBuahBaru, 'buah sudah di dalam data. Sekarang masukkan harga buah berapa ? ')
                hargaBuahBaru = int(input('\nMasukkan harga buah dalam bentuk satuan angka : '))

                yibBuahBaru = {namaBuahBaru : hargaBuahBaru}
                buahyib.update(yibBuahBaru)

                print('Data Buah : ')

                for a,b in buah.items() :
                      print ('- ' ,a, '(harga  : ' , b, ')')
            else :
                hargaBuahBaru = int(input('\nMasukkan Harga dalam bantuk satuan angka : '))
                buah[namaBuahBaru] = hargaBuahBaru

                print('Data Buah : ')
                
                for a,b in buah.items() :
                      print ('- ' ,a, '(harga  : ' , b, ')')
            break
        except ValueError :
            print ('\nInputan Invalid Coba Lagi di Ulangi Siapa tau bisa ^_^')
            continue
print ('Daftar menu : ')
print('a. Tambah data buah')
print('b. Beli buah')
print('97. Keluar')

while True :
    pilihanDaftarMenu = input('\nPilihan Menu : ').lower()

    if(pilihanDaftarMenu == 'a') :
        nambahBuah(buah)
    elif(pilihanDaftarMenu == 'b') :
        beliBuah(buah)
    elif(pilihanDaftarMenu == '97') :
        break
    else :
        print('Tuhkan ada yang salah input an, coba lagi deh, SEMANGATTTT')
        continue

                


                
                
            
                
