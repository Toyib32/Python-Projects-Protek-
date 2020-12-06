def dataStat(x):
    a = sum(x) / len(x)
    b = max(x)
    c = min(x)

    dataHasil = [a, b, c]

    return dataHasil

while True:
    try:
        n = int(input("Silahkan masukkan banyak data yang Anda inginkan (***data = angka***) :"))
        break
    except ValueError:
        print ("incorrect input! silahkan masukkan kembali data sesuai petunjuk")
        continue
dataHasil = []
i = 0
while (i < n):
    try :
        bilangan = int(input("silahkan input data berupa bilangan bulat :"))
        dataHasil.append(bilangan)
        i +=1
    except ValueError :
        print ("incorrect input! silahkan masukkan kembali data sesuai petunjuk")
cetak = dataStat(dataHasil)
print(cetak)
    
