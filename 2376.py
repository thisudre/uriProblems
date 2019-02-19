equipes = "A B C D E F G H I J K L M N O P".split()
for i in range(15):
    # equipes jogando = (i*2-i) e (i*2-i+1)
    jogo = input().split()
    if(jogo[0]>jogo[1]):
        equipes.pop(i*2-i+1)
    else:
        equipes.pop(i*2-i)

print(equipes[0])