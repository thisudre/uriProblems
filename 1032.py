def listar_primos(lista_primos, tam_min):
    a = 2
    if (len(lista_primos) != 0):
        a = lista_primos[len(lista_primos)-1]
    i = a
    while (len(lista_primos) < tam_min):
        eh_primo = 1
        for j in range(2, int(i**(1/2)) + 1):
            if(i % j == 0):
                eh_primo = 0
                break
                pass
            pass
        if (eh_primo == 1):
            lista_primos.append(i)
            pass
        i += 1
        pass
    return lista_primos

def criar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(i+1)
        pass
    return lista

def tirar_numero(lista, lista_primos):
    i = 0
    remover = -1
    while(len(lista) > 1):
        remover += lista_primos[i]
        i += 1
        while(remover >= len(lista)):
            remover -= len(lista)
            pass
        lista.pop(remover)
        remover -= 1
        pass
    return lista[0]

lista_primos = listar_primos([], 3501)
while (True):
    tamanho = int(input())
    if (tamanho == 0):
        break
        pass
    else:
        print(tirar_numero(criar_lista(tamanho), lista_primos))
