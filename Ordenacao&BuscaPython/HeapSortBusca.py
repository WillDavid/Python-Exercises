'''
Bloco de estudos - Heap Sort
Heap Sort simula uma árvore binária completa
Cada elemento "pai" do vetor possui dois "filhos"

Como funciona a localização dos filhos?
Pai será sempre (i)
filho da esquerda = (2*i+1)
filho da direita = (2*i+2)


'''
def heapify(lista, tamanhoLista, i): 
    raiz = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2 

    if (esquerda < tamanhoLista and lista[i] < lista[esquerda]): 
        raiz = esquerda 

    if (direita < tamanhoLista and lista[raiz] < lista[direita]): 
        raiz = direita 

    if (raiz != i): 
        lista[i],lista[raiz] = lista[raiz],lista[i]
  
        heapify(lista, tamanhoLista, raiz) 
  
def heapSort(lista): 
    tamanhoLista = len(lista) 

    for i in range(tamanhoLista, -1, -1): 
        heapify(lista, tamanhoLista, i) 

    for i in range(tamanhoLista-1, 0, -1): 
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0) 


## Só funciona se o vetor estiver ordenado
def buscaBinaria(lista, item):
  primeiro = 0
  ultimo = len(lista)-1
  encontrado = False
  while (primeiro <= ultimo and encontrado == False):
    meio = (primeiro + ultimo)//2
    if lista[meio] == item:
      encontrado = True
      return encontrado
    else:
      if item < lista[meio]:
        ultimo = meio - 1
      else:
        primeiro = meio + 1

  return encontrado
#Lista não ordenada
lista = [1,2,3,14,11,6,8,9,10]
item = 10
heapSort(lista)
print("Lista ordenada: ", lista)


if buscaBinaria(lista, item):
  print("O valor {} foi encontado".format(item))
else:
  print("O valor {} não foi encontado".format(item))