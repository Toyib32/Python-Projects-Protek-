# import datetime and Project1_Chapter11
from datetime import *
import Project1_Chapter11
# read file
fileTeks = open('dataPeminjam.txt', 'r')
isiTeks = fileTeks.readlines()
# create input
bookCode = input('Masukkan Kode Member : ')
# loop for find data
for x in range(len(isiTeks)) :
    if (bookCode in isiTeks[x]) :
        difference = isiTeks[x].split('|')
        bookStatus = 'available'
        break
    
    else :
        bookStatus = 'notAvailable'
        continue

#membuat percabangan agar bisa menemukan data peminjaman buku
if (bookStatus == 'available'):
    print('Data Peminjam Buku')
    print('Kode Member                 : ', difference[0])
    print('Nama Member                 : ', difference[1])
    print('Judul Buku                  : ', difference[2])
    print('Tanggal Mulai Peminjaman    : ', difference[3])
    print('Tangal Pengambilan Maksimal : ', difference[4])
    print('Tanggal Pengembalian Buku   : ', datetime.date(datetime.now()))
    # create formula
    late = Project1_Chapter11.diffDate(difference[4])
    punishLate = 2000 * abs(late)
    # branching for late or not
    if(late >= 0 ) :
        print('Terlambat   : 0 hari')
        print('Denda       : 0')
    else :
        print('Terlambat : ', abs(late))
        print('Denda       : ', punishLate)
else :
    print('Peminjaman Buku Tidak Ada')
            


        
