def bintang(n):
    sudutRuncing = int(n / 2 + 1)
    for a in range(1, n+1):
        formasi = "*" * (1 + (a-1)*2)
        print(formasi.center(50))
        
        if(a == sudutRuncing): 
            for a in range(sudutRuncing - 1, 0, -1):
                formasi = "*" * (1 + (a-1)*2)
                print(formasi.center(50))     
            break
# lakukan pemanggilan cetak
bintang(7)
