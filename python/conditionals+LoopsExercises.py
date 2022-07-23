#################Exec 1#######################


# valores = int(input('Digita um valor ai mano: '))
# soma = valores
# quantidadeValores = 0

# while valores != 0:
#     valores = int(input('Mais um:'))
#     soma = soma + valores
#     quantidadeValores += 1

# print('{:.2f}'.format(soma/quantidadeValores))


#################Exec 2#######################
# posicaoInicial = float(input('Digite a posição inicial em metros: '))
# tempo = 0
# posicao = posicaoInicial


# while posicao >= 0:
#     posicao = posicaoInicial - (0.5 * (9.8 * tempo**2))
#     if tempo == 1:
#         tempo == 0
#     tempo += 1
#     if posicao < 0:
#         break
#     print('t = {}'.format(tempo - 1))
#     print('h = {:.1f}'.format(posicao))

#################Exec 3#######################
# numHabitA = int(input('Numero de habitantes de A: '))
# numHabitB = int(input('Numero de habitantes de B: '))
# percentCresA = float(input('Digite o percentual de crescimento de A: '))
# percentCresB = float(input('Digite o percentual de crescimento de B: '))

# numHabitA_Var = 0 + numHabitA #100
# numHabitB_Var = 0 + numHabitB #200

# anosPercorridos = 0

# while numHabitA_Var < numHabitB_Var:
#     numHabitA_Var += (numHabitA_Var * (percentCresA / 100))
#     anosPercorridos += 1
# print(anosPercorridos)

# while numHabitB_Var < numHabitA_Var:
#     numHabitB_Var += (numHabitB_Var * (percentCresB / 100))
#     print(numHabitB_Var)
  
#################Exec 8#######################
# pi = 3.14159
# raio = 1
# areas = []
# while raio > 0:
    
#     raio = float(input('Mais um:'))
#     if raio == 0:
#         break
#     area = pi * raio ** 2
#     areas.append(area)

# for elemento in areas:
#     print('{:.2f}'.format(elemento))

#################Exec 10#######################
totaldeNumeros = int(input('Digite o total ai: '))
entradaNum = 0
entradaNumSoma = 0
quantiNum = 0

# while entradaNum < totaldeNumeros:
#     entradaNum = int(input('Digita um numero ai pai:'))
#     entradaNumSoma += entradaNum
#     quantiNum += 1
#     if entradaNumSoma > totaldeNumeros:
#         entradaNum = entradaNumSoma
    
# print(quantiNum)
# print('{:.1f}'.format(entradaNum/quantiNum))

#################Exec 11#######################
# notaAluno = 0
# lista = []

# while notaAluno == 0 or notaAluno <= 10:
#     notaAluno = float(input('Zap: '))
#     if notaAluno > 10 or notaAluno < 0:
#         break
#     if notaAluno >= 7:
#         lista.append('APROVADO')
#     elif notaAluno < 7 and notaAluno >=3:
#         lista.append('FINAL')
#     else:
#         lista.append('REPROVADO')


# for element in lista:
#     print(element)

#################Exec 16#######################
# numPositivosList = []
# numNegativosList = []

# entrada = 1 

# while entrada != 0:
#     entrada = int(input())
#     if entrada < 0:
#         numNegativosList.append(entrada)
#     elif entrada > 0:
#         numPositivosList.append(entrada)
    

# total = len(numNegativosList) + len(numPositivosList)

# numPositivosList = len(numPositivosList)
# numNegativosList = len(numNegativosList)
# total = total


# numPositivosPer = (numPositivosList / total) * 100
# numNegativosPer = (numNegativosList / total) * 100

# print("{:.1f}".format(numPositivosPer))
# print("{:.1f}".format(numNegativosPer))

#################Exec 17#######################

# valoresPares = []
# valoresPMedia = 0
# valoresPQuant = 0


# valoresImpares = []
# valoresIMPmedia = 0
# valoresIMPQuant = 0

# entrada = 1

# while entrada > 0:
#     entrada = int(input())
#     if entrada % 2 == 0:
#        valoresPares.append(entrada)
#        valoresPMedia += entrada
#        valoresPQuant += 1
#     else:
#         valoresImpares.append(entrada)
#         valoresIMPmedia += entrada
#         valoresIMPQuant += 1
#     if entrada == 0:
#         valoresPares.pop()
#         valoresPQuant -= 1


# somadasListas = len(valoresPares) + len(valoresImpares)

# print('{:.1f}'.format(valoresPMedia / valoresPQuant))
# print('{:.1f}'.format(valoresIMPmedia / valoresIMPQuant))
# print(somadasListas)

