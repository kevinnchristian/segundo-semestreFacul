# Gerenciamento de 2 filas do banco

# Se idade >= 60 entra na fila preferencial
# E cada 2 pessoas que saem da fila preferencial, 1 pessoa sai da fila normal.

class Fila():
  def __init__(self):
    self.data = []
  
  def inserir(self, x):
    self.data.append(x)

  def remover(self):
    if len(self.data) > 0:
      return self.data.pop(0)

  def top(self):
    if len(self.data) > 0:
      return self.data[0]
  
  def empty(self):
    return not len(self.data) > 0


filaNormal = Fila()
filaPreferencial = Fila()

pessoasIdade = [20, 30, 40, 85, 60, 65, 70, 72, 38, 59, 75, 80]

# Função faz controle da fila
def controleFila(fila1, fila2):
  if len(fila1.data) >= 2:
    fila1.remover()
    fila1.remover()
    fila2.remover()
    print('Fila Preferencial:')
    print(fila1.data)
    print('---------------------')
    print('Fila Normal:')
    print(fila2.data)
    print('')
    print('')
  else: 
    fila1.remover()
    fila2.remover()
    print('Fila Preferencial:')
    print(fila1.data)
    print('---------------------')
    print('Fila Normal:')
    print(fila2.data)
    print('')
    print('')

# Percorre o array de pessoas com suas idades, fazendo seletiva para fila
# de acordo com a idade de cada uma
for i in range(len(pessoasIdade)):
  if pessoasIdade[i] >= 60:
    filaPreferencial.inserir(pessoasIdade[i])
  else:
    filaNormal.inserir(pessoasIdade[i])

print('Fila Preferencial:')
print(filaPreferencial.data)
print('---------------------')
print('Fila Normal:')
print(filaNormal.data)
print('')
print('')

controleFila(filaPreferencial, filaNormal)
controleFila(filaPreferencial, filaNormal)
controleFila(filaPreferencial, filaNormal)
controleFila(filaPreferencial, filaNormal)