#######Exec 1############################################################
# ddd = int(input('Digite o seu DDD:'))


# if ddd == 61:
#     print('Brasilia')
# elif ddd == 71:
#     print('Salvador')
# elif ddd == 11:
#     print('São Paulo')
# elif ddd == 21:
#     print('Rio De Janeiro')
# elif ddd == 32:
#     print('Juiz de Fora')
# elif ddd == 19:
#     print('Campinas')
# elif ddd == 71:
#     print('Vitoria')
# elif ddd == 31:
#     print('Belo Horizonte')
# else: 
#     print('DDD não cadastrado')

# #############Exec 9##########################################################
# #- Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá
# se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos
# deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.


# num1 = int(input())
# num2 = int(input())
# varC = 0

# if num1 == num2:
#     varC = num1 + num2
#     print(f'O valor de varC é:{varC}')
# elif num1 != num2:
#     varC = num1 * num2
#     print(f'O valor de varC é:{varC}')



# #############Exec 10##########################################################

# salario = float(input())
# gastos = float(input())


# if salario >= gastos:
#     print('Gastos dentro do orçamento')
# else:
#     print('Orçamento estourado')


# #############Exec 11##########################################################

# gols_timeA = int(input())
# gols_timeB = int(input())


# if gols_timeA > gols_timeB:
#     print('Vitória do time A')
# elif gols_timeA < gols_timeB:
#     print('Vitória do time B')
# else:
#     print('Empate')

# #############Exec 12##########################################################

# altura = float(input('Digite a altura em centimetros:'))
# largura = float(input('Digite a largura em centimetros:'))
# comprimento = float(input('Digite o comprimento em centimetros:'))
# consumoPorDia = float(input('Digite o consumo em litros: '))

# capacidadeTotal = (altura * largura * comprimento) / 1000
# autonomia = capacidadeTotal / consumoPorDia

# print(f"A capacidade total em litros é {capacidadeTotal}L ")
# print(f"A autonomia do reservatório é {autonomia}L/Dia ")

# if autonomia < 2:
#     print('O reservatório tem consumo elevado')
# elif autonomia >= 2 and autonomia <= 7:
#     print('O reservatório tem consumo moderado')
# else:
#     print('O reservatório tem consumo reduzido')