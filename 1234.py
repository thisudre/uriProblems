while (True):
    try:
        sentenca = input()
        s_dancante = []
        ultima_letra = 'a'
        for caracter in sentenca:
            if(caracter == " "):
                s_dancante.append(" ")
                pass
            elif(ultima_letra.islower()):
                s_dancante.append(caracter.upper())
                ultima_letra = caracter.upper()
                pass
            elif(ultima_letra.isupper()):
                s_dancante.append(caracter.lower())
                ultima_letra = caracter.lower()
                pass
            pass
        print(''.join(s_dancante))
    except EOFError:
        break
