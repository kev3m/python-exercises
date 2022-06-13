# numInicial = int(input())
# numFinal = int(input())

# while numInicial <= numFinal:
#     print(numInicial)
#     numInicial += 1
# print("Fim")   

# import random 
# random.seed()

# num = random.randrange(1,10)
# print(num)
# chances = 3
# numEntrada = int(input("Qual número foi gerado? "))



# while 
# if numEntrada != num:
#     print('Número incorreto')
#     numEntrada = int(input("Qual número foi gerado? "))
# print('Acertou, miseravi')

# '''O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde para
# dar uma indicação sobre a condição de peso de uma pessoa adulta.

# A fórmula é IMC = peso / ( altura )²

# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de
# acordo com a tabela abaixo.
# IMC em adultos Condição:
# Abaixo de 18,5 → Abaixo do peso
# Entre 18,5 e 25 → Peso normal
# Entre 25 e 30 → Acima do peso
# Acima de 30 → Obeso'''

# peso = float(input('Digite seu peso:'))
# altura = float(input('Digite sua altura em metros: '))

# imc = peso / ( altura )**2

# if imc < 18.5:
#     print('Abaixo do peso')
# elif imc >= 18.5 and imc <= 25:
#     print('Peso normal')
# elif imc >= 25 and imc <= 30:
#     print('Acima do peso')
# else:
#     print('Obeso')

# for i in range(1,100):
#     if i % 2 == 0:
#         print(i)

# '''Faça um programa em Python que leia 10 números reais, um de cada vez (ou seja, um por linha), e conte quantos são positivos, a soma dos números negativos, e a média de todos os valores.'''

# numero_positivo = 0
# soma_negativo = 0
# soma = 0

# for num in range(0, 10):
#   numero = float(input("num: "))
#   soma = soma + numero
#   if numero > 0:
#     numero_positivo = numero_positivo + 1
#   elif numero < 0:
#     soma_negativo = soma_negativo + numero
  
# media = soma / 10

# print(numero_positivo)
# print(soma_negativo)
# print('{:.1f}'.format(media))

##############################################################
# salario = float(input("salario: "))#998
# quantidade_cont = int(input('Quantidade: '))#5
# despesa = 0
# for num in range(quantidade_cont): 
#   valor_contas = float(input("valor das contas: "))
#   despesa = despesa + valor_contas

# economia = salario - despesa  
    
# if economia > 0:
#         print(f'Parabens! Este mês você economizou {economia:.2f}  reais')
# elif economia < 0:
#         print(f'Você precisa reduzir suas despesas em {economia:.2f} reais')

##############################################################


# '''Escreva um programa em Python que leia as 10 notas de uma avaliação dos alunos que cursam uma disciplina de algoritmos, calcule e imprima na tela (nesta ordem):

# A quantidade de notas maiores ou iguais a 7;
# A quantidade de notas maiores ou iguais a 3 e menores que 7;
# A quantidade de notas menores que 3;
# A média da turma na avaliação.
# '''

# notas_aprovadas = 0
# notas_reprovadas = 0


# for notas in range(0 ,10):
#    notas = float(int('Digite as notas:'))
#    print(notas)



# salario = float(input('Digite um salario: '))
# quantidade_contas = int(input('Quantidade de Contas a pagar: '))
# despesas = 0

# for i in range(1,quantidade_contas + 1):
#     i = float(input('Digite o valor da conta a ser paga: '))
#     despesas += i

# if (salario - despesas) > 0:
#     print("Parabens! Este mes voce economizou {} reais".format(salario - despesas))
# else:
#     print("Voce precisa reduzir suas despesas em {} reais".format((salario - despesas) * -1))
a = 7
d = 0
for i in range(1, a):
    d = d + i
    
    

print(i)