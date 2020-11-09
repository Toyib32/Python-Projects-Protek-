# definisi faktorial(n)
def faktorial(n):
    faktor = 1
    while(n > 0):
        faktor = faktor*n
        n -= 1
    return faktor

def kombinasi(a, b):
    c = a-b
    hasil = faktorial(a)/(faktorial(b)*faktorial(c))
    print(hasil)

def permutasi(a, b):
    c = a-b
    hasil = faktorial(a)/faktorial(c)
    print(hasil)

# jawaban nomer 3 a (kombinasi)
a = 5
b = 3
print("a. C(a, b) = ")
print(kombinasi(a, b))

# jawaban nomer 3 b (permutasi)
a = 10
b = 7
print("b. P(a, b) = ")
print(permutasi(a, b))
