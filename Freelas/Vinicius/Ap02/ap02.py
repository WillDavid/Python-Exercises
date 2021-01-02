'''
Ap 02

'''

def ordenar(listaNomes): 
    tamanhoLista = len(listaNomes) 
    for i in range(tamanhoLista-1): 
        for j in range(0, tamanhoLista-i-1): 
            if listaNomes[j] > listaNomes[j+1] : 
                listaNomes[j], listaNomes[j+1] = listaNomes[j+1], listaNomes[j] 

qtdAlunos = int(input())
nomesAlunos = []
nota01 = []
nota02 = []
mediaAluno = []
dicionario = {}

for i in range(qtdAlunos):
  nomesAlunos.append(input())
  nota01.append(float(input()))
  nota02.append(float(input()))

  media = (nota01[i] + nota02[i])/2
  mediaAluno.append(media)


for i in range(len(nomesAlunos)):
  dicionario.update({nomesAlunos[i]: mediaAluno[i]})


ordenar(nomesAlunos)

for i in range(len(nomesAlunos)): 
    print (nomesAlunos[i])
    print(dicionario[nomesAlunos[i]])






