from base64 import b64decode
import random

# def selectionSort(lista):
#     for j in range(len(lista)-1):
#         minIndex = j

#         for i in range(j, len(lista)):
#             if lista[i] < lista[minIndex]:
#                 minIndex = i

#         if lista[j] > lista[minIndex]:
#             lista[j], lista[minIndex] = lista[minIndex], lista[j]
#     return lista

# def bubble(lista):
#     for i in range(len(lista)-1):
#         for j in range(len(lista)-1):
#             if lista[j] > lista[j+1]:
#                 lista[j], lista[j+1] = lista[j+1], lista[j]
#     return lista 

lista = [224,229,227,223,221,220]

# def insertion(lista):
#     for i in range(1, len(lista)):
#         chave = lista[i]
#         j = i - 1
#         while j >= 0 and lista[j] > chave:
#             lista[j+1] = lista[j]
#             j -= 1
#         lista[j+1] = chave
#     return lista

# print(insertion(lista))

# def bolha(lista):
#     for i in range(len(lista)-1):
#         for j in range(len(lista)-1):
#             if lista[j] > lista[j+1]:
#                 lista[j+1], lista[j] = lista[j], lista[j+1]
#     return lista

# print(bolha(lista))





# n = 10
# assert n != 10

# def seelction(lista):
#     for i in range(len(lista)-1):
#         minIndex = i

#         for j in range(i, len(lista)):
#             if lista[j] < lista[minIndex]:
#                 minIndex = j

#         if lista[i] > lista[minIndex]:
#             lista[minIndex], lista[i] = lista[i], lista[minIndex]
#     return lista

# lista = [3,2,6,1,8,9,5]
# print(seelction(lista))

# def bubble(lista):
#     for i in range(len(lista)-1):
#         for j in range(len(lista)-1):
#             if lista[j] > lista[j +1]:
#                 lista[j], lista[j+1] = lista[j+1], lista[j]
#     return lista

# print(bubble(lista))

# def selectionSort(lista):
#     for i in range(len(lista)-1):
#         minIndex = i
#         for j in range(i, len(lista)):
#             if lista[j] < lista[minIndex]:
#                 minIndex = j
        
#         if lista[minIndex] < lista[i]:
#             lista[i], lista[minIndex] = lista[minIndex], lista[i]
#     return lista
            

# print(selectionSort(lista))
# LISTA = eval(b64decode(b64decode(b'VzJrZ1ptOXlJR2tnYVc0Z2NtRnVaMlVvTlRBd01EQXdLVjA9')))
# lista = [1,4,7,9,10,14,16,19,23,25,27,33,44,45,46,47]
# n = random.choice(lista)
# print(n)


# def binarySearch(lista, num, comeco=0, fim=None):
#     if fim == None:
#         fim = len(lista)-1
#     if comeco <= fim:
#         meio = (comeco + fim)//2
#         if lista[meio] == num:
#             return meio
#         if num < lista[meio]:
#             return binarySearch(lista,num,comeco, meio-1)
#         else:
#             return binarySearch(lista, num, meio+1, fim)
#     return -1

# # print(binarySearch(LISTA, n))

# def buscaBin(lista, num, comeco=0, fim=None):
#     if fim == None:
#         fim = len(lista)-1
#     if comeco <= fim:
#         meio = (comeco + fim) //2
#         if lista[meio] == num:
#             return meio
#         if num < lista[meio]:
#             return buscaBin(lista,num, comeco, meio-1)
#         else:
#             return buscaBin(lista,num, meio+1, fim)
#     return -1
        

# print(buscaBin(lista,n))
class Conta:
    def __init__(self,nome,servicos,saldo):
        self.nome = nome
        self.servicos = servicos
        self.saldo = saldo
    
    def __repr__(self):
        if self.servicos:
            return str('{}, com servicos extras, possui {:.2f} reais'.format(self.nome, self.saldo))
        if not self.servicos:
            return str('{}, sem servicos extras, possui {:.2f} reais'.format(self.nome, self.saldo))

contas = []
for a in range(3):
    nome = input('nome: ')
    servicos = eval(input('servicos extras: '))
    saldo = float(input('saldo da conta: '))
    objeto = Conta(nome,servicos,saldo)
    contas.append(objeto)

for conta in contas:
    if conta.saldo <100:
        conta.saldo +=200

for conta in contas:
    if conta.servicos:
        conta.saldo -=50
    if not conta.servicos:
        conta.saldo -=10

for conta in contas:
    if conta.saldo >1000:
        contas.remove(conta)
			
contas.sort(key=lambda x: x.saldo)

for conta in contas:
    print(conta)