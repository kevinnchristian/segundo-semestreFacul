# Aplicando Memoização na Função Fibonacci criada no outro arquivo
import time

dicionario = dict() 

def fibonacci(n):
  if n <= 1:
    return  n
  elif dicionario.get(n) != None:  
    return dicionario[n]           
  else:                           
    dicionario[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dicionario[n]

start = time.time()
print(fibonacci(10))
print('Recursão com memoização: {} second'.format(time.time() - start))