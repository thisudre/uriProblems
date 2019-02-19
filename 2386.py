tel = int(input())
N = int(input())
qtd = 0
for i in range(N):
    if (tel*int(input()) >= 40000000):
        qtd += 1
print(qtd)