# pembuka
print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. silahkan tebak ya!!!")
jawaban = int(input("Tebakan anda :"))

# lakukan validasi 
from random import randint
while True:
    bil = randint(0,100)
    if(bil == 10):
        if(jawaban < bil):
            print("Hehehe... Bilangan tebakan anda terlalu kecil")
            jawaban = int(input("Tebakan anda :"))
        elif(jawaban > bil):
            print("Hehehe... Bilangan tebakan anda terlalu besar")
            jawaban = int(input("Tebakan anda :"))
        elif(jawaban == bil):
            print("Yee... Bilangan tebakan anda BENAR:-)")
            break
   
     
    
        
                
