# lakukan import
import random
def shuffleString(a, n):
    randomInput = []
    
    for i in range(n) :
        b = list(random.sample(a, len(a)))
        c = "".join(b)
        
        if(c in randomInput) :
            continue
        else :
            randomInput.append(c)
            print(c)


kata = input("silahkan input kata / teks yang akan diacak: ")
acak = int(input("jumlah kombinasi acak yang diinginkan: "))
# lakukan pemanggilan cetak 
shuffleString(kata,acak)
