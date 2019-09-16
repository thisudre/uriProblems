testes = int(input())
while (testes > 0):
    strings = input().split()
    string1 = strings[0]
    string2 = strings[1]
    string3 = []
    for i in range(len(string1)):
        string3.append(string1[i])
        if(i < len(string2)):
            string3.append(string2[i])
        pass
    if(i < len(string2)):
        string3.append(string2[i+1:])
        pass
    print("".join(string3))
    testes -= 1
