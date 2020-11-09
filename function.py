# function 1 jumlah total
def sum(*n):
    i = 0
    for a in n:
        i = i+a
    print(i)
# function 2 rata-rata
def average(*n):
    i = 0
    j = 0
    for a in n:
        i = i+a
        j += 1
    average = i/j
    print(average)
# function 3 nilai maksimum
def maks(*n):
    maks = n[0]
    for i in (n):
        if(i > maks):
            maks = i
    print(maks)
# function 4 nilai minimum
def min(*n):
    min = n[0]
    for i in (n):
        if(i < min):
            min = i
    print(min)
    
