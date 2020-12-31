# membuka dan menambahkan file txt
penjumlahan = open('Penjumlahan.txt', 'r')
hasil = open('HasilPenjumlahan.txt', 'a')
file = penjumlahan.readlines()
for i in range(len(file)) :
    bil = file[i]
    bil1, bil2 = bil.split('|')
    bil3 = int(bil1) + int(bil2)
    bil4 = str(bil3)
    hasil.write(bil4)
    hasil.write('\n')
hasil.close()
# lakukan cetak
cetakHasil = open('HasilPenjumlahan.txt', 'r')
print("-------- Hasil Penjumlahan --------")
print(cetakHasil.read())
cetakHasil.close()
