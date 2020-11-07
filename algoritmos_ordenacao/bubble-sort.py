def bubble_sort(v):
  for i in range(len(v) - 1):  # percorre os passos no conjunto -1
    for j in range(len(v) - i - 1):  # percorre os pares do conjunto, do primeiro elemento ao penúltimo
      if (v[j] > v[j + 1]):  # faz a comparação entre os elementos, comparando se o elemento da esquerda é maior do que o da direita
        v[j], v[j + 1] = v[j + 1], v[j]  # se a condição for verdadeira, troca os elementos de posição 

vetor = [25, 50, 2, 30, 10, 8, 60, 42, 56, 90, 80]

print('Vetor antes:', vetor)
print('-----------------------------------------------------------')
bubble_sort(vetor)
print('Vetor depois:', vetor)