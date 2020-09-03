# Exemplo de Lista #
pets = ['cão', 'gato', 'peixe']
listaExemplo = [1, 'ab', [], [1,2]]
print(pets)
print(listaExemplo)

# Acessar um elemento da lista pelo indice #
print(pets[1])
print(listaExemplo[3])
print(listaExemplo[3][0])

# Exemplos de utilização de métodos em lista #
print(pets.count('cão'))
print(pets.index('cão'))

pets.insert(3, 'passarinho')
print(pets)

pets.pop()
print(pets)

pets.remove('peixe')
print(pets)

pets.reverse()
print(pets)

pets.sort()
print(pets)


# Exemplo de Tupla #
dias = ('seg','ter','qua')
print(dias)
print(dias[0])