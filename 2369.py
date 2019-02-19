l = int(input())
price = 7

if(l<=10):
    pass
elif(l<=30):
    price = price + (l-10)*1
elif(l<=100):
    price = price + 20 + (l-30) * 2
else:
    price = price + 160 + (l-100)*5

print (price)