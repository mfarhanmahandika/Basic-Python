kkm = 70

teori = int(input("nilai teori: "))
praktek = int(input("nilai praktek: "))

if teori >= kkm and praktek >= kkm:
    print("Selamat, anda lulus!")

if teori >= kkm and praktek < kkm:
    print("Anda harus mengulang ujian praktek.")

if teori <kkm and praktek >=kkm:
    print("Anda harus mengulang ujian teori")

if teori <kkm and praktek < kkm:
    print("Anda harus mengulang ujian teori dan praktek")
