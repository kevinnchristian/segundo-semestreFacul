class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  
  def setx(self, x):
    self.x = x

  def sety(self, y):
    self.y = y
  
  def get(self):
    return self.x, self.y
  
  def move(self, offsetX, offsetY):
    self.x += offsetX
    self.y += offsetY
  
  def __repr__(self):
    return '(' + str(self.x) + ',' + str (self.y) + ')'
  
  # Essa função será usada quando tivermos usando o operador + (como vimos __add__ )
  # Esse método pertece a classe int.__add__, essa classe é instanciada 
  # quando por exemplo definimos uma variável x = valorX_inteiro
  def __add__(self, other):  # other é parametro para o segundo operando
    if type(other) == Point:
      return Point(self.x + other.x, self.y + other.y)
    else:
      return Point(self.x + other, self.y + other)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1)
print(p2)

# Somando dois objetos Point
print(p1 + p2)  # como temos o operador + dispara a função __add__

# Somando objeto Point + valorX_inteiro_ou_float
print(p1 + 10)
print(p2 + 5.5)