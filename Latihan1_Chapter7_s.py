try :
    file = input("Masukkan nama file : ")
    print("isi file", file, "adalah :")
    print(open (file, "r").read())
except FileNotFoundError:
    print("Maaf! File yang anda masukkan tidak ditemukan")
except OSError:
    print("Invalid Argumen! Mohon masukkan argumen yang tepat")
except UnicodeDecodeError:
    print("Maaf! format file salah... silahkan masukkan file dengan format (.txt)")
except ValueError:
    print("Maaf! terjadi kesalahan pada tipe data")
    
