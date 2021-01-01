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

# Main
qtdNumeros = int(input())
listaNumeros = []
totPar = 0
totImpar = 0
totPrimo = 0
soma = 0
somaQuadrados = 0
maiorNumero = 0
menorNumero = 10000000000


for i in range(qtdNumeros):
  listaNumeros.append(int(input()))

for i in listaNumeros:
  result = ""
  if parImpar(i) == 1:
    result += "Par"
    totPar += 1
  else:
    result += "Impar"
    totImpar +=1
  if primo(i) == 1:
    result += " Primo"
    totPrimo += 1
  result += " " + str(quadrado(i))
  result += " " + str(fatorial(i))

  soma += i
  somaQuadrados += quadrado(i)

  if i > maiorNumero:
    maiorNumero = i
  if i < menorNumero:
    menorNumero = i

  #Parte 2

  print(result)

mediaAri = soma/qtdNumeros

print(totPar)
print(totImpar)
print(totPrimo)
print("{:.2f}".format(mediaAri))
print(somaQuadrados)
print(maiorNumero)
print(menorNumero)
  

  

