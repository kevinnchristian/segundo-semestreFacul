class Pilha():
  def __init__(self):  # Função executada automaticamente ao chamar a classe
    self.data = []

  def push(self, x):  # Inserir um elemento dentro da pilha
    self.data.append(x)

  def pop(self):  # Remove elemento da lista
    if len(self.data) > 0:  # Lista tem que ser maior do que 0
      return self.data.pop(-1)  # Indica para pegar o último elemento da lista

  def top(self):
    if len(self.data) > 0:
      return self.data[-1]  # Consultando o último elemento da lista

  def empty(self):  # Verificar se a lista está vazia
    return not len(self.data) > 0

pilha = Pilha()

pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.push(4)
pilha.push(5)

print(pilha.pop())
print(pilha.pop())

print(pilha.top())

print(pilha.empty())