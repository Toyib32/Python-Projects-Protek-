# keterangan jumlah gaji pokok berdasarkan golongan 
A = 10000000
B = 8500000
C = 7000000
D = 5500000

# keterangan jumlah potongan berdasarkan golongan
potA = 2.5
potB = 2.0
potC = 1.5
potD = 1.0

# lakukan input
kodeKaryawan = input("Masukkan kode karyawan    :")
namaKaryawan = input("Masukkan nama karyawan    :")
golongan = input("Masukkan golongan         :")

# lakukan cetak 
print("============================================"+"\n")
print("STRUK RINCIAN GAJI KARYAWAN"+"\n")
print("--------------------------------------------"+"\n")
print("Nama Karyawan             :",(namaKaryawan),"(kode:",(kodeKaryawan),")")
print("Golongan                  :",(golongan),""+"\n")
print("--------------------------------------------"+"\n")
if(golongan == "A"):
    print("Gaji Pokok                : Rp",(A))
    print("Potongan(",(potA),"%)          : Rp",int(A*potA/100),""+"\n")
    print("-------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(A - A*potA/100))                  
elif(golongan == "B"):
    print("Gaji Pokok                : Rp",(B))
    print("Potongan(",(potB),"%)          : Rp",int(B*potB/100),""+"\n")
    print("--------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(B - B*potB/100))
elif(golongan == "C"):
    print("Gaji Pokok                : Rp",(C))
    print("Potongan(",(potB),"%)          : Rp",int(C*potC/100),""+"\n")
    print("-------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(C - C*potC/100))
elif(golongan == "D"):
    print("Gaji Pokok                : Rp",(D))
    print("Potongan(",(potB),"%)          : Rp",int(D*potD/100),""+"\n")
    print("-------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(D - D*potD/100))
elif( not golongan == "A, B, C, D"):
    print("Mohon maaf, Data yang Anda input pada golongan tidak tepat. silahkan masukkan ulang data dengan benar!.. input golongan (A - D)")
    

          
    

    
    




