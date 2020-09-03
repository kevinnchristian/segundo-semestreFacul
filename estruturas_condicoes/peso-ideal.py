import math

sexo = input('Informe o sexo da pessoa (M para masculino e F para feminimo): ')
altura = input('Informe a altura da pessoa (Informe usando . ex: 1.70): ')

## Função que calcula peso ideal para homem, baseado na formula informada ##
def pesoHomem(alturaH):
  calc = (72.7 * alturaH) - 58
  return calc

## Função que calcula peso ideal para mulher, baseado na formula informada ##
def pesoMulher(alturaM):
  calc = (62.1 * alturaM) - 44.7
  return calc

## Condição que verifica que tipo de dado entrou e toma a decisão de acordo com mesmo ##
if sexo.upper() == 'M':
    print(math.floor(pesoHomem(eval(altura))))
elif sexo.upper() == 'F':
    print(math.floor(pesoMulher(eval(altura))))
else:
    print('Não foi informado nenhum dado!!!')
