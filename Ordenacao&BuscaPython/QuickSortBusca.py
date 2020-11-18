def particao(lista, inicio, fim): 
    i = ( inicio - 1 ) 
    x = lista[fim] 
    for j in range(inicio, fim): 
        if (lista[j] <= x):
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i] 
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1] 
    return (i + 1) 

def quickSort(lista, inicio, fim):
  lista2 = []
  lista2.append((inicio, fim))
  
  while lista2:
    inicio, fim = lista2.pop()
    pivot = particao(lista, inicio, fim)
    if (pivot - 1 > inicio):
      lista2.append((inicio, pivot - 1))
    if (pivot + 1 < fim):
      lista2.append((pivot + 1, fim))


def buscaBinaria(lista, chave, primeiro, ultimo, verificador):
  while (primeiro <= ultimo):
    meio = (primeiro + ultimo)//2
    if lista[meio] < chave:
      primeiro = meio + 1
    elif lista[meio] > chave:
      ultimo = meio - 1
    elif lista[meio] == chave:
      verificador = True
      return verificador
  return verificador


  

lista = [5,11,9,10,33,1,45,-4]
inicio = 0
fim = len(lista) - 1

print(lista)
quickSort(lista, inicio, fim)
print(lista)

lista2 = [3,4,5]



primeiro = 0
ultimo = len(lista) - 1
chave =  int(input("Qual valor você quer encontrar? "))
verificador = False


encontraChave = buscaBinaria(lista,chave,primeiro,ultimo, verificador)
if (encontraChave == True):
  print("Valor encontrado")
else:
  print("Valor não encontrado")


