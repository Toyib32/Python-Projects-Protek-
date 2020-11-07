# lakukan input
bIndo = int(input("Masukkan nilai Bahasa Indonesia  :"))
ipa = int(input("Masukkan nilai IPA               :"))
matematika = int(input("Masukkan nilai Matematika        :"))

# lakukan cetak
print("-------------------------------------"+"\n")
if(bIndo >= 60) and (ipa >= 60) and (matematika >= 70):
    print("Status Kelulusan                 : LULUS")
elif(bIndo < 0) or (bIndo > 100) or (ipa < 0) or (ipa > 100) or (matematika < 0) or (matematika > 100):
    print("Maaf input ada yang tidak valid")
else:
    print("Status Kelulusan                 : TIDAK LULUS")
    print("Sebab                            :")
    if(bIndo < 60):
        print("- Nilai Bahasa Indonesia kurang dari 60")
    if(ipa < 60):
        print("- Nilai IPA kurang dari 60")
    if(matematika < 70):
        print("- Nilai matematika kurang dari 70")
    
