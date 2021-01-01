'''
Ap01 - Questão 01

'''

def parImpar(i):
  if i%2 == 0:
    return 1
  else:
    return 0

def primo(i):
    if i < 2:
        return 0
    else:
        for j in range(2, i):
            if i % j == 0:
               return 0
        return 1

def fatorial(i):
  fat = 1
  j = 2
  while j <= i:
    fat *= j
    j +=1
  return fat

def quadrado(i):
  return i**2

qtdNumeros = int(input())
listaNumeros = []

for i in range(qtdNumeros):
  listaNumeros.append(int(input()))

for i in listaNumeros:
  if(primo(i) == 1):
    print("Primo")
  print(fatorial(i))
