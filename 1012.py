i = list(map(float, input().split()))
print("TRIANGULO: {0:.3f}".format((i[0]*i[2]/2)))
print("CIRCULO: {0:.3f}".format((3.14159*i[2]**2)))
print("TRAPEZIO: {0:.3f}".format(i[2]*(i[0]+i[1])/2))
print("QUADRADO: {0:.3f}".format(i[1]**2))
print("RETANGULO: {0:.3f}".format(i[0]*i[1]))
