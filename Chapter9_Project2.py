def bintang(n) :
    for a in range(1, n+1) :
        formation = "*" * (1 + (a-1)*2)
        print(formation.center(50))

        
bintang(10)

