##### Exec 1 ###########################

# num1 = int(input())
# num2 = int(input())

# if (num1 * num2) % 2 == 0:
#     print(num1 + num2)
# elif (num1 * num2) % 2 != 0:
#     print(num2 - num1)

##### Exec 2 ###########################

# patrono = input()

# if patrono == "cervo":
#     print("{} eh patrono do Harry Potter.".format(patrono))
# else: 
#     print("{} nao eh patrono do Harry Potter".format(patrono))

##### Exec 3 ###########################

#Celsius para - F = C/5 = F-32/9
#Simplificado - F = C *1.8 = 32


# escala = input()
# temp = float(input())
# F = (temp * 1.8) + 32

# if escala.lower() == "c":
#     temp = F
#     print(round(temp, 1))
# elif escala.lower() == "f":
#     temp = (temp - 32) / 1.8
#     print(round(temp, 1))

##### Exec 4 ###########################

# altura = float(input())
# sexo = input()


# if sexo.lower() == "m":
#     altura = (72.7 * altura) - 58
#     print(round(altura, 2))
# elif sexo.lower() == "f":
#     altura = (62.1 * altura) - 44.7
#     print(round(altura, 2))

##### Exec 5 ###########################

# num = int(input())
# newNum = num % 100
# # if 100 <= num or num <= 999:
# #     num = num % 100
# #     print(num)
# # if num % 100 == 0:
# #     print("Zero não é divisor")
# # elif 100 <= num or num <= 999:
# #     num = num % 100
# #     print(num)

# if num % newNum == 0:
#     print("SIM") 
# else:
#     print("NAO")


##### Exec 6 ###########################

# numA = int(input())
# numB = int(input())
# numC = int(input())

# if numA > numB and numB > numC:
#     print(int(numB))
# elif numA > numC and numC > numB:
#     print(int(numC))
# elif numB > numA and numA > numC:
#     print(int(numA))
# elif numC > numA  and numA > numB:
#     print(int(numA))
# else:
#     print(int(numB))


dicio = {}

for i in range(3):
    for j in range(3):
        dicio[(i+1,j+1)] = 0

print(dicio)