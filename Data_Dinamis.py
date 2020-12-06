#no 1
a= [1, 5, 6, 3, 6,  9,11,  20, 12]
b=[7, 4, 5, 6, 7, 1, 12, 5, 9]
print (a)
print(b)
print()
#no 2
a.insert(3,10)
b.insert(2,15)
print (a)
print(b)
print()
#no 3
a.append(4)
b.append(8)
print (a)
print(b)
print()
#no 4
a.sort()
b.sort()
print (a)
print(b)
print()
#no 5
x = a[0:8]
y = b[2:10]
print(x)
print(y)
print()
#no 6
e = [ ]
for z in range(len(y)):
    element = x[z] + y[z]
    e.append(element)
print (e)
print()
#no 7
data = tuple(e)
#no 8
minimal = min (data)
maksimal = max(data)
penjumlahan = sum(data)
print(minimal)
print(maksimal)
print(penjumlahan)
print()
#no 9
myString = 'Python adalah bahasa pemograman yang menyenangkan'
#no 10
charPenyusunan = set(myString)
print(charPenyusunan)
print()
#no 11
listPenyusun = list(charPenyusunan)
listPenyusun.sort()
print(listPenyusun)

