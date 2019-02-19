N = input().split()
alunos = []
for i in range(int(N[0])):
    alunos.append(input())

alunos.sort()
print(alunos[int(N[1])-1])