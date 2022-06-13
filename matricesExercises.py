#exec 05

# aberto = ['[','{', '(']
# fechado = [']','}', ')']

# def casado(sequence):
#     pilha = []
#     for i in sequence:
#         if i in aberto:
#             pilha.append(i)
#             #combinar no top e colocar lá
#         elif i in fechado:
#             pos = fechado.index(i)
#             if ((len(pilha) > 0 ) and (aberto[pos] == pilha[len(pilha)-1])):
#                 pilha.pop()
#             else:
#                 return 'NAO'
#     if len(pilha) == 0:
#         return 'SIM'
#     else:
#         return 'NAO'

# s = input('sequência: ')
# while s != '###':
    
#     print(casado(s))
#     s = input('Digite a cadeia: ')


# open_list = ["[","{","("] 
# close_list = ["]","}",")"] 
# def check(myStr): 
#     stack = [] 
#     for i in myStr: 
#         if i in open_list: 
#             stack.append(i) 
#         elif i in close_list: 
#             pos = close_list.index(i) 
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack)-1])): 
#                 stack.pop() 
#             else: 
#                 return "Unbalanced"
#     if len(stack) == 0: 
#         return "Balanced"
#     else: 
#         return "Unbalanced"
  
  #declarando matriz 

#PONTO EM QUADRANTES SUPERIORES OU INFERIORES
# x = float(input('valor de x>'))
# y = float(input('valor y>'))

# if x > 0 and y > 0:
#   print('Superiores')
# elif x < 0 and y > 0:
#   print('Superiores')
# elif x < 0 and y < 0:
#   print('Inferiores')
# else:
#   print('Inferiores')

#Maior pagamento da semana

# matriz = eval(input('digite a matriz>'))

# for funcio in matriz:
#   print(max(funcio))

#Diagonal principal versus diagonal secundária
# matrizdimensao = int(input('Digite a dimensão: '))
# matriz = []
# diagPrincipal = 0
# diagSec = 0
# counter = (matrizdimensao - 1)
# for i in range(matrizdimensao):
#   matrizlinhas = eval(input('Digite a linha da matriz: '))
#   matriz.append(matrizlinhas)
#   diagPrincipal += matrizlinhas[i]


# for i in matriz:
#   num = i[counter]
#   diagSec += num
#   counter -= 1


# diferenca = diagPrincipal - diagSec

# print(diferenca)

#TEMPERATURAS MÍNIMAS
# matriz = eval(input(''))
# menorTemp = []
# for i in matriz:
#   menor = min(i)
#   menorTemp.append(menor)

# print(menorTemp)

#HORAS DE TRABALHO POR FUNCIONÁRIO
# matriz = eval(input('matriz> '))
# #coluna = dia da semana
# #linha = funcionario
# vetor = []
# for i in matriz:
#   hrs = sum(i)
#   vetor.append(hrs)


# for linhas in matriz:
#   for colunas in range(len(matriz)):
#     horas = 

