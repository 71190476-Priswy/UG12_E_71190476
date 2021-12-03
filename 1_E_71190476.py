a = int(input("Masukkan awal deret: "))
b = int(input("Masukkan akhir deret: "))

if a %2 == 1:
    a = a + 1

c = range(a,b,2)

for x in c:
    if x %5 == 0:
        continue
    elif x %9 == 0:
        continue
    print (x ,end= (" "))