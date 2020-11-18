a,b,c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

if(a>b and a>c):
    maior = a
    elif(b<a and b>c):
        meio = b
        menor = c
elif(b>a and b>c):
    maior = b
    elif(b<a and b>c):
        meio = a
        menor = c
elif(c>a and c>b):
    maior = c
    elif(c>


