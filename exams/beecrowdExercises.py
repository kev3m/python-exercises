#1035
# valA, valB, valC, valD = map(int, input().split())


# if valB > valC and valD > valA and (valC + valD) > (valA + valB) and valC > 0 and valD > 0:
#     print('Valores aceitos')
# else:
#     print("Valores nao aceitos")

#1038
# codigo, quantidade = map(int, input().split())

# total = 0
# if codigo == 1:
#     total = quantidade * 4
# elif codigo == 2:
#     total = quantidade * 4.5
# elif codigo == 3:
#     total = quantidade * 5
# elif codigo == 4:
#     total = quantidade * 2
# elif codigo == 5:
#     total = quantidade * 1.5

# print(f"Total: R$ {total:.2f}")

#1045

# A, B, C = map(float, input().split())
# var = [A, B , C]
# var.sort(reverse=True)

# A = var[0]
# B = var[1]
# C = var[2]

# if A >= (B + C):
#     print('NAO FORMA TRIANGULO')
# elif A**2 == B**2 + C**2:
#     print('TRIANGULO RETANGULO')
# elif A**2 > (B**2) + (C**2):
#     print('TRIANGULO OBTUSANGULO')
# elif A**2 < (B**2) + (C**2):
#     print('TRIANGULO ACUTANGULO')

# if A == B == C:
#     print('TRIANGULO EQUILATERO')
# elif A == B or A == C or B == C or B == C:
#     print('TRIANGULO ISOSCELES')

#1042
# A, B, C = map(int, input().split())
# cres = [A, B , C]
# cres.sort()
# for i in cres:
#     print(i)
# print()
# normal = [A, B , C]
# for i in normal:
#     print(i)

#1050

# A = map(int, input().split())
# A = int(input())

# if A == 61:
#     print('Brasilia')
# elif A == 71:
#     print('Salvador')
# elif A == 11:
#     print('Sao Paulo')
# elif A == 21:
#     print('Rio De Janeiro')
# elif A == 32:
#     print('Juiz de Fora')
# elif A == 19:
#     print('Campinas')
# elif A == 27:
#     print('Vitoria')
# elif A == 31:
#     print('Belo Horizonte')
# else:
#     print('DDD nao cadastrado')

#1828

# T = int(input())

# for i in range(1, T + 1):
#     i = sheld, raj = input().split()
    
#     if sheld == 'papel' and raj == 'pedra' or raj =='spock':
#         print('Caso #1: Bazinga!')
#     elif sheld == 'pedra' and raj == 'lagarto' or raj == 'tesoura':
#         print('Caso #1: Bazinga!')
#     elif sheld == 'tesoura' and raj == 'papel' or raj == 'lagarto':
#         print('Caso #1: Bazinga!')
#     elif sheld == 'spock' and raj == 'tesoura' or raj == 'pedra':
#         print('Caso #1: Bazinga!')
#     elif sheld == 'lagarto' and raj == 'spock' or raj == 'papel':
#         print('Caso #1: Bazinga!')
#     elif sheld == 'papel' and raj == 'tesoura' or raj == 'lagarto':
#         print('Caso #2: Raj trapaceou!')
#     elif sheld == 'pedra' and raj == 'papel' or raj == 'spock':
#         print('Caso #2: Raj trapaceou!')
#     elif sheld == 'tesoura' and raj == 'pedra' or raj == 'spock':
#         print('Caso #2: Raj trapaceou!')
#     elif sheld == 'spock' and raj == 'papel' or raj == 'lagarto':
#         print('Caso #2: Raj trapaceou!')
#     elif sheld == 'lagarto' and raj == 'tesoura' or raj == 'pedra':
#         print('Caso #2: Raj trapaceou!')
#     else:
#         print('Caso #3: De novo!')

T = int(input())

for i in range(1, T + 1):
    i = A, B, C = int(input()), input(), int(input())
    print(i)