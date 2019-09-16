testes = int(input())
while testes>0:
    alfabeto = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    frase = input()
    for i in frase:
        for j in alfabeto:
            if (i==j):
                alfabeto.remove(j)
                break
                pass
            pass
        pass
    if(len(alfabeto) == 0):
        print("frase completa")
        pass
    elif(len(alfabeto) <= 13):
        print("frase quase completa")
        pass
    else:
        print("frase mal elaborada")
        pass
    testes -= 1
    pass

