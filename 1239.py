while(True):
    try:
        texto = list(input())
        i, b = False, False
        for n in range(len(texto)):
            if(texto[n] == '*' and not b):
                texto[n] = "<b>"
                b = True
                pass
            if(texto[n] == '*' and b):
                texto[n] = "</b>"
                b = False
                pass
            if(texto[n] == '_' and not i):
                texto[n] = "<i>"
                i = True
                pass
            if(texto[n] == '_' and i):
                texto[n] = "</i>"
                i = False
                pass
            pass
        print("".join(texto))
        pass
    except EOFError:
        break
