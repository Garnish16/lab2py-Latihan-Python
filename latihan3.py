# mengimport module math
import math

# masukan atau input nilai variable a dan b
a = input("Masukan nilai a : ")
b = input("Masukan nilai b : ")

# menampilkan isi variable a dan b yang sudah diinput sebelumnya.
print("variable a = ", a)
print("variable b = ", b)


"""
Metode format() memformat nilai yang ditentukan dan memasukkannya ke dalam placeholder string.
Placeholder didefinisikan menggunakan tanda kurung kurawal: {}.
Metode format() mengembalikan string yang diformat.
 {0} akan diisi oleh variable a
 {1} akan diisi oleh variable b
"""
print("Hasil penggabungan {0} & {1} = " .format(a, b) + (a + b))

# mengkonversi nilai variable ke integer dengan method int()
a = int(a)
b = int(b)

# pow() method untuk mempangkatkan nilai. variable a pangkat b
pangkat = pow(a, b)

# menampilkan hasil penjumlahan dari a + b
print("Hasil Penjumlahan {0} + {1} = %d".format(a, b) % (a + b))

# menampilkan hasil pembagian dari a / b
print("Hasil Pembagian {0} / {1} = %d".format(a, b) % (a / b))

# menampilkan hasil perkalian dari a * b
print("Hasil Perkalian {0} * {1} = %d".format(a, b) % (a * b))

# menampilkan hasil perpangkatan dari a ^ b
print("Hasil Perpangkatan {0}^{1} = %d".format(a, b) % pow(a, b))

"""Metode math.sqrt() => mengembalikan akar kuadrat dari suatu angka:
kita akan menampilkan hasil akar kuadrat dari variable pangkat diatas
"""
print("Hasil akar {0} = %d".format(pangkat) % math.sqrt(pangkat))
