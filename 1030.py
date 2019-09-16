def eliminar_soldado(lista, salto):
    i = -1
    while (len(lista)>1):
        i += salto
        while (i >= len(lista)):
            i -= len(lista)
            pass
        lista.pop(i)
        i -= 1
        pass
    return lista[0]

def criar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(i+1)
        pass
    return lista

for i in range(int(input())):
    entry1 = list(map(int, input().split()))
    print("Case {:d}: {:d}".format(i+1, eliminar_soldado(criar_lista(entry1[0]), entry1[1])))
