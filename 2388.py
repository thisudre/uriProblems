N = int(input())
km = 0
for i in range(N):
    a = input().split()
    km = km + int(a[0]) * int(a[1])
print(km)