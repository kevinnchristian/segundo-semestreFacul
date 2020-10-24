# Aplicando Memoização na Função Fatorial criada no outro arquivo
import time

dicionario = dict()   # dict é uma estrutura de dicionário, onde dentro dele
                      # conseguimos armazenar chave e valor

def fatorial(n):
  if n == 0:
    return  1
  elif dicionario.get(n) != None:  # Ele verifica se tal posição no dicionário
    return dicionario[n]           # está ocupada, se sim ele retorna o valor da mesma,
  else:                            # se não ele cai nesse else abaixo, que atribui um valor para a posição vazia
    dicionario[n] = n * fatorial(n-1)
    return dicionario[n]

start = time.time()
print(fatorial(10))
print('Recursão com memoização: {} second'.format(time.time() - start))