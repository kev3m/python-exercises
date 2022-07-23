###########Exec 1########################

# n1 = int(input('Digte o primeiro número:'))
# n2 = int(input())

# for i in range(n1+1, n2-1):
#    if i % 7 == 0:
#       print('{} '.format(i), end="")
   

########Exec 4############################### 
   


# numA = int(input())
# numB = int(input())
# soma = 0

# for i in range(numA,numB+1):
#     soma += i
    
# print(soma)

########Exec 6############################### 

# n = int(input())
# primos = []

# for num in range(1,n+1):
#    cont=0
#    for divisor in range(1, num+1):
#         if num % divisor == 0:
#            cont += 1
#            if cont == 2:
#                primos.append(num)
#                print(primos)



# '''Escreva um programa em Python que leia uma quantidade n de pessoas entrevistadas. Em seguida, para cada pessoa leia a idade e o sexo, e calcule e mostre:

#     A média de idade das pessoas;
#     A média de idade das mulheres;
#     A média de idade dos homens;
#     A quantidade de pessoas em cada faixa etária segundo a tabela a seguir;
#     A porcentagem de homens da quarta faixa etária.

# 1 	Até 15 anos
# 2 	De 16 a 30 anos
# 3 	De 31 a 45 anos
# 4 	De 46 a 60 anos
# 5 	Acima de 60 anos

# Quando o usuário for inserir a informação "Sexo" as entradas que devem ser usadas são: "Homem" e "Mulher";
# '''


# quantas_pessoas = int(input('Quantas pessoas? '))
# idade_pessoas = 0
# idade_mulheres = 0
# soma_mulheres = 0
# idade_homens = 0
# soma_homens = 0
# faixa_etaria1 = 0
# faixa_etaria2 = 0
# faixa_etaria3 = 0
# faixa_etaria4 = 0
# faixa_etaria5 = 0
# homens_faixa4 = 0

# '''1 	Até 15 anos
# 2 	De 16 a 30 anos
# 3 	De 31 a 45 anos
# 4 	De 46 a 60 anos
# 5 	Acima de 60 anos'''
        
      

# divisores = []


# num_fornecidos = int(input('Digite a quantidade de números: '))

# for n in range(num_fornecidos):
#     n = int(input('Digite um número:'))
#     num.append(n)
#     print(num)

# for elemento in num:
#     for i in range(1, elemento-1):
#         if elemento % i == 0:
#             print(i)   

########Exec 10############################### 

# n = int(input('Digite o número de termos: '))


# for i in range(n):
#     i = n * 0.5

# print('{:.1f}'.format(i))


########Exec 11############################### 
# num = []
# divisores = []


# num_fornecidos = int(input('Digite a quantidade de números: '))

# for n in range(num_fornecidos):
#     n = int(input('Digite um número:'))
#     num.append(n)
#     print(num)

# for elemento in num:
#     for i in range(1, elemento-1):
#         if elemento % i == 0:
#             print(i)   
            

########Exec 3############################### 

# n = int(input()) 
# m = int(input()) 

# if n < m:
#    for i in range(n,m+1, 1):
#     i = (i - 32) * (5/9)
#     print('{:.0f} {:.1f}'.format(i * 1.8 + 32, i))
# elif n > m:
#    for i in range(n,m-1, -1):
#       i = (i - 32) * (5/9)
#       print('{:.0f} {:.1f}'.format(i * 1.8 + 32, i))

    



########Exec 7############################### 

# notas_boas = 0
# notas_medias = 0
# notas_ruins = 0
# media = 0

# for i in range(1,10+1):
#     i = float(input('Digite uma nota: '))
#     if i >= 7:
#         notas_boas = notas_boas + 1
#         media = media + i
#     elif i >= 3 and i < 7:
#         notas_medias = notas_medias + 1
#         media = media + i
#     else:
#         notas_ruins = notas_ruins + 1
#         media = media + i

# media = media / 10

# print(notas_boas) 
# print(notas_medias) 
# print(notas_ruins) 
# print(round(media,1))

########Exec 8############################### 


# retorno = []

# for notas in range(1,10+1):
#     notas = float(input('Digita uma nota ai filho de uma putaaaa: '))
#     if notas >= 7:
#         retorno.append('APROVADO')
#     elif notas >= 3 and notas < 7:
#         retorno.append('FINAL')
#     else:
#         retorno.append('REPROVADO')

# for lista in retorno:
#     print(lista)
########Exec 2############################### 

# lista = []

# for i in range(1,10+1):
#     i = float(input('Digita algo: '))
#     lista.append(i)

# print (max(lista))
# print (min(lista))
    
#################Exec 7################
# numero = int(input("Digite um numero qualquer: "))
# quantidadeDeNumerosImpares = 0
# soma = 0

# for num in range(1, numero,2):
#   if soma < numero:
#     soma += num
#     if soma <= numero:
#       quantidadeDeNumerosImpares+=1


# print(quantidadeDeNumerosImpares)

# quantiaFaltas = 0
# quantiaFaltastotal = 0
# totalalunos = 0

# while quantiaFaltas >= 0:
#   quantiaFaltas = int(input("Falta: "))
#   if quantiaFaltas >= 0:
#     quantiaFaltastotal += quantiaFaltas
#     totalalunos += 1

# print(quantiaFaltastotal / totalalunos)
# print(totalalunos)

# ladoA = float(input())
# ladoB = float(input())
# ladoC = float(input())


# print("Entradas: {}, {}, {}".format(ladoA, ladoB, ladoC))
# if ladoA == ladoB == ladoC:
#   print('Tipo de triangulo: equilatero')
# elif ladoA <= 0 or ladoB  <= 0 or ladoC <= 0 or ladoA >= (ladoB + ladoC) or ladoB >= (ladoA + ladoC) or ladoC >= (ladoA + ladoB):
#   print('Tipo de triangulo: invalido')
# elif ladoA != ladoB != ladoC:
#   print('Tipo de triangulo: escaleno')
# else:
#   print('Tipo de triangulo: isosceles')

##EXEC 2 ######
# consumo = float(input())
# tipo = input("digite R ou I ou C: ")


# print("Entradas: {} kWh e tipo {},".format(consumo, tipo))
    

# if tipo == 'R':
#   if consumo <= 500:
#     consumo = consumo * 0.44
#   elif consumo > 500:
#     consumo = consumo * 0.65
# if tipo == 'C':
#   if consumo <= 1000:
#     consumo = consumo * 0.55
#   elif consumo > 1000:
#     consumo = consumo * 0.60
# if tipo == 'I':
#   if consumo <= 5000:
#     consumo = consumo * 0.55
#   elif consumo > 5000:
#     consumo = consumo * 0.60

# if tipo == 'I' or tipo == 'C' or tipo == 'R':
#   print("Valor total: R$ {:.2f}".format(consumo))  
# else:
#   print('Dados invalidos')
    
#####exec 3#############
  
numX = float(input())
numA = float(input())
numB = float(input())

if numX >= numA and numX <= numB:
  print("{} pertence ao intervalo {} , {}".format(numX, numA, numB))
elif numA >= numB:
  print("Entradas {} e {} invalidas".format(numA, numB))
else: 
  print("{} não pertence ao intervalo {} , {}".format(numX, numA, numB))

