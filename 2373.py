N = int(input())
quebrou = 0
for i in range(N):
    a = input().split()
    L = int(a[0])
    C = int(a[1])
    if (L>C):
        quebrou = quebrou + C

print (quebrou)