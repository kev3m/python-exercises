import random
# def menu():
#     print("\n"*2)
#     print('''Digite a opção desejada \n
# [1] - Adicionar mercadoria a pilha
# [2] - Encaminhar mercadorias a fila
# [3] - Permitir embarque de mercadorias no caminhão
# [4] - Retirar caixas do caminhão
# [5] - Listar mercadoria desembarcadas
# [6] - Parar''')
#     opcao = int(input('Qual sua escolha?: '))
#     return opcao

# pilha = []
# filadeEsp = []
# embarque = []
# desembarque = []
# opcao = menu()

# while True:
#     if opcao == 1:
#         mercadoria = input('Digite a mercadoria a ser inserida na pilha: ')
#         pilha.append(mercadoria)
#         print(f'{mercadoria} foi adicionada na pilha')
#         opcao = menu()
#     elif opcao == 2:
#         print('encaminhando mercadorias a fila de espera')
#         while len(pilha) != 0:
#             retirar = pilha.pop()
#             filadeEsp.append(retirar)
#         print(pilha)
#         print(filadeEsp)
#         opcao = menu()
#     elif opcao == 3:
#         print('Realizando o embarque no caminhão')
#         while len(filadeEsp) != 0:
#             retirar = filadeEsp.pop(0)
#             embarque.append(retirar)
#             print(embarque)
#         opcao = menu()
#     elif opcao == 4:
#         while len(embarque) != 0:
#             retirar = embarque.pop()
#             desembarque.append(retirar)
#             print(embarque)
#     elif opcao == 5:
#         print(desembarque)
#     elif opcao == 6:
#         break
#         

#FIla - O Primeiro a chegar sai primeiro, e o ultimo sai por ultimo

# def menu():
#     print('''
#     [1] - Listar o número de aviões aguardando na fila
#     [2] - Autorizar a decolagem do primeiro avião
#     [3] - Adicionar um avião a lista
#     [4] - Listar o número de aviões aguardando na fila
#     [5] - Listar as características do primeiro avião da fila
#     [6] - Encerrar o programa        
#         ''')
#     opcao = int(input('Digite a escolha: '))
#     return opcao

# avioes = {} 
# filaEs = []
# opcao = menu()

# while True:
#     if opcao == 1:
#         print(f'O núm de aviões aguardando é {len(avioes.keys())}')
#         opcao = menu()
#     elif opcao == 2:
#         decolar = filaEs[0]
#         print(f'Iniciada a decolagem do avião {decolar}')
#         avioes.pop(filaEs)
#         opcao = menu()
#     elif opcao == 3:
#         numAv = int(input('Digite o numero do avião: '))
#         cor = input('Digite a cor do avião: ')
#         avioes[numAv] = cor
#         filaEs.append(numAv)
#         print(f'O avião {numAv} foi adicionado a lista de espera')
#         opcao = menu()
#     elif opcao == 4:
#         print(f'Os aviões na fila de espera são: {avioes.keys()}')
#         opcao = menu()
#     elif opcao == 5:
#         char = filaEs[0]
#         print(f'As caracateristicas do avião da primeira fila são {avioes[0]}')
#         opcao = menu()
#     elif opcao == 6:
#         break

# print(avioes)

#Sistema de pilha 

# def menu():
#     print('''
# [1] - Adicionar livros a pilha
# [2] - Ler livro e doar para biblioteca
# [3] - Parar   
#     ''')
#     opcao = int(input('Selecione uma opção: '))
#     return opcao


# livros = []
# biblioteca = []

# opcao = menu()
# while opcao != 3:
#     if opcao == 1:
#         comprado = input('livro comprado> ')
#         while comprado != '.':
#             livros.append(comprado)
#             comprado = input('livro comprado> ')
#         opcao = menu()
#     if opcao == 2:
#         doar = livros.pop()
#         print(f'Greg, vc deve ler {doar}')
#         biblioteca.append(doar)
#         opcao = menu()

# print(livros)
# print(biblioteca)

# matriz = []
# contadorde0 = 0

# for i in range(8):
#     linha = []
#     for j in range(8):
#         randomnum = random.randint(0,1)
#         linha.append(randomnum)
#         if randomnum == 0:
#             contadorde0 += 1
#     matriz.append(linha)


# doisTercos = ((8 * 8) / 3) * 2
# if contadorde0 > doisTercos:
#     print("É uma matriz esparsa")
# else:
#     print("Não é uma matriz esparsa")

# print(matriz)
# print(contadorde0)
# matriz = []
# matriz2 = []
# matrizSum = []

# for i in range(6):
#     linha = []
#     for j in range(9):
#         num = random.randint(1,100)
#         linha.append(num)
#     matriz.append(linha)

# for i in range(6):
#     linha = []
#     for j in range(9):
#         num = random.randint(1,100)
#         linha.append(num)
#     matriz2.append(linha)

# for i in range(6):
#     linha = []
#     for j in range(9):
#         num = matriz[i][j] + matriz2[i][j]
#         linha.append(num)
#     matrizSum.append(linha)

# print(matriz)
# print(matriz2)
# print(matrizSum)

# matriz = {}
# media = []
# quant7 = 0

# #3 alunos
# for alunos in range(3):
#     medias = []
#     for provas in range(3):
#         nota = int(input('Digite a nota do aluno> '))
#         matriz[(alunos +1 ,provas +1)] = nota
#         medias.append(nota)
#     media.append(sum(medias)/ 3 )

# for i in media:
#     if i > 7:
#         quant7 += 1
# print(matriz)
# print(media)
# print(quant7)

# Questão 1 - versão 2 - matriz esparsa
# notas ={}
# # Leitura das notas
# for i in range(3): #linha corresponde ao aluno
#     for j in range(5): #coluna corresponde as notas
#         nota = float(input(('Digite a nota {0} do aluno {1}'.format(j+1, i+1))))
#         notas[(i+1,j+1)]=nota
# medias = []
# cont = 0
# maior = 0
# for i in range(3): #linha corresponde ao aluno
#     m = 0
#     for j in range(5): #coluna corresponde as notas
#         m += notas.get((i+1,j+1),0)
#         print(notas.get((i+1,j+1),0), end=' ')
#     medias.append(m/5)
#     print(medias[i],end=' ')
#     print()

#     if i == 0:
#        maior = medias[0]
#     else:
#         if medias[i] > maior:
#             maior = medias[i]

#     if medias[i] > 7:
#         cont +=1

# print('quantidade de medias superiores a 7: ',cont)
# print('Maior media = ',maior)
# gastos = ['Alimentação', 'Água', 'Luz', 'Telefone', 'Internet', 'Outros']


matriz = {}
#primeiro vem a linha, dps a coluna
for i in range(2):
    for j in range(3):
        gst = int(input('>'))
        matriz[(i+1,j+1)]= gst


print(matriz)