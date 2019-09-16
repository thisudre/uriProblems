
while(True):
    entry = input().split()
    if(entry == ["0", "0"]):
        break
        pass
    else:
        erro, numero = entry[0], list(entry[1])
        while(erro in numero):
            numero.remove(erro)
            pass
        while(True):
            if(len(numero) > 0):

                if(numero[0]=="0"):
                    numero.pop(0)
                    pass
                else:
                    break
                    pass
                pass
            else:
                break
                pass
            pass
        if(len(numero)==0):
            numero = ["0"]
        print("".join(numero))
