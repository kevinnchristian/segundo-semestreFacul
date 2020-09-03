import math

nome_aluno = input('Informe o nome do aluno: ')
nota1 = input('Informe a nota de numero 1: ')
nota2 = input('Informe a nota de numero 2: ')

## Função que calcula nota média ##
def calcMedia(nota1, nota2):
  calc = (0.4 * eval(nota1)) + (0.6 * eval(nota2))
  return math.ceil(calc)

media = calcMedia(nota1, nota2)

## Condição que verifica se o aluno está aprovado ou não, media para ser aprovado é 5.0 ##
if media >= 5.0:
  print('Aluno(a) ', nome_aluno,' está aprovado! Com a média:', media)
else:
  print('Aluno(a)', nome_aluno,'está reprovado! Com a média:', media)