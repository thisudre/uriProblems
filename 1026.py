while(True):
    try:
        numeros = list(map(int, input().split()))
        print(numeros[0]^numeros[1])
        pass
    except EOFError:
        break
