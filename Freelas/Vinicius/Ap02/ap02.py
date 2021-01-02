import math
def ordenar(listaNomes): 
    tamanhoLista = len(listaNomes) 
    for i in range(tamanhoLista-1): 
        for j in range(0, tamanhoLista-i-1): 
            if listaNomes[j] > listaNomes[j+1] : 
                listaNomes[j], listaNomes[j+1] = listaNomes[j+1], listaNomes[j] 

qtdAlunos = int(input())
listaNome = []
nota01 = []
nota02 = []
media = []
somatorioMedia = 0

mediaPessoa = 0

for i in range(qtdAlunos):
  listaNome.append(input())
  nota01.append(float(input()))
  nota02.append(float(input()))
  mediaPessoa = (nota01[i] + nota02[i])/2
  media.append(mediaPessoa)
  somatorioMedia += media[i]

  mediaPessoa = 0
  

dicionario = {}

for i in range(len(listaNome)):
  dicionario.update({listaNome[i]: media[i]})


mediaTurma = somatorioMedia/qtdAlunos

listMaiores = {}
contador = 0
for i in range(len(listaNome)):
  if dicionario[listaNome[i]] >= mediaTurma:
    listMaiores.update({listaNome[i]: media[i]})
    contador += 1





lista3 = []
for i in listMaiores:
    lista3.append(listMaiores[i])



ordenar(listaNome)



for i in range(len(listaNome)): 
  print (listaNome[i])
  print("{:.1f}".format(dicionario[listaNome[i]]))

print(contador)

ordenar(lista3)

lista3 = lista3[::-1]

porDez = len(listaNome) * 0.10
porDez = math.ceil(porDez)
listaNomesRodados = [""]
c = 0
for j in lista3:
  for i in listMaiores:
    if( c >= porDez):
      break
    elif (j == listMaiores[i]):
      for k in range(len(listaNomesRodados)):
        if i in listaNomesRodados:
          listaNomesRodados.append(i)
        else:
          print(i)
      
      c+=1

