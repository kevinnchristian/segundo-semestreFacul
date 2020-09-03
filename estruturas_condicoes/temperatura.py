temperatura = eval(input('Informe a temperatura atual: '))

## Função que verifica a temperatura ##
def identificarTemp(temp):
  if temp >= 32 and temp < 86:
    print('Está Frio!!!')
  elif temp >= 86:
    print('Está Quente!!!')
  else:
    print('Está Congelando!!!')

identificarTemp(temperatura)