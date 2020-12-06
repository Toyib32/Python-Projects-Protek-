print ("-----------------------------------------------")
print ("PROGRAM HITUNG RATA-RATA")
print ("-----------------------------------------------")

data = True
sum = 0
penjumlahan = 0
while (data == True):
# blok try-except
    try :
        bil = int(input("Masukkan bilangan bulat : "))
        sum += bil
        penjumlahan +=1

        option = input('Lagi ? (y/n) : ')
        if(option == "y"):
            data = True
        elif(option == "n"):
            data = False
        else :
            print ("Hanya dapat memasukkan y/n ")
            break
    except ValueError :
        print("Bukan bilangan bulat")
        print("Silahkan masukkan bilangan bulat lagi")
        continue
rataan = sum / penjumlahan 
print("Rata-ratanya adalah : ",rataan)
        
