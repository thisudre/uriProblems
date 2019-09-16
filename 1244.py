def insertionsort(lista):
    for i in range(len(lista)):
        maior_elemento = lista[i]
        indice = i
        for j in range(i+1, len(lista)):
            if(len(lista[j]) > len(maior_elemento)):
                maior_elemento = lista[j]
                indice = j
                pass
            pass
        lista.pop(indice)
        lista.insert(i, maior_elemento)
        pass
    return lista

testes = int(input())
while(testes > 0):
    strings = input().split()
    strings = insertionsort(strings)
    print(" ".join(strings))
    testes -= 1
