mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

listUp = []

for i in range(len(mhs)) :
    up = mhs[i].split(":")
    listUp.append(up)

    down = listUp[i][2].split("-")
    down.reverse()
    
    downJoin = "/".join(down)
    listUp[i][2] = downJoin


print("=" * 70)
print("NIM".ljust(10), "NAMA MAHASISWA".ljust(20),
      "TGL LAHIR".ljust(20), "TEMPAT LAHIR".ljust(10))
print('-' * 70)

for i in range(len(listUp)) :
    print(listUp[i][0].ljust(10),
          listUp[i][1].ljust(20),
          listUp[i][2].ljust(20),
          listUp[i][3].ljust(10),)
print("-" * 70)
