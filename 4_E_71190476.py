def nilai_maksimal():
    y = x[0]
    for z in x:
     if y < z:
        y = z
    print("Nilai terbesar: ",y)
    for z in x:
     if y > z:
        y = z
    print("Nilai terkecil: ",y)

if __name__ == '__main__':
    x = [3, 20, 100, -35, 50]
    print(x)
    nilai_maksimal()