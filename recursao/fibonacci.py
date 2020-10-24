# n-ésimo termo da sequência de Fibonacci
import time

# Versão com recursão
def fibonacci_rec(n):
  if n <= 1:
    return n
  else:
    resultado = (fibonacci_rec(n - 1) + fibonacci_rec(n - 2))
    return resultado 

def fibonacci_it(n):
  resultado = n
  posicaoA, posicaoB = 0, 1
  for i in range(2, n+1):
    resultado = posicaoA + posicaoB
    posicaoA, posicaoB = posicaoB, resultado
  return resultado 


start = time.time()
print(fibonacci_rec(30))
print('Recursão: {} second'.format(time.time() - start))
start = time.time() 
print(fibonacci_it(30))
print('Iterativo: {} second'.format(time.time() - start))