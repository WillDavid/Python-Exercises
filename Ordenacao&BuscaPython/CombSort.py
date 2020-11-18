def combsort(lista):
  salto = len(lista)
  troca = True

  while salto > 1 or troca == True:
    salto = max(1, int(salto / 1.3))   
    troca = False
    for i in range(len(lista) - salto):
      j = i+salto
      if lista[i] > lista[j]:
        lista[i], lista[j] = lista[j], lista[i]
        troca = True

lista = [2,9,3,6,7,12,5,8,4,11]
print(lista)
combsort(lista)
print(lista)