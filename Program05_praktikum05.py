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

# tunjangan karyawan dan status
tunjanganIstriSuami = 10
tunjanganAnak = 5

# lakukan input
kodeKaryawan = input("Masukkan kode karyawan    :")
namaKaryawan = input("Masukkan nama karyawan    :")
golongan = input("Masukkan golongan         :")
status = input("Masukkan status (1:menikah, 2:belum) :")
if(status == "1"):
    anak = input("Masukkan jumlah anak      :")

# lakukan cetak 
print("============================================"+"\n")
print("STRUK RINCIAN GAJI KARYAWAN"+"\n")
print("--------------------------------------------"+"\n")
print("Nama Karyawan             :",(namaKaryawan),"(kode:",(kodeKaryawan),")")
print("Golongan                  :",(golongan))
if(status == "1"):
    print("Status Menikah            : Menikah")
    print("Jumlah Anak               :",(anak),""+"\n")
elif(status == "2"):
    print("Status Menikah            : Belum Menikah")
print("--------------------------------------------"+"\n")
if(golongan == "A") and (status == "1"):
    print("Gaji Pokok                : Rp",(A))
    print("Tunjangan Istri/Suami     : Rp",int(A*tunjanganIstriSuami/100))
    print("Tunjangan anak            : Rp",int((A*tunjanganAnak/100)*int(anak)),""+"\n")
    print("-------------------------------------------- +"+"\n")
    print("Gaji Kotor                : Rp",int(A+int(A*tunjanganIstriSuami/100)+int((A*tunjanganAnak/100)*int(anak))))
    print("Potongan(",(potA),"%)          : Rp",int(int(A+int(A*tunjanganIstriSuami/100)+int((A*tunjanganAnak/100)*int(anak)))*(potA/100)),""+"\n")
    print("-------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(int(A+int(A*tunjanganIstriSuami/100)+int((A*tunjanganAnak/100)*int(anak)))- int(int(A+int(A*tunjanganIstriSuami/100)+int((A*tunjanganAnak/100)*int(anak)))*(potA/100))),""+"\n")
elif(golongan == "A") and (status == "2"):
    print("Gaji Pokok                : Rp",(A))
    print("Potongan(",(potA),"%)          : Rp",int(A*potA/100),""+"\n")
    print("--------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(A - A*potA/100))
elif(golongan == "B") and (status == "1"):
    print("Gaji Pokok                : Rp",(B))
    print("Tunjangan Istri/Suami     : Rp",int(B*tunjanganIstriSuami/100))
    print("Tunjangan anak            : Rp",int((B*tunjanganAnak/100)*int(anak)),""+"\n")
    print("-------------------------------------------- +"+"\n")
    print("Gaji Kotor                : Rp",int(B+int(B*tunjanganIstriSuami/100)+int((B*tunjanganAnak/100)*int(anak))))
    print("Potongan(",(potB),"%)          : Rp",int(int(B+int(B*tunjanganIstriSuami/100)+int((B*tunjanganAnak/100)*int(anak)))*(potB/100)),""+"\n")
    print("-------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(int(B+int(B*tunjanganIstriSuami/100)+int((B*tunjanganAnak/100)*int(anak)))- int(int(B+int(B*tunjanganIstriSuami/100)+int((B*tunjanganAnak/100)*int(anak)))*(potB/100))),""+"\n")
elif(golongan == "B") and (status == "2"):
    print("Gaji Pokok                : Rp",(B))
    print("Potongan(",(potB),"%)          : Rp",int(B*potB/100),""+"\n")
    print("--------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(B - B*potB/100))
elif(golongan == "C") and (status == "1"):
    print("Gaji Pokok                : Rp",(C))
    print("Tunjangan Istri/Suami     : Rp",int(C*tunjanganIstriSuami/100))
    print("Tunjangan anak            : Rp",int((C*tunjanganAnak/100)*int(anak)),""+"\n")
    print("-------------------------------------------- +"+"\n")
    print("Gaji Kotor                : Rp",int(C+int(C*tunjanganIstriSuami/100)+int((C*tunjanganAnak/100)*int(anak))))
    print("Potongan(",(potC),"%)          : Rp",int(int(C+int(C*tunjanganIstriSuami/100)+int((C*tunjanganAnak/100)*int(anak)))*(potC/100)),""+"\n")
    print("-------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(int(C+int(C*tunjanganIstriSuami/100)+int((C*tunjanganAnak/100)*int(anak)))- int(int(C+int(C*tunjanganIstriSuami/100)+int((C*tunjanganAnak/100)*int(anak)))*(potC/100))),""+"\n")
elif(golongan == "C") and (status == "2"):
    print("Gaji Pokok                : Rp",(C))
    print("Potongan(",(potC),"%)          : Rp",int(C*potC/100),""+"\n")
    print("--------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(C - C*potC/100))
elif(golongan == "D") and (status == "1"):
    print("Gaji Pokok                : Rp",(D))
    print("Tunjangan Istri/Suami     : Rp",int(D*tunjanganIstriSuami/100))
    print("Tunjangan anak            : Rp",int((D*tunjanganAnak/100)*int(anak)),""+"\n")
    print("-------------------------------------------- +"+"\n")
    print("Gaji Kotor                : Rp",int(C+int(D*tunjanganIstriSuami/100)+int((D*tunjanganAnak/100)*int(anak))))
    print("Potongan(",(potD),"%)          : Rp",int(int(D+int(D*tunjanganIstriSuami/100)+int((D*tunjanganAnak/100)*int(anak)))*(potD/100)),""+"\n")
    print("-------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(int(D+int(D*tunjanganIstriSuami/100)+int((D*tunjanganAnak/100)*int(anak)))- int(int(D+int(D*tunjanganIstriSuami/100)+int((D*tunjanganAnak/100)*int(anak)))*(potD/100))),""+"\n")
elif(golongan == "D") and (status == "2"):
    print("Gaji Pokok                : Rp",(D))
    print("Potongan(",(potD),"%)          : Rp",int(D*potD/100),""+"\n")
    print("--------------------------------------------- -"+"\n")
    print("Gaji Bersih               : Rp",int(D - D*potD/100))
elif( not golongan == "A, B, C, D"):
    print("Mohon maaf, Data yang Anda input pada golongan tidak tepat. silahkan masukkan ulang data dengan benar!.. input golongan (A - D)")
    
