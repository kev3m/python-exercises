# def trueOrFalse(num1, num2):
#     if num1 % num2 == 0:
#         return True
#     else:
#         return False

# numero1 = int(input(''))
# numero2 = int(input(''))

# while numero2 != 0:
#     if trueOrFalse(numero1, numero2) == True:
#         print('DIVISIVEL')
#     elif trueOrFalse(numero1, numero2) == False:
#         print('nop')
#     numero1 = int(input(''))
#     numero2 = int(input(''))
   

   
# def quadranteCalc(angulo):
#     if 0 < angulo < 90:
#         return 1
#     elif 90 < angulo < 180:
#         return 2
#     elif 180 < angulo < 270:
#         return 3
#     elif 270 < angulo < 360:
#         return 4
#     elif angulo == 0:
#         return 5
#     elif angulo == 90:
#         return 6
#     elif angulo == 180:
#         return 5
#     elif angulo == 270:
#         return 6
#     elif angulo < 0 or angulo > 360:
#         return -1


# ang = int(input('Aqui: '))

# if quadranteCalc(ang) == 5:
#     print('eixo horizontal')
# elif quadranteCalc(ang) == 6:
#     print('eixo vertical')
# elif quadranteCalc(ang) == -1:
#     print('not an angle, man!')
# else:
#     print(quadranteCalc(ang))


# def fcm(idade,fcr):
#     fct = fcr + 0.6 * ((220 - idade) - fcr)
#     return fct

# age = int(input('Digite sua idade: '))
# freq = int(input('Digite sua frequência cardiaca de repouso: '))

# while age > 0:
#     print('{:.0f}'.format(fcm(age,freq)))
#     age = int(input('Digite sua idade: '))
#     freq = int(input('Digite sua frequência cardiaca de repouso: '))

# def somadospares(n1,n2):
#     soma = 0
#     for i in range(n1, n2+1):
#         if i % 2 == 0:
#             soma += i
#     return soma

# num1 = int(input(''))
# num2 = int(input(''))

# while num1 < num2:
#     print(somadospares(num1, num2))
#     num1 = int(input(''))
#     num2 = int(input(''))

# def existemraizes(a,b,c):
#     delta = b**2 - 4 * (a * c)

#     if delta < 0:
#         return 'nao existem raizes reais'
#     elif delta == 0:
#         return 'existe uma unica raiz'
#     else: 
#         return 'existem duas raizes reais'

# n1, n2, n3 = int(input('')), int(input('')), int(input(''))
# print(existemraizes(n1,n2,n3))

# def ordenando(a,b,c):
#     cresc = []

#     if a > b > c:
#         cresc.append(c)
#         cresc.append(b)
#         cresc.append(a)
#     elif a > c > b:
#         cresc.append(b)
#         cresc.append(c)
#         cresc.append(a)
#     elif c > b > a:
#         cresc.append(a)
#         cresc.append(b)
#         cresc.append(c)
#     elif c > a > b:
#         cresc.append(b)
#         cresc.append(a)
#         cresc.append(c)
#     elif b > a > c:
#         cresc.append(c)
#         cresc.append(a)
#         cresc.append(b)
#     elif b > c > a:
#         cresc.append(a)
#         cresc.append(c)
#         cresc.append(b)
#     return cresc    


# n1, n2, n3 = int(input('')), int(input('')), int(input(''))
# print(*ordenando(n1, n2, n3))

# def existriang(a, b, c):
#     if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
#         return True
#     else:
#         return False

# def classtriang(l1,l2,l3):
#     if l1 ** 2 == l2 **2 + l3**2:
#         return 'retangulo'
#     elif l1 **2 < l2 **2 + l3 **2:
#         return 'acutangulo'
#     elif l1**2 > l2**2 + l3**2:
#         return 'obtusangulo'

# seg1 = int(input('a: '))
# seg2 = int(input('b: '))
# seg3 = int(input('c: '))
# print(existriang(seg1,seg2,seg3))

# while seg1 > 0 and seg2 > 0 and seg3 > 0:
#     if existriang(seg1,seg2,seg3) == True:
#         print(classtriang(seg1,seg2,seg3))
#     elif existriang(seg1,seg2,seg3) == False:
#         print('not a triangle')
#     seg1 = int(input('a: '))
#     seg2 = int(input('b: '))
#     seg3 = int(input('c: '))

# def enesimo(n):
#     enesi = n

#     for i in range(1, n):

#     en = n-1 + n+2
#     return en

# num = int(input(''))
# print(enesimo(num))

# from math import sqrt

# def enesimo(num):
#     return ((1+sqrt(5))**num-(1-sqrt(5))**num)/(2**num*sqrt(5))

# n = int(input(''))
# while n > 0:
#     print('{:.0f}'.format(enesimo(n)))
#     n = int(input(''))