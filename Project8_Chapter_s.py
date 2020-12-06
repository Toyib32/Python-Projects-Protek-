hargaBuah = {"Apel" : 5000, "Jeruk" : 8500, "Mangga" : 7800, "Duku" : 6500}

def rata2HargaBuah (hargaBuah):
    zigma = 0
    jumlah = 0

    for x,y in hargaBuah.items() :
        zigma += y
        jumlah +=1

    rata2 = zigma / jumlah
    return rata2
print(rata2HargaBuah(hargaBuah))




