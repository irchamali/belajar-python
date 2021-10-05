# seleksi dan kondisi
# memilih suatu kondisi yang terpenuhi
# fungsi aktivasi ==> ReLU.. if(n>0) maka n. else if(n < 0) maka 0
# menerima input dari keyboard, kemudian casting ke int
n = int(input("masukan Nilai: "))
if(n > 0):  # jika terpenuhi jalankan print
    print("nilai: "+str(n))
else:
    print("nilai: "+str(0))


# input n = 0 - 100
# A: 85-100
# B: 70-84
# C: 60-69
# D: <60

# AND == 1 & 1 = 1, 1 & 0 = 0, 0 & 1 = 0, 0 & 0 = 0
# Lazy Condition: AND, OR

n = int(input("Masukan nilai: "))
if(n >= 85 and n <= 100):
    print("A")
elif(n >= 70 and n <= 84):
    print("B")
elif(n >= 60 and n <= 69):
    print("C")
elif(n <= 59 and n >= 0):
    print("D")
else:
    print("Salah")
