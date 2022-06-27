##Busca binária
# def buscaBin(lista, item, comeco=0, fim=None):
#     if fim is None:
#         fim = len(lista)-1
#     if comeco <= fim:
#         meio = (comeco + fim) // 2
#         if lista[meio] == item:
#             return meio
#         if item < lista[meio]:
#             return buscaBin(lista, item, comeco, meio-1)
#         else: 
#             return buscaBin(lista, item, meio+1, fim)
#     else:
#        return -1

# lista = eval(input('digite uma lista: '))
# num = int(input('digite um número inteiro: '))
# print(buscaBin(lista, num))

#Selection Sort

#Bubble sort
# def bubble(lista):
#     tam = len(lista)
#     for j in range(2):
#         for i in range(tam-1):
#             if lista[i] > lista[i+1]:
#                 lista[i], lista[i+1] = lista[i+1], lista[i]
#     return lista

# lista = eval(input('digite uma lista: '))
# print(bubble(lista))
    
#Insertion Sort
# def insertion(lista):
#     tam = len(lista)
#     for i in range(1,2):
#         chain = lista[i]
#         j = i - 1
#         while j >= 0 and lista[j] > chain:
#             lista[j +1] = lista[j]
#             j -= 1
#         lista[j+1] = chain
#     return lista

# lista = eval(input('digite uma lista: '))
# print(insertion(lista))

# def createDic():
#     agenda = {}
#     for i in range(15):
#         nome = input('')
#         agenda[nome] = int(input(''))
#     return agenda

# def busca_dic(num, agenda):
#     for i,j in agenda.items():
#         if j == num:
#             return i
#     return -1

# agenda = createDic()
# numero = int(input(''))
# print(busca_dic(numero,agenda))


# lista = []

# num = input('d: ')
# n = int(num)
# lista.append(n)

# while num:
#     num = input('d: ')
#     if num != '':
#         n = int(num)
#         lista.append(n)
#     else:
#         break

# def selectionSort(lista):
#     tam = len(lista)
#     minIndex = 0
#     for i in range(tam):
#         if lista[i] < lista[minIndex]:
#             minIndex = [i]
#     j = 0
#     if lista[j] > lista[minIndex]:
#         aux = lista[j]
#         lista[j] = lista[minIndex]
#         lista[minIndex] = aux

# listanome = []

# nome = input('digite o nome: ')

# while nome:
#     listanome.append(nome)
#     nome = input('digite o nome: ')

# def insertion(lista):
#     tam = len(lista)
#     counter = 0
#     for i in range(1, tam):
#         chain = lista[i]
#         j = i - 1 
#         while j >= 0 and lista[j] > chain:
#             lista[j+1] = lista[j]   
#             j = j - 1
#             counter += 1
#         lista[j+1] = chain
#     return lista, counter

# listan, trocas = insertion(listanome)
# for i in listan:
#     print(i)
# if trocas == 1:
#     print('1 troca realizada')
# else:
#     print(f'{trocas} trocas realizadas')

# import sys
# lista = []
# trocas = 0

# def selectionSort(lista):
# 	global trocas
# 	array = lista.copy()
# 	n = len(array)
# 	for i in range(n):
# 		menor = i
# 		for j in range(i+1, n):
# 			if array[menor] > array[j]:
# 				menor = j
# 		if menor != i:
# 			trocas += 1
# 			array[i], array[menor] = array[menor], array[i]
# 	return array
# for line in sys.stdin:
# 	line = line.strip()
# 	lista.append(int(line))
# ordenada = selectionSort(lista)
# print("Lista Ordenada: {}, {} trocas foram realizadas.".format(ordenada, trocas))





def selectionSort(lista):
	#Percorre o elemento de forma crescente variando o tamanho da lista
	trocas = 0
	for j in range(len(lista)-1):
		minIndex = j

		#PROCURA O MENOR INDICES
		for i in range(j, len(lista)):
			if lista[i] < lista[minIndex]:
				minIndex = i
			
		if lista[j] > lista[minIndex]:
			aux = lista[j]
			lista[j] = lista[minIndex]
			lista[minIndex] = aux
			trocas += 1
	return lista, trocas

lista = []
while True:
	try:
		num = int(input(''))
		lista.append(num)
	except ValueError:
		break

listaord, trocas = selectionSort(lista)	
print('Lista Ordenada: {}, {} trocas de indices realizadas.'.format(listaord, trocas))


# print(selectionSort(lista))

# lista = [8,4,2,7,1,7,3]
# def bubble(lista):
# 	for j in range(len(lista)-1):
# 		for i in range(len(lista)-1):
# 			if lista[i] > lista[i+1]:
# 				lista[i], lista[i+1] = lista[i+1], lista[i]

# print(bubble(lista))

class Conta_corrente:
    numero_conta = 1
    def __init__(self,nome_correntista,servicos_extras, saldo_conta):
        self.nome_correntista = nome_correntista
        self.servicos_extras = servicos_extras
        self.saldo_conta = saldo_conta

    def atualizarSaldo100Reais(self):
        if self.saldo_conta < 100:
            self.saldo_conta += 200
    
    def atualizarSaldoServicos(self):
        if self.servicos_extras == True:
            self.saldo_conta -= 50
        else:
            self.saldo_conta -= 10

    def get_saldo_conta(self):
        return self.saldo_conta


def cadastrar(Conta_corrente):
    listaDeContas = []
    for i in range(3):
        nome_correntista = input('')
        servicos_extras = eval(input(''))
        saldo_conta = float(input(''))
        conta = Conta_corrente(nome_correntista, servicos_extras, saldo_conta)
        conta.numero_conta += i
        listaDeContas.append(conta)
    return listaDeContas

def removerConta(lista):
    for conta in lista:
        if conta.saldo_conta > 1000:
            lista.remove(conta)
    
lista = cadastrar(Conta_corrente)
newlist = sorted(lista, key = Conta_corrente.get_saldo_conta, reverse = True)
for conta in newlist:
    if conta.saldo_conta < 100:
        if conta.servicos_extras == True:
            print('{}, com servicos extras, possui {:.2f} reais'.format(conta.nome_correntista, conta.saldo_conta))
        else:
            print('{}, sem servicos extras, possui {:.2f} reais'.format(conta.nome_correntista, conta.saldo_conta))

removerConta(newlist)
for conta in newlist:
    conta.atualizarSaldo100Reais()
    conta.atualizarSaldoServicos()
    if conta.servicos_extras == True:
        print('{}, com servicos extras, possui {:.2f} reais'.format(conta.nome_correntista, conta.saldo_conta))
    else:
        print('{}, sem servicos extras, possui {:.2f} reais'.format(conta.nome_correntista, conta.saldo_conta))