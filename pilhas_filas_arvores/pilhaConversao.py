# Convertendo de decimal para binário
class Pilha():
  def __init__(self):
    self.data = []

  def push(self, x):
    self.data.append(x)

  def pop(self): 
    if len(self.data) > 0:  
      return self.data.pop(-1) 

  def top(self):
    if len(self.data) > 0:
      return self.data[-1]

  def empty(self): 
    return not len(self.data) > 0

pilha = Pilha()
numeroConversao = int(input('Insira o número para conversão: '))

while numeroConversao > 0:
  resto = numeroConversao % 2
  numeroConversao = numeroConversao // 2  # Pegando o novo consciente para fazer divisão
  pilha.push(resto)

while not pilha.empty():
  print(pilha.pop())
