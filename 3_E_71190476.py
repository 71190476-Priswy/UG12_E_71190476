n = int(input("Masukkan Angka: "))

for x in range(0,n):
    print(" " * (n-x) ,x * "* ")

for x in range(n,0,-1):
    print(" " * (n-x) ,x * "* ")