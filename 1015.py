p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))
print("{0:.4f}".format(((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)))
