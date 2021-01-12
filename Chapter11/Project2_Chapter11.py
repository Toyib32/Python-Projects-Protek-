# menyimpan data peminjam dengan max pinjaman 7 hari
# inport datetime and os 
from datetime import *
import os
# file text mode
if (os.path.exists('dataPeminjam.txt')):
    fileTeksMode = 'a'
else:
    fileTeksMode = 'w'
fileTeks = open('dataPeminjam.txt', fileTeksMode)
# create input and save data input
while True:
    code = input('Masukkan Kode Member   : ')
    name = input('Masukkan Nama Member   : ')
    title = input('Masukkan Judul Buku    : ')

    dayTake = date.today()
    dayTurn = dayTake + timedelta(days = 7)
    dataTake = [code, name, title, str(dayTake), str(dayTurn), '\n']
    fileTeks.write('|'.join(dataTake))
    # loop for add data
    repeat = input('Ulangi lagi (y/n) : ')

    if (repeat.lower() == 'y'):
        continue
    elif (repeat.lower() == 'n'):
        break
    else :
        print('invalid input. silahkan masukkan dengan benar')
fileTeks.close()
