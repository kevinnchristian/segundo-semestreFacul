## Listas/Matriz Bidimensional
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(m[0][1])
print(m[1][2])
print(m[2][0])

## Função que verifica se a matriz é simetrica, m = m transposta
def simetrica(matriz):
  num_linhas = len(matriz)
  num_colunas = len(matriz[0])

  for i in range(num_linhas):
    ## i + 1 pq estará acessando a diagonal da matriz
    for j in range(i + 1, num_colunas):
      if matriz[i][j] != matriz[j][i]:
        return False
  
  return True

matrizTeste = [[1, 2, 3], [2, 4, 5], [3, 5, 3]]
matrizTeste2 = [[1, 2, 2], [2, 4, 5], [3, 5, 3]]
print(simetrica(matrizTeste))
print(simetrica(matrizTeste2))
