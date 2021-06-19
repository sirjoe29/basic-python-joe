def salam():
    print("Selamat datang!")
    print("")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
salam()

d = {
    "nama" : "Andi",
    "no telepon" : "08123456789",
    "nama" : "Budi",
    "no telepon" : "081298765432",    
}   

a = int(input("Pilih menu : "))
print(a)
if a == 1 :
    print(d)
elif a = 2 :
    print()
else:
    print("Program selesai, sampai jumpa!")


for i in range(1):
    nama = input("Nama : ")
    telepon = int(input("No Telepon : "))
      data = {
        "nama" : nama,
        "no telepon" : telepon,
      }
    d.append(data)

for i in d:
    print("Nama : ",i["nama"])
    print("No Telepon : ",i["telepon"])
