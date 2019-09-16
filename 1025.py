def partition(lista, inicio, fim): 
    i = (inicio-1)
    pivo = lista[fim] 
    for j in range(inicio, fim): 
        if   lista[j] <= pivo:
            i = i+1
            lista[i], lista[j] = lista[j], lista[i] 
    lista[i+1], lista[fim] = lista[fim], lista[i+1] 
    return (i+1)

def quick_sort(lista, inicio, fim): 
    if inicio < fim:
        pivo = partition(lista, inicio, fim)
        quick_sort(lista, inicio, pivo-1) 
        quick_sort(lista, pivo+1, fim)

def busca_binaria (lista, buscado, inicio, fim):
    meio = int((inicio+fim)/2)
    if (lista[meio] == buscado):
        indice = checa_anterior(lista, meio)
        return indice
    elif (inicio >= fim):
        return -1
    else:
        if(lista[meio] < buscado):
            return busca_binaria(lista, buscado, meio+1, fim)
        else:
            return busca_binaria(lista, buscado, inicio, meio-1)
        pass
    pass

def checa_anterior(lista, indice):
    novo_indice = indice
    if(indice != 0):
        while((lista[novo_indice] == lista[novo_indice-1]) and (novo_indice != 0)):
            novo_indice = busca_binaria(lista, lista[novo_indice], 0, novo_indice)
            pass
    return novo_indice

caso = 0
while (True):
    caso += 1
    entrada1 = list(map(int, input().split()))
    if(entrada1 == [0, 0]):
        break
        pass
    else:
        marmores = entrada1[0]
        testes = entrada1[1]
        lista_marmores = []
        while(marmores > 0):
            lista_marmores.append(int(input()))
            marmores -= 1
            pass
        quick_sort(lista_marmores, 0, len(lista_marmores)-1)
        print("CASE# {:d}:".format(caso))
        while(testes > 0):
            buscado = int(input())
            indice = busca_binaria (lista_marmores, buscado, 0, len(lista_marmores) - 1) + 1
            if (indice == 0):
                print("{:d} not found".format(buscado))
                pass
            else:
                print("{:d} found at {:d}".format(buscado, indice))
            testes -= 1
