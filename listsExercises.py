import re
from collections import Counter
##Exec 1
# def posicao(quant, lista):
#     listaPar = []
#     listaImpar = []
#     for i in range(quant):
#             if i % 2 == 0:
#                 listaPar.append(lista[i])
#             else:
#                 listaImpar.append(lista[i])
#     return listaPar, listaImpar

# quantEl = int(input('quant: '))
# num = eval(input('aqui: '))[:quantEl]
# par, impar = posicao(quantEl, num)

# if par:
#     print(par)
# if impar:
#     print(impar)
    

# lista = []
# listaImpar = []
# def ordenarNumeros(num):
#     if num % 2 == 0:
#         lista.append(num)
#     else:
#         listaImpar.append(num)

#     return lista, listaImpar
    
# n = int(input('Digite: '))

# while n > 0:
#     ordenarNumeros(n)
#     n = int(input('Digite: '))

# lista.extend(listaImpar)
# print(*lista, sep = ', ')

# def contarAlunos(age):
#     idades = []
#     for i in range(0, 4):
#         age = int(input('Digite a idade: '))
#         idades.append(age)
#     return idades

# idade = int(input('Digite: '))
# print(contarAlunos(idade))




# def contarCons(frase):
#     cont = 0
#     dicts = Counter(re.sub('[aeiouAEIOU]', '', frase))
#     for i in dicts.items():
#         cont += i
#     return cont, dicts


# fras = input('frase: ')
# cont, dicts = contarCons(fras)
# print(cont)
# print(dicts)


# temp = []
# meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Outubro', 'Novembro', 'Dezembro']
# for i in range(3):
#     temperature = float(input('temperature: '))
#     temp.append(temperature)

# media = sum(temp) /3
# print(temp)
# for j in temp:
#     if j > media:
#         print(enumerate(j in temp))
           

# quant = int(input('aq: '))
# lista = eval(input('lista: '))
# n1 = eval(input('n1: '))
# n2 = eval(input('n2: '))

# def swap(quantidade, lista,n1,n2):
#     index1 = []
#     index2 = []
#     if n1 in lista and n2 in lista:
#         for i in range(quantidade):
#             swp = lista[i]
#             if swp == n1:
#                 index1.append(i)
#             if swp == n2:
#                 index2.append(i)
#         lista[index1[0]] = n2
#         lista[index2[0]] = n1
#         return lista
#     else: 
#         return None

# listaTrocada = swap(quant, lista, n1,n2)
# if listaTrocada != None:
#     print(f'swap succeded: {listaTrocada}')
# else: 
#     print('elements not found')


 
# idades = eval(input('id: '))
# alturas = eval(input('heigth: '))

# mediaAlt = 0
# for altura in alturas:
#     mediaAlt += altura
# mediaAlt /= 3
# menorQamedia = 0

# for i in range(len(idades)):
#     altura = alturas[i]
#     idade = idades[i]
#     if altura < mediaAlt and idade > 13:
#         menorQamedia += 1 

# print(menorQamedia)



# sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
# votos = [0,0,0,0,0,0]

# vote = int(input('Digite seu voto: '))


# while vote != 0:
#     votos[vote - 1] += 1
#     vote = int(input('Digite seu voto: '))
    
# totalVotos = sum(votos)
# maisVotado = votos.index(max(votos))
# print(maisVotado)
# print(votos)

# print('Windows Server {} {:.2f}%'.format(votos[0], votos[0] * 100 / totalVotos))
# print('Unix {} {:.2f}%'.format(votos[1],votos[1] * 100 / totalVotos))
# print('Linux {} {:.2f}%'.format(votos[2],votos[2] * 100 / totalVotos))
# print('Netware {} {:.2f}%'.format(votos[3],votos[3] * 100 / totalVotos))
# print('Mac OS {} {:.2f}%'.format(votos[4],votos[4] * 100 / totalVotos))
# print('Outro {} {:.2f}%'.format(votos[5],votos[5] * 100 / totalVotos))
# print('total {} votos'.format(totalVotos))
# print('O Sistema Operacional mais votado foi o {}'.format(sistemas[maisVotado]))
# sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
# votos = [0,0,0,0,0,0]

# vote = int(input(''))

# while vote != 0:
#     votos[vote - 1] += 1
#     vote = int(input(''))
    
# totalVotos = sum(votos)


# prcList = []
# maisVotado = votos.index(max(votos))
# for i in votos:
# 	prc = (i *100)/ totalVotos
# 	prcList.append(prc)
	
	
# maiorprc = max(prcList)	
# maiorvoto = max(votos)	

			
# for i in range(6):
# 	print('{} {} {:.0f}%'.format(sistemas[i], votos[i], prcList[i]))

# print('Total {} votos'.format(totalVotos))
# print('O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {:.0f}% dos votos'.format(sistemas[maisVotado],maiorvoto, maiorprc))
# lista1 = eval(input('>'))
# lista2 = eval(input('>'))

# terceiroVet = []

# for i in range(10):
#     terceiroVet.append(lista1[i])
#     terceiroVet.append(lista2[i])

# print(terceiroVet)