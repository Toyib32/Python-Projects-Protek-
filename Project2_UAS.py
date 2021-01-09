#code to find data karyawan in file .dat
#read file
fileText = open('dataKaryawan.dat', 'r')
textFill= fileText.readlines()
#input user
karyawanCode = input('Masukkan Kode Karyawan : ')
#create loop to find data
#create execption to handle error
try :    
    for i in range(len(textFill)):
        if (karyawanCode in textFill[i]):
            change = textFill[i].replace('\n', '')
            delete = change.split('|')

    karyawanData = {karyawanCode : [delete[1], delete[2], delete[3], delete[4], delete[5]]}
    #create branching
    if (karyawanData[karyawanCode][2]):
        salaryMain = 4000000
    elif (karyawanData[karyawanCode][2]):
        salaryMain = 4500000
    else :
        salaryMain = 5000000

    #print
    print('\nKode Karyawan      : ', karyawanCode)
    print('Nama Karyawan        : ', karyawanData[karyawanCode][0])
    print('Alamat Karyawan      : ', karyawanData[karyawanCode][1])        
    print('Golongan Karyawan  : ', karyawanData[karyawanCode][2])
    print('Gaji Pokok Karyawan : Rp. ', salaryMain)
    print("Tanggal Lahir Karyawan : {0} (Usia: {1} Tahun) ".format(karyawanData[karyawanCode][3], karyawanData[karyawanCode][4]))
except NameError :
    print('invalid input, data karyawan is not found. try again!')
