def insertion_sort(v):
  for i in range(1, len(v)):  # percorrer o vetor da posição 1 até o tamanho dele total
    elemento = v[i]  # recebe o segundo elemento, elemento que quero inserir na minha lista
    indice = i - 1  # comparação com elemento, posição anterior
    while indice >= 0 and elemento < v[indice]:  # enquanto indice for >= 0 e elemento < v[indice]
      v[indice + 1] = v[indice]  # troca o indice de posição
      indice -= 1 # decrementa o indice, pois aquele elemento assumiu sua devida posição
    v[indice + 1] = elemento  # após o enquanto terminar, inserimos o elemento na posição correta
    
vetor = [2, 48, 65, 70, 8, 10, 50, 30, 25, 6]

print('Vetor antes:', vetor)
print('-----------------------------------------------------------')
insertion_sort(vetor)
print('Vetor depois:', vetor)