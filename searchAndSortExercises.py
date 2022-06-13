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

listanome = []

nome = input('digite o nome: ')

while nome:
    listanome.append(nome)
    nome = input('digite o nome: ')

def insertion(lista):
    tam = len(lista)
    counter = 0
    for i in range(1, tam):
        chain = lista[i]
        j = i - 1 
        while j >= 0 and lista[j] > chain:
            lista[j+1] = lista[j]   
            j = j - 1
            counter += 1
        lista[j+1] = chain
    return lista, counter

listan, trocas = insertion(listanome)
for i in listan:
    print(i)
if trocas == 1:
    print('1 troca realizada')
else:
    print(f'{trocas} trocas realizadas')

