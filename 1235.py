testes = int(input())
while(testes > 0):
    string = input()
    string_final = []
    for i in range(int(len(string)/2)-1, -1, -1):
        string_final.append(string[i])
        pass
    for i in range(len(string)-1, int(len(string)/2)-1, -1):
        string_final.append(string[i])
        pass
    print(''.join(string_final))
    testes -= 1
