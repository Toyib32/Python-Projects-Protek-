def ubahHuruf1(teks, a, b):
    teksA = teks.replace(a, b)
    return teksA

def ubahHuruf2(teks, a, b):

    listTeks = list(teks)
    for i in range(len(listTeks)):
        if(listTeks[i] == a):
            listTeks[i] = b
            
    teksA = ''.join(listTeks)
    return teksA

# lakukan penginputan 
teks = input("silahkan masukkan kata / kalimat yang ingin dirubah : ")
a = input("Huruf apa yang ingin dirubah pada kata/kalimat tersebut : ")
b = input("Ubah {0} menjadi : ".format(a))

# lakukan cetak
hasil1 = ubahHuruf1(teks, a, b)
print(hasil1)

hasil2 = ubahHuruf2(teks, a, b)
print(hasil2)
