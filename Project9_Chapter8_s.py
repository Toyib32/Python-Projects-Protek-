hargaBuah = {"apel" : 5000, "jeruk" : 8500, "mangga" : 7800, "duku" : 6500}

def jumlahBuah() :
    jumlah = int(input("Berapa Kg (dalam satuan KiloGram) : "))

    print ('======================')
    print ( 'Total Harga : ', hargaBuah.get(namaBuah, 0)*jumlah)

print('Daftar Buah : ')
for a,b in hargaBuah.items() :
    print ('- ' ,a, ' : ' , b)

while True :
    namaBuah = input('\nNama buah yang akan anda beli apa : ')

    if (namaBuah not in hargaBuah.keys ()) :
        print ('Maaf buah yang anda masukkan tidak invalid dengan daftar buah yang ada ' )
        continue
    else :
        while True :
            try :
                jumlahBuah()
                break
            except ValueError :
                continue
        break
