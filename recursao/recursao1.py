def imprime_rec(myList, i=0):
  if i < len(myList):
    print(myList[i])
    imprime_rec(myList, i+1)
  

myList = [1, 2, 3, 4, 5]
imprime_rec(myList) 