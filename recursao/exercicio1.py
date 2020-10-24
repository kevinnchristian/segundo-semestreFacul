#Exercicio de retornar maior numero da lista
def numberBigger(myList):
  if len(myList) == 0:
    return 'A lista não possui valores.'
  elif len(myList) == 1:
    return myList[0]

  number = numberBigger(myList[1:])
  if myList[0] > number:
    number = myList[0]

  return number

myList = [50, 1000, 830, 400]

print(numberBigger(myList))