from random import randint
toyib = 0
while True:
    bil = randint(0, 10)
    print(bil)
    toyib = toyib + 1
    if bil == 5:
        break
print("Jumlah perulangan : " + str(toyib))
