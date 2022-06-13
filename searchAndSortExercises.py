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
def insertion(lista):
    tam = len(lista)
    for i in range(1,2):
        chain = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chain:
            lista[j +1] = lista[j]
            j -= 1
        lista[j+1] = chain
    return lista

lista = eval(input('digite uma lista: '))
print(insertion(lista))

   