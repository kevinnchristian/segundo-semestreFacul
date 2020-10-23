import random

class MyList(list):   # list é a classe base que vamos herda
  def choice(self):
    return random.choice(self)

# usando classe list normal que herdamos
l1 = MyList([1, 2, 3, 4])
print(l1)

# usando método criado pela nossa função choice dentro da classe MyList
print(l1.choice())  # choice retorna de forma aleátoria elementos que contém na lista