a = input().split()
lim = True
elevador = 0
for i in range(int(a[0])):
    b = input().split()
    elevador = elevador - int(b[0]) + int(b[1])
    if (elevador > int(a[1])):
        lim = False
    else:
        pass

if (lim == False):
    print("S")
else:
    print("N")