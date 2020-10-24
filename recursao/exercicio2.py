#Exercicio de retornar soma dos numero da lista
def sumNumberList(myList):
  if len(myList) == 0:
    return 'A lista não possui valores.'
  elif len(myList) == 1:
    return myList[0]
  else:
    return myList[0] + sumNumberList(myList[1:])

lista = [100, 200, 300, 400]

print(sumNumberList(lista))