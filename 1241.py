testes = int(input())
while (testes > 0):
    numeros = input().split()
    num1, num2 = numeros[0], numeros[1]
    if(len(num1)>= len(num2)):
        if(num1[len(num1)-len(num2):] == num2[:]):
            print("encaixa")
            pass
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")
    testes -= 1
