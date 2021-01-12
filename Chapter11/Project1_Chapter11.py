# import datetime 
from datetime import *
# create functtion diffdate 
def diffDate (x):
    divide = x.split('-')
    dayList = []
    # looping for counting day
    for y in divide :
        dayList.append(int(y))

    day = date(dayList[0], dayList[1], dayList[2])
    dayRun = datetime.date(datetime.now())
    difference = day - dayRun
    resultDifference = abs(difference.days)
    return resultDifference

#mencoba Program untuk menghitung selisih hari
''' 
print(diffDate('2021-01-20'))
print(diffDate('2020-12-20'))
print(diffDate('2022-09-10'))
'''
#membuat program jika user yang harus menginput tahun, bulan, dan tanggal
''' 
# exception handling 
try :
    dayNow = input('Masukkan tanggal, dengan Format (yyyy-mm-dd) : ')
    diff = diffDate(dayNow)
    # Output
    print ('Selisih dengan tanggal yang di input adalah : ', diff, 'hari')
except ValueError :
    print('invalid input!. silahkan coba lagi sesuai petunjuk')
''' 
