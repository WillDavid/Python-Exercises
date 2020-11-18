#Erika 2
#Selection Sort

def pesquisaBinaria(lista, item):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return 1
        elif lista[meio] > item:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1

def selectionSort(lista):
  for i in range(len(lista)):
    j = i + 1
    menor = i
    while (j < len(lista)):
      if (lista[j] < lista[menor]):
        menor = j
      j = j + 1
    lista[i], lista[menor] = lista[menor], lista[i]
   

lista = [40,10,20,60,84,-5] 

x = 84 #Valor que vai ser buscado na lista
print("Lista não ordenada: ", lista)

selectionSort(lista)

print("Lista ordenada: ", lista)

print("Valor para buscar na lista: ", x)
if (pesquisaBinaria(lista, x) == 1):
  print("Achou o valor", x)
else:
  print("Não achou o valor", x)