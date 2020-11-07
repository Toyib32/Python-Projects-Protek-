# lakukan input
bIndo = int(input("Masukkan nilai Bhs Indonesia     :"))
ipa = int(input("Masukkan nilai IPA               :"))
matematika = int(input("Masukkan nilai Matematika        :"))

# lakukan cetak
print("-------------------------------------"+"\n")
if(bIndo < 0) or (bIndo > 100) or (ipa < 0) or (ipa > 100) or (matematika < 0) or (matematika > 100):
    print("Maaf input ada yang tidak valid")
elif(bIndo >= 60) and (ipa >= 60) and (matematika >= 70):
    print("Status Kelulusan                 : LULUS")
else:
    print("Status Kelulusan                 : TIDAK LULUS")
