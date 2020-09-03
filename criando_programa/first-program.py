nome = 'UNIVESP'
ano = 2020
nomeAluno = input()
registroAluno = int(input())

testeA = eval('len([1, 2, 3])')
testeB = eval('3 + 4')
testeC = eval('3 > 4')

temperaturaCelsius = int(input())
formulaConversao = int(eval('1.8 * temperaturaCelsius + 32')) 

#### Função em Python ####
###### f(x) = x² + 1 #####
def temp(x):
  res = x**2 + 1
  return res

###### Juros #####
def juros(preco, juros):
  res = preco * (1 + (juros / 100))
  return res

print('|----- Primeiro Programa em Python na Facul!!! -----|')
print('|---------------- ',nome, '-', ano, ' -----------------|')
print('')
print('Aluno:', nomeAluno)
print('RA:', registroAluno)
print('')
print(testeA)
print(testeB)
print(testeC)
print('\n')
print('|------------------ Temperatura -------------------|')
print('|------------ Celsius para Fahrenheit -------------|')
print('')
print('Usuário informou: ', temperaturaCelsius,'°C')
print('Temperatura em Fahrenheit: ', formulaConversao,'°F')
print('\n')

print('|--------------------- Função ---------------------|')
print('')
print('Resultado Temperatura: ', temp(2))
print('Resultado Juros: ', juros(10, 50))
print('\n')

help(max) # retorna como usar aquela função, seria uma documentação
help(len) 
help(eval)
