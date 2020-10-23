# Definindo uma classe
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
  
  # Criar representação inicial, para ele não mostrar como na primeira instância do objeto:
  # <__main__.Point object at 0x7f59f2991220>
  def __repr__(self):
    return '(' + str(self.x) + ',' + str (self.y) + ')'

p1 = Point()
p2 = Point(10, 10)
print(p1)
print(p2)

p1.setx(5)
p1.sety(3)
p2.setx(20)
p2.sety(20)
print(p1.get())
print(p2.get())

p1.move(10, 8)
p2.move(30, 30)
print(p1.get())
print(p2.get())