cidades = []
estradas = []
estrada_base = {"C1":0, "C2":0, "Size":0}

a = input().split()
while len(cidades)<int(a[0]):
    cidades.append()
    pass

while estradas<int(a[1]):
    a = input().split()
    new_estrada = estrada_base.copy()
    new_estrada["C1"] = int(a[0])
    
    pass