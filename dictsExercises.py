#JOGANDO CARTAS FORA

# pilha = []
# n = int(input(''))
# zero = int(input(''))

# for i in range(1, n+1):
#     pilha.append(i)

# print(pilha)
# descartadas = []

# while len(pilha) >= 2:
#     descart = pilha.pop(0)
#     descartadas.append(descart)
#     swap = pilha.pop(0)
#     pilha.append(swap)

# dscrt = str(descartadas)[1:-1]

# print('descartadas: {}'.format(dscrt))
# print('remanescente: {}'.format(*pilha))

#Fila do Bandejão

# aluno = input('Quem chegou agora? ')
# fila = []
# while aluno:
#     fila.append(aluno)
#     aluno = input('Quem chegou agora? ')
#     if 'Berlina' in fila:
#         fila.remove('Carlen')
#     elif 'Carlen' in fila:
#         fila.remove('Berlina')

# if fila[0] == 'Arbento':
#     swap = fila.pop(0)
#     fila.insert(1,swap)

# print(fila)

#Notação polonesa reversa

# ct = int(input('Num de casos teste: '))
# pilha = []

# count = 0
# while count < ct:
#     addToPilha = int(input('Add> ')) 
#     while addToPilha != '.':    
        
#         pilha.append(addToPilha)
#         addToPilha = int(input('Add> ')) 

#     count += 1

# print(pilha)


