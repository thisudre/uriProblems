def contar_linhas(texto, carac_linha):
    linhas = 1
    array = texto.split(" ")
    tam_linha = len(array[0])
    for i in (array[1:]):
        nova_palavra = i
        if(tam_linha + len(nova_palavra) + 1 > carac_linha):
            tam_linha = len(nova_palavra)
            linhas += 1
            pass
        else:
            tam_linha += len(nova_palavra) + 1
            pass
        pass
    return linhas

while(True):
    try:
        entry = list(map(int, input().split()))
        qtd_palavras = entry[0]
        qtd_linhas = entry[1]
        qtd_carac = entry[2]
        
        texto = input()
        linhas = contar_linhas(texto, qtd_carac)
        paginas = int(linhas/qtd_linhas)
        if(linhas % qtd_linhas != 0):
            paginas += 1
            pass
        print(paginas)
        pass
    except EOFError:
        break
