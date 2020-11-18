lista = []
verificador =  False
i = 0
while (verificador != True):
  x = float(input("Informe o numero (Digite 0 para parar)"))
  if x != 0:
    lista.append(x)
  else:
    verificador = True
while i < len(lista):
  j = i + 1
  while j < len(lista):
    if lista[j] == lista[i]:
      del(lista[j])
    else:
      j = j + 1
  i = i + 1
for i in lista:
  print(i)