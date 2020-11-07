def intercala(v, ini, meio, fim):
  L = v[ini:meio+1]  # Variavel aux, que ajuda com um sub-vetor
  R = v[meio+1:fim+1]   # Variavel aux, que ajuda com um sub-vetor
  L.append(999)  # Valor sentinela, valor máximo para o elemento do vetor ele nunca podera passar desse valor. Ajuda no incremento de i e j, assim ele não incrementa mais do que deve
  R.append(999)  # Valor sentinela, valor máximo para o elemento do vetor ele nunca podera passar desse valor. Ajuda no incremento de i e j, assim ele não incrementa mais do que deve
  i = 0  # Indice
  j = 0  # Indice
  for k in range(ini, fim+1):
    if L[i] <= R[j]:
      v[k] = L[i]
      i += 1
    else:
      v[k] = R[j]
      j += 1

def merge_sort(v, ini, fim):  # Vetor, Inicio do Vetor, Fim do Vetor
  if ini < fim:  
    meio = (ini + fim) // 2  # Divindo o vetor no meio
    merge_sort(v, ini, meio)  # Fazendo recursão do inicio ao meio
    merge_sort(v, meio + 1, fim)  # Fazendo recursão do meio ao fim
    intercala(v, ini, meio, fim)  # 



vetor = [2, 48, 65, 70, 8, 10, 50, 30, 25, 6]

print('Vetor antes:', vetor)
print('-----------------------------------------------------------')
merge_sort(vetor, 0, len(vetor) - 1)
print('Vetor depois:', vetor)