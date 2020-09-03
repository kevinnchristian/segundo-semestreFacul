# Expressões Aritméticas #
print(5 + 2) # int
print(5 - 2) # int
print(5 * 2) # int
print(5 * 2.5) # float
print(5 / 2) # float
print(4 / 2) # float
print(5 // 2) # int
print(4 // 2) # int
print(5 ** 2) # int
print(5 % 2) # int

print(abs(-2)) # retorna o valor absoluto de número
print(min(1, 3, 5, 7)) # retorna o valor mínimo entre os números
print(max(1, 3, 5, 7)) # retorna o valor máximo entre os números

# Calcular a média harmônica dos números: 3.6, 8.9, 10 #
print((3) / ((1 / 3.6) + (1 / 8.9) + (1 / 10)))

# Calcular a média harmônica amortizada dos números: 3.6, 8.9, 10. Para x=4 #
x = 4
print(((3) / ((1 / 3.6 + x) + (1 / 8.9 + x) + (1 / 10 + x))) - x)

# Expressões Lógicas #
print(5 == 5) # retorna True
print(2 + 1 >= 3) # retorna True
print(13 % 10 != 3) # retorna False
print(1 > 3 or 1 + 3 > 2) # retorna True
print(1 > 3 and 1 + 3 > 2) # retorna False
print(not 1 > 3 and 1 + 3 > 2) # retorna True, por causa do not negando oq vem na frente
print(4 in [1, 4, 5, 6]) # retorna True pq a lista contém o 4
print(5 not in [1, 4, 5, 6]) # retorna False pq a lista contém o 5
print(4 is not 1) # retorna True pq quatro não é 1
print(5.0 is int(5)) # retorna False pq 5.0 é do tipo float
