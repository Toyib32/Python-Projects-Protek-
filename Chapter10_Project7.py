# mengubah kembali sandi
kataSandi = open('HasilSandiFile.txt', 'r')
jumlahInput = int(input('Masukkan nilai n : '))
membaca = kataSandi.read()
terjemahkan = list(membaca)
karakterTerjemahan = []
for x in terjemahkan :
    if (x == ' ') :
        d = ord(x)
    else :
        a = ord(x)
        d = a - jumlahInput
        if (d < 65) :
            d = d + 26
        elif (90 < d and d <97) :
            d = d + 26
    Terjemahan = chr(d)
    karakterTerjemahan.append(Terjemahan)
kalimatTerjemahan = ''.join(karakterTerjemahan)
hasilTerjemahan = open('HasilTerjemahanFile.txt', 'w')
hasilTerjemahan.write(kalimatTerjemahan)
hasilTerjemahan.close()
    
