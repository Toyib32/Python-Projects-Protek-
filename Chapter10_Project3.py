file = open("namaDanNIM.txt" , "r")

data = file.readlines()
dataMHS = {}
for i in range(len(data)) :
    Mhs = data[i]
    a,b,c = Mhs.split('|')
    a,b,c = a,b,c.replace('\n', '')
    dataMahasiswa = {'nim' : a, 'nama' : b, 'alamat' : c}
    dataMHS[a] = dataMahasiswa
# lakukan cetak
print(dataMHS)
file.close
