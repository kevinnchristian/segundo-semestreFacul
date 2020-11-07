def quick_sort(v, ini, fim): 
  meio = (ini + fim) // 2  # Dividi o vetor em dois
  pivo = v[meio]  # Armazena o indice do meio do vetor
  i = ini  # Ponteiro do primeiro sub-vetor
  j = fim  # Ponteiro do segundo sub-vetor
  while i < j:
    while v[i] < pivo:  # Enquanto i for menor que meio, incrementa i até que seja igual a meio
      i += 1
    while v[j] > pivo:  # Enquanto j for maior que meio, incrementa j até que seja igual a meio
      j -= 1  
    if i <= j:
      v[i], v[j] = v[j], v[i]  # Troca/Cruza i e j, caso i seja <= j
    i += 1
    j -= 1
  if j > ini:
    quick_sort(v, ini, j)  # Chama recursão
  if i < fim:  
    quick_sort(v, i, fim)  # Chama recursão

vetor = [2, 48, 65, 70, 8, 10, 50, 30, 25, 6]

print('Vetor antes:', vetor)
print('-----------------------------------------------------------')
quick_sort(vetor, 0, len(vetor) - 1)
print('Vetor depois:', vetor)