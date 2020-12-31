print("---------- Menghitung banyak bilangan ----------")
file = open('deretBilangan.txt','r')
isiFile = file.readlines()
#lakukan perhitungan
genap = []
ganjil = []
for i in range(len(isiFile)):
    if ('\n' in isiFile[i] == True):
        IsiFile[i].replace('\n', '')

        if (int(isiFile[i])%2 == 0):
            genap.append(isiFile[i])
        else :
            ganjil.append(isiFile[i])
    else :
        if (int(isiFile[i])%2 == 0) :
            genap.append(isiFile[i])
        else :
            ganjil.append(isiFile[i])\
                                       
# lakukan cetak
print("Banyaknya bilangan Genap : {0}".format(len(genap)))
print("Banyaknya bilangan Genap : {0}".format(len(ganjil)))
