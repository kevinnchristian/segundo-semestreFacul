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

fila = Fila()

fila.inserir(1)
fila.inserir(2)
fila.inserir(3)
fila.inserir(4)
fila.inserir(5)

print(fila.remover())
print(fila.remover())
print(fila.remover())
print(fila.remover())

print(fila.empty())
print(fila.remover())
print(fila.empty())