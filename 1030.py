N = int(input())

for i in range(N):
    a = input().split()
    roda = list(range(int(a[0])))
    n = int(a[1])-1
    while len(roda)>1:
        roda.pop(n)
        n = n+int(a[1])-1
        while n>=len(roda):
            n = n - len(roda)

    print("Case " + str(i+1) + ": " + str(roda[0]+1))