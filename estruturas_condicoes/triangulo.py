triangulo1 = 'Equilátero'  # 3 lados iguais
triangulo2 = 'Isósceles'   # 2 lados iguais, 1 lado diferente
triangulo3 = 'Escaleno'    # 3 lados diferentes

## Considerando que o triângulo tenha 3 lados: ##
ladoA = eval(input('Informe o lado A do triângulo: '))
ladoB = eval(input('Informe o lado B do triângulo: '))
ladoC = eval(input('Informe o lado C do triângulo: '))


## Condições que verifica qual é o maior lado ##
'''maior_lado = 0
if ladoA > maior_lado:
  maior_lado = ladoA
if ladoB > maior_lado:
  maior_lado = ladoB
if ladoC > maior_lado:
  maior_lado = ladoC'''

## Ou podemos utilizar uma função nativa do python que pega o maior entre os valores ##
maior_lado = max(ladoA, ladoB, ladoC)

## Condição que verifica qual tipo de triângulo temos, conforme os valores de entrada ##
## Caso maior_lado seja < que a soma dos os dois temos uma triângulo ##
if maior_lado < (ladoA + ladoB + ladoC - maior_lado):
  print('Os lados formam um triângulo!')
  if ladoA == ladoB and ladoB == ladoC and ladoC == ladoA:
    print('Temos um triângulo:', triangulo1)
  elif ladoA != ladoB and ladoB != ladoC and ladoC != ladoA:
    print('Temos um triângulo:', triangulo3)
  else:
    print('Temos um triângulo:', triangulo2)
else:
  print('Os lados não formam um triângulo!')