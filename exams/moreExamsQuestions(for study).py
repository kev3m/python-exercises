# import math
from pickle import dump, load
# x1 = 0
# y1 = 0
# x2 = 0
# y2 = 0

# repeat = 'S'

# while repeat == 'S':
#     x1 = float(input())
#     y1 = float(input())
#     x2 = float(input())
#     y2 = float(input())
#     distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     print (f"{distancia:.2f}")
#     repeat = input('Deseja calcular outra distância? [S/N]').upper()


# positivos = 0
# negativos = 0
# pares = 0
# impares = 0

# for i in range(10):
#     i = int(input('Digite um número natural: '))

#     if i > 0:
#         positivos += 1
#     elif i < 0:
#         negativos += 1  

#     if i % 2 == 0:
#         pares += i 
#     elif i % 2 != 0:
#         impares += i 
    
#     resul = 1
#     for j in range(1, i + 1):
#         print(j)
#         resul *= j

#     print(resul)



# print(positivos)
# print(negativos)
# print(pares)
# print(impares)
# print(f"A soma dos números pares subtraídos dos impares é: {pares + impares}")

# from re import sub


# operacao = int(input('Escolha uma operacao: \n 1 - Soma \n 2 - Subtração \n 3 - Mult \n 4 - Divid \n 5 - Pot \n 6 - Encerrar \n '))

# while 1 <= operacao < 6:

#     num1 = 0
#     num2 = 0 

#     if operacao == 1:
#         print('Você escolheu soma')
#         num1 = int(input('Digite um número: '))
#         num2 = int(input('Digite um número: '))
#         contadorDeChances = 1
#         soma = num1 + num2
#         tentativa = 0
#         while soma != tentativa and contadorDeChances <= 3:
#             tentativa = int(input('Digite o resultado da soma entre os números escolhidos: '))
            
#             if tentativa != soma:
#                 contadorDeChances += 1
#             elif tentativa == soma:
#                 print(f"Parabéns, você acertou na {contadorDeChances} tentativa!") 
#         if soma != tentativa:  
#                 print(f"O resultado correto é: {soma}")

#     elif operacao == 2:
#         print('Você escolheu subtração')
#         num1 = int(input('Digite um número: '))
#         num2 = int(input('Digite um número: '))
#         contadorDeChances = 1
#         subtracao = num1 - num2
#         tentativa = 0
#         while subtracao != tentativa and contadorDeChances <= 3:
#             tentativa = int(input('Digite o resultado da soma entre os números escolhidos: '))
            
#             if tentativa != subtracao:
#                 contadorDeChances += 1
#             elif tentativa == subtracao:
#                 print(f"Parabéns, você acertou na {contadorDeChances} tentativa!") 
#         if subtracao != tentativa:  
#                 print(f"O resultado correto é: {subtracao}")


#     operacao = int(input('Escolha uma operacao: \n 1 - Soma \n 2 - Subtração \n 3 - Mult \n 4 - Divid \n 5 - Pot \n 6 - Encerrar \n '))

################ Prova Antiga ########################

# print ('''
# Relação dos planetas \n
# # ---------- Gravidade Relativa --- Planeta \n
# 1 ---------- 0,37 ---------- Mércurio \n
# 2 ---------- 0.88 ---------- Vênus \n
# 3 ---------- 0.38 ---------- Marte \n
# 4 ---------- 2,64 ---------- Júpiter \n
# 5 ---------- 1,15 ---------- Saturno \n
# 6 ---------- 1,17 ---------- Urano \n''')

# mercurio = 1
# venus = 2
# marte = 3
# jupiter = 4
# saturno = 5
# urano = 6

# peso = float(input('Digite um peso'))
# planeta = int(input('Digite um planeta'))

# if planeta == 1:
#     peso = peso/10 * 0.37
# elif planeta == 2:
#     peso = peso/10 * 0.88
# elif planeta == 3:
#     peso = peso/10 * 0.38
# elif planeta == 4:
#     peso = peso/10 * 2.64
# elif planeta == 5:
#     peso = peso/10 * 1.15    
# elif planeta == 6:
#     peso = peso/10 * 1.17

# else:
#     print('Planeta inexistente')

# print(f"O peso é de {peso}kg no planeta de índice {planeta} ")




# sacosDisp = int(input('Digite a quantidade de sacos de cimento disponiveis no estoque: '))
# preco = float(input('Digite o preço de cada saco: '))
# maiorvalor = 0
# maiorcliente = 0
# cliente = 1
# while cliente > 0 and sacosDisp >= 100:
#     cliente = int(input('Digite o código do cliente: '))
#     sacosComprados = int(input('Digite a quantidade de sacos adquiridos por este cliente: '))
#     valor = sacosComprados * preco
    
#     if valor > maiorvalor:
#         maiorvalor = valor
#         maiorcliente = cliente


#     if sacosDisp > sacosComprados and sacosComprados <= (sacosDisp * 0.1):
#         print(f"O código do cliente é {cliente}")
#         print(f"A quantiade de sacos pedidos é {sacosComprados}")
#         print(f"o valor do pedido é {valor}")
#         sacosDisp -= sacosComprados
#     elif sacosDisp < sacosComprados:
#         print('Estoque insuficiente')
#     else: 
#         print('Ultrapassado o máximo permitido')


# print(f"A quantidade de sacos em estoque é: {sacosDisp}")
# print(f'O cliente que fez o maior pedido é o {maiorcliente}')



class Pessoa:
    def __init__(self, cPF, nome, idade,sexo):
        self.cPF = cPF
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.amigos = []

def menu():
  print("Entre com uma opção do menu abaixo: ")
  print("[a] - Cadastrar Pessoa.")
  print("[b] - Buscar Pessoa.")
  print("[c] - Cadastrar amigo de uma Pessoa.")
  print("[d] - Desfazer amizade.")
  print("[e] - Imprimir os dados de todas as Pessoas cadastradas.")
  print("[f] - Devolver a lista de amigos de uma Pessoa de nome X.")
  print("[g] - Gravar os dados de todas as pessoas em um arquivo texto, como saída.")
  print("[h] - Encerrar.")
  opcao = input("Escolha sua opção: ")
        
entrada = open('entrada.dat', 'wb')
pessoa1 = Pessoa('08959039543','Pedro','18', 'M')
pessoa2 = Pessoa('94582231489','Mauricio','23', 'M')
pessoa3 = Pessoa('45852904123','Ana','21', 'F')
pessoa4 = Pessoa('58217894127','Luzia','25', 'F')
pessoa5 = Pessoa('83905827892','Tarcio','17', 'M')

pessoa1.amigos.append(pessoa2.cPF)
pessoa2.amigos.append(pessoa1.cPF)

pessoa1.amigos.append(pessoa3.cPF)
pessoa3.amigos.append(pessoa1.cPF)

pessoa2.amigos.append(pessoa5.cPF)
pessoa5.amigos.append(pessoa2.cPF)

pessoa4.amigos.append(pessoa5.cPF)
pessoa5.amigos.append(pessoa4.cPF)

pessoa2.amigos.append(pessoa4.cPF)
pessoa4.amigos.append(pessoa3.cPF)

dump(pessoa1, entrada)
dump(pessoa2, entrada)
dump(pessoa3, entrada)
dump(pessoa4, entrada)
dump(pessoa5, entrada)
entrada.close()

print(pessoa4.amigos)