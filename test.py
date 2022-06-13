
###########Exercicio 1#####################################################################################


# altura = float(input('Digite a altura da fachada '))
# comprimento = float(input('Digite o comprimento, em metros da fachada '))
# pintura = float(input('Digite o valor da pintura por metro quadrado '))

# x = altura * comprimento * pintura

# print(round(x, 2))

###########Exercicio 2#####################################################################################


# sacar = int(input())

# if sacar > 100:
#     saqueCem = sacar // 100
#     print(saqueCem)
# elif saqueCem == 0:
#     saqueCem %

###########Exercicio 4#####################################################################################

# import math

# raio = float(input())
# area = math.pi * raio**2

# print (round(area, 2))

# volume = 4/3 * math.pi * raio**3

# print (round(volume, 2))

###########Exercicio 5#####################################################################################

# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

# Constantes fornecidas pelo enunciado:
# comprimento = 12
# altura = 3
# material = 100

# # Leitura do servico de pintura
# servico = float(input("Qual o custo do serviço? "))

# # Calculo do custo
# custo = servico * (comprimento * altura) + material

# # Impressao do resultado
# print(round(custo, 2))

###########Exercicio 6#####################################################################################
# numeros = input()

# if (numeros < 1000):
#     print('Digite um número de 4 digitos')
# elif (numeros > 9999):
#     print('Digite um número de 4 digitos')
# else:
#     print(sum(int(i) for i in n))

###########Exercicio 7#####################################################################################

# vendas = float(input('Total de vendas:'))
# lucro = vendas * 30/100

# print(round(lucro,2))

###########Exercicio 8#####################################################################################

# comprado = float(input('Comprado: '))
# ficara = comprado * 1/3

# print(round(ficara,3))

###########Exercicio 9#####################################################################################
# import math

# hpMonstro = int(input())
# d1 = int(input())
# d2 = int(input())

# pi = math.pi

# raiz = math.sqrt(5 * d1)
# dano = int(raiz + pi ** (d2/3))
# print(hpMonstro - dano)

###########Exercicio 9#####################################################################################

# nota1 = int(input())
# peso1 = int(1)

# nota2 = int(input())
# peso2 = int(2)

# nota3 = int(input())
# peso3 = int(3)

# nota4 = int(input())
# peso4 = int(4)

# media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / (peso1 + peso2 + peso3 + peso4)
# print (float((round(media, 3))))

###########Exercicio 13#####################################################################################

# spc = int(input())
# tmp = int(input())

# if 1 <= spc <= 500:
#      print()
# else:
#      print('Digite um número maior que 1 e menor que 500!')

# if 1 <= tmp <= 100:
#      print()
# else:
#      print('Digite um número maior que 1 e menor que 100!')

# vel = (spc / tmp)
# print(int(vel))

###########Exercicio 14#####################################################################################

# entradaA = int(input())
# entradaB = int(input())
# entradaC = int(input())
# entradaD = int(input())
# entradaE = int(input())
# inimigos = entradaA - (entradaB + entradaC + entradaD + entradaE) 

# if (entradaA or entradaB or entradaC or entradaD or entradaE) > 1000:
#      print('Digite novas entradas menores que 1000')
#      entradaA = int(input())
#      entradaB = int(input())
#      entradaC = int(input())
#      entradaD = int(input())
#      entradaE = int(input())
# elif (entradaB + entradaC + entradaD + entradaE ) > entradaA:
#      print('Os valores das Entradas B,C,D e E não podem ser superiores a Entrada A')
# else:
#      print(int(inimigos))


# num = int(input())


# if num <= 99:
     
#      print('O numero deve conter três algarismos ')
#      primeiro = (input())
#      segundo = (input())
#      terceiro = (input())
# elif num >= 1000 :
#      print('O numero deve conter três algarismos ')
#      primeiro = (input())
#      segundo = (input())
#      terceiro = (input())
# else:
#      print(num)


# import math

# enxA = float(input())
# enyA = float(input())
# enxB = float(input())
# enyB = float(input())


# equacao = (enxB - enxA)**2 + (enyB - enyA)**2
# dAB = math.sqrt(equacao)

# print(round(dAB, 3))

# peso = float(input('Digite o seu peso: '))
# altura = float(input('Digite a sua altura: '))

# imc = peso / altura**2
# print(round(imc, 2))

# cordXA = float(input())
# cordYA = float(input())
# cordXB = float(input())
# cordYB = float(input())

# xM = (cordXB + cordXA) / 2
# yM = (cordYB + cordYA) / 2

# print(round(xM, 1))
# print(round(yM, 1))

# valor = int(input("Qual o valor do saque? "))

# # Quantidade de notas de R$ 50
# notas_100 = valor // 100

# # Valor restante a ser sacado com notas menores que R$ 50
# resto_100 = valor % 100

# # Quantidade de notas de R$ 10
# notas_50 = resto_100 // 50

# # Valor restante a ser sacado com notas menores que R$ 50
# resto_50 = resto_100 % 50

# # Quantidade de notas de R$ 2
# notas_10 = resto_50 // 10

# print(int(notas_100))
# print(int(notas_50))
# print(int(notas_10))

# num = int(input())
# centena = num // 100
# print(centena)
# dezena = num % 100 // 10
# print(dezena)
# unidade = num % 10 // 1
# print(unidade)
# print(unidade, dezena, centena)

# num = int(input())

# horas = num // 3600
# minutos = num % 3600 // 60
# segundo = num % 60 

# print (f'{horas}h {minutos}m {segundo}s')