numeros = []
x = int(input("Informe a quantidade de numeros: "))
for i in range(x):
  numero = float(input("Informe um número real: "))
  numeros.append(numero)

lista = []
for i in numeros:
  if i not in lista:
    lista.append(i)

print("Lista Ordenada: ", lista)
