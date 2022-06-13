# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

# valor = int(input("Qual o valor do saque? "))

# # Quantidade de notas de R$ 50
# notas_50 = valor // 50

# # Valor restante a ser sacado com notas menores que R$ 50
# resto_50 = valor % 50

# # Quantidade de notas de R$ 10
# notas_10 = resto_50 // 10

# # Valor restante a ser sacado com notas menores que R$ 50
# resto_10 = resto_50 % 10

# # Quantidade de notas de R$ 2
# notas_2 = resto_10 // 2

# print(int(notas_50))
# print(int(notas_10))
# print(int(notas_2))

# num = int(input())

# milhar = num // 1000
# print(milhar)

# centena = num % 1000 // 100
# print(centena)

# dezena = num % 100 // 10
# print(dezena)

# unidade = num % 10 // 1
# print(unidade)

# print(int(milhar + centena + dezena + unidade))

preco = float(input())
pagamento = float(input())

if preco > pagamento:
	print("Falta {}".format(preco - pagamento)) 
else:
    print("Troco {}".format(pagamento - preco))