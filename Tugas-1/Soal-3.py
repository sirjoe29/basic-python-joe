nilai_teori = int(input("Nilai ujian teori Anda : "))
nilai_praktek = int(input("Nilai ujian praktek Anda : "))

#boolean
if nilai_teori >= 70 and nilai_praktek >= 70:
    print("Selamat, Anda lulus")
elif nilai_teori >= 70 and nilai_praktek <= 70:
    print("Anda harus mengulang ujian praktek.")
elif nilai_teori <= 70 and nilai_praktek >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")