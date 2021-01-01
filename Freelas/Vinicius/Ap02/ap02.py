'''
Ap 02

'''

qtdAlunos = int(input())
nomesAlunos = []
nota01 = []
nota02 = []
mediaAluno = []

for i in range(qtdAlunos):
  nomesAlunos.append(input())
  nota01.append(float(input()))
  nota02.append(float(input()))

  media = (nota01[i] + nota02[i])/2
  mediaAluno.append(media)
  

  



