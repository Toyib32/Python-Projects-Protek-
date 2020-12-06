hargaBuah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}

def jumlahBuah() :
    jumlah = int(input('Berapa Kg (dalam satuan KiloGram) : '))
    harga = hargaBuah.get(namaBuah, 0)*jumlah
    return harga

print('Daftar Buah : ')
for a,b in hargaBuah.items() :
    print ('- ' ,a, ' : ' , b)

total =[]
lanjutTidak = True

while (lanjutTidak == True) :
    namaBuah = input('\nNama buah yang akan anda beli apa : ').lower()

    if (namaBuah not in hargaBuah.keys ()) :
        print ('Maaf buah yang anda masukkan tidak invalid dengan daftar buah yang ada ' )
        continue
    else :
        try :
            harga = jumlahBuah ()
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
                
            
                
