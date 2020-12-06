while True:
    try:
        n =int(input("Silahkan masukkan banyak data yang Anda inginkan (***data = bilangan bulat***): "))
        break
    except ValueError :
        print ("incorrect input! silahkan masukkan kembali data sesuai petunjuk")
        continue

data =[ ]

i = 0
while (i < n) :
    try :
        bil = int(input('Masukkan bilangan bulat yang anda inginkan : '))
        data.append(bil)
        i +=1
    except ValueError :
        print ('Inputan tidak valid')
data.sort(reverse = True)
print (data)
        
