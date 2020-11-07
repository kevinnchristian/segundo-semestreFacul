def busca_binaria(lista, elementoX, inicio, fim):
  meio = (inicio + fim) // 2

  if fim < inicio:  # Para o caso de não encontrar elemento
    return -1

  if elementoX == lista[meio]:
    return meio

  if elementoX < lista[meio]:
    return busca_binaria(lista, elementoX, inicio, meio - 1)

  if elementoX > lista[meio]:
    return busca_binaria(lista, elementoX, meio + 1, fim)
  
elemento1 = 6
elemento2 = 12
elemento3 = 18
elemento4 = 99

vetor = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print('Posição do Elemento:', busca_binaria(vetor, elemento1, 0, len(vetor) - 1))
print('------------------------------------------------')

print('Posição do Elemento:', busca_binaria(vetor, elemento2, 0, len(vetor) - 1))
print('------------------------------------------------')

print('Posição do Elemento:', busca_binaria(vetor, elemento3, 0, len(vetor) - 1))
print('------------------------------------------------')

print('Posição do Elemento:', busca_binaria(vetor, elemento4, 0, len(vetor) - 1))
print('------------------------------------------------')