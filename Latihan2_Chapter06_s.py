# program formasi pertama
print("formasi bintang ke-1")
def starFormation1(n):
    kolom = 0
    baris = n

    i = 0
    while(i <= n):
        j = 0
        while(j < kolom):
            print("*", end='')
            j += 1
        print('')
        i += 1
        kolom += 1

# output formasi pertama
starFormation1(4)
print()

# program formasi kedua
print("formasi bintang ke-2")
def starFormation2(n):
    kolom = n
    baris = n

    i = 0
    while(i <= n):
        j = 0
        while(j < kolom):
            print("*", end='')
            j += 1
        print('')
        i += 1
        kolom -= 1
# output formasi kedua 
starFormation2(4)
print()

# program formasi gabungan 1 dan 2
print("formasi bintang ke-3")
def starFormation3(n):
    kolom = 0
    baris = n
    middle = (n+1)/2

    i = 0
    while(i <= n):
        j = 0
        while(j < kolom):
            print("*", end='')
            j += 1
        print()
        i += 1
        kolom += 1

        if(kolom == middle):
            kolom = middle
            baris = middle

            i = 0
            while(i <= n):
                j = 1
                while(j <= kolom):
                    print("*", end='')
                    j += 1
                print()
                i += 1
                kolom -= 1

# Output formasi ketiga
starFormation3(7)
print()

            
