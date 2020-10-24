# Função recursiva para calcular fatorial de número
def fatorial(n):
  if n == 0:
    return 1
  else:
    resultado = n * fatorial(n-1)  # recursão sendo aplicada, chamamos a função
    return resultado               # fatorial dentro dela mesmo de forma natural

print(fatorial(4))