led_painel = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
testes = int(input())
while (testes>0):
    qtd_leds = 0
    numero = input()
    for i in numero:
        qtd_leds += led_painel[int(i)]
        pass
    print ("{:d} leds".format(qtd_leds))
    testes -= 1
    pass

