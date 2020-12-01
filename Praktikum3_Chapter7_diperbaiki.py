try:
    file = open("d:/data1.txt", "r")
    sum = 0
    for data in file:
        try :
            sum = sum + int(data)
        except ValueError:
            continue
    print (sum)
except ValueError:
    print("tidak dapat menjumlahkan dengan alfabet")

