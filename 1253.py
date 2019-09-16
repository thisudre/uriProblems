alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def obter_letra(casas, letra):
    numero_letra = 0
    for i in range(len(alfabeto)):
        if (alfabeto[i] == letra):
            numero_letra = i
            break
    numero_letra_nova = numero_letra - casas
    if (numero_letra_nova < 0):
        numero_letra_nova += len(alfabeto)
    return alfabeto[numero_letra_nova]

testes = int(input())
while testes>0:
    palavra = input()
    casas = int(input())
    nova_palavra = []
    for i in palavra:
        nova_palavra.append(obter_letra(casas, i))
    
    print(''.join(nova_palavra))
    testes -= 1
    
