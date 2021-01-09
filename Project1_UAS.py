#program save data to file .dat
#import os and datetime
from datetime import *
import os

#create a file .dat if does not exists
#add data to file .dat if exists
if (os.path.exists):
    modeFileTeks = 'a'
else :
    modeFileTeks = 'w'
fileTeks = open('dataKaryawan.dat', modeFileTeks)

#function to add karyawan
def addKaryawan (nip, name, address, gol, birth, age):

    listDataKaryawan = [nip, name, address, gol, birth, str(age) + '\n']
    fileTeks.write('|'.join(listDataKaryawan))
    
#function to counting age
def getAge(birth):
    splited = birth.split('-')
    birthYear = int(splited[0])
    currentYear = datetime.now()
    age = currentYear.year - birthYear
    return age

#loop to add data karyawan
while True:
    nip = input('Masukkan NIP                    : ')
    name = input('Masukkan Nama                  : ')
    address = input('Masukkan Alamat             : ')
    gol = input('Masukkan Golongan ( A / B / C ) : ')
    #create branching
    if(gol.lower() == 'a' or gol.lower() == 'b' or gol.lower() == 'c'):
        birth = input('Masukkan Tgl Lahir (Format : yyyy-mm-dd) : ')
        ageNow = getAge(birth)
        #block exeption
        try :
            if (datetime.strptime(birth, '%Y-%m-%d')):
                ifAdd = input('\nTambah data ( y / n) : ')
                #create branching
                if (ifAdd.lower() == 'y'):
                    addKaryawan(nip, name, address, gol, birth, ageNow)
                    continue
                elif (ifAdd.lower() == 'n'):
                    addKaryawan(nip, name, address, gol, birth, ageNow)
                    break
                else :
                    print('invalid input')
                    addKaryawan(nip, name, address, gol, birth, ageNow)
                    break
        except ValueError :
            print ('invalid input')
            continue
    else :
        print('invalid input')
        continue

#for close text
fileTeks.close()


