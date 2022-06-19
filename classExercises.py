#BE FIT
from pprint import pprint
from collections import OrderedDict


# class Pessoa:
#     def __init__(self, altura, peso):
#         self.altura = altura
#         self.peso = peso

#     def CalculaIMC(self):
#         imc = self.peso / (self.altura * self.altura)
#         if imc <= 18.4:
#             return 'Abaixo do peso'
#         if  18.5 <= imc <= 24.9:
#             return 'Peso normal'
#         if imc >= 25:
#             return 'Acima do peso'

# altura = float(input(''))
# peso = float(input(''))

# imcCalc = Pessoa(altura, peso)
# print(imcCalc.CalculaIMC())

#PRA ESQUENTAR O CLIMA

# class Temperature:
#     def __init__(self, value, scale):
#         self.value = value
#         self.scale = scale

#     def converter(self):
#         if self.scale == 'C':
#             temp =  (self.value * 1.8) + 32
#         elif self.scale == 'F':
#             temp =  (self.value - 32) / 1.8
#         return temp

#     def altscale(self):
#         if scale == 'C':
#             alt = 'F'
#         elif scale == 'F':
#             alt = 'C'
#         return alt


# value = float(input(''))
# scale = input('')


# conv = Temperature(value,scale)
# alt = conv.altscale()
# print('{} {} = {:.1f} {} '.format(value ,scale, conv.converter(), alt))

#AND THE OSCAR GOES TO

# class Ator:
#     def __init__(self, nome,oscarPr ,oscarCDJ):
#         self.nome = nome
#         self.oscarPr = oscarPr
#         self.oscarCDJ = oscarCDJ


#     def compara(self):
#         prest = (self.oscarPr * 2) + self.oscarCDJ
#         return prest

# def comp():
#     nome = input('')
#     pR = int(input(''))
#     cDJ = int(input(''))
#     return nome, pR, cDJ

# def compara(comp1prest, comp2prest):
#     if comp1prest.compara() > comp2prest.compara(): 
#         return comp1prest.nome
#     elif comp1prest.compara() < comp2prest.compara():
#         return comp2prest.nome
#     else:
#         if (comp1prest.oscarPr + comp1prest.oscarCDJ) > (comp2prest.oscarPr + comp2prest.oscarCDJ):
#             return comp1prest.nome
#         else:
#             return comp2prest.nome
   
    
    
# ator1nome, ator1pr, ator1cdj = comp()
# ator2nome, ator2pr, ator2cdj = comp()

# comp1 = Ator(ator1nome, ator1pr, ator1cdj)
# comp2 = Ator(ator2nome, ator2pr, ator2cdj)

# print(compara(comp1,comp2))

# class Pessoa:
#     id = 1
#     def __init__(self, nome, idade,sexo, salario):
#         self.nome = nome
#         self.idade = idade
#         self.sexo = sexo
#         self.salario = salario


# def funcionarios(obj):
#     lista = []
#     for i in range(10):
#         name = input('')
#         idade = int(input(''))
#         sexo = input('')
#         salario = float(input(''))
#         pp = obj(name,idade,sexo,salario)
#         pp.id += i
#         lista.append(pp)
#     return lista
        
# def calcularMedia(lista):
#     totalFem = 0
#     salarioSum = 0
#     for i in lista:
#         if i.sexo == 'Feminino':
#             totalFem += 1
#             salarioSum += i.salario
#     return (salarioSum / totalFem)

# def maiorSalario(lista):
#     maior = 0
#     for i in lista:
#         if i.salario > maior:
#             maior = i.salario
#     for j in lista:
#         if j.salario == maior:
#             return ('{}, {} anos, sexo {}, recebe {:.2f} reais.'.format(j.nome, j.idade, j.sexo.lower(), j.salario))

# lista = funcionarios(Pessoa)
# print('{:.2f}'.format(calcularMedia(lista)))
# print(maiorSalario(lista))

# class Conta:
#     def __init__(self,nome_usuario,email,senha):
#         self.nome_usuario = nome_usuario
#         self.email = email
#         self.senha = senha
        
# def cadastrar(num,conta):
#     dicio = {}
#     count = 0
#     while count != num:
#         nomeuser = input('')
#         email = input('')
#         senha = input('')
#         pessoa = conta(nomeuser,email,senha)
#         if email in dicio.keys():
#             print('E-mail ja cadastrado')
#         else:
#             dicio[pessoa.email] = pessoa  
#             count += 1
#     return dicio


# n = int(input(''))           
# dicio = cadastrar(n, Conta)
# email = input('')
# try:
#     print(dicio[email].nome_usuario)
# except KeyError:
#     print('E-mail nao cadastrado')

#hora de comer

# class Pedido:
#     id = 0
#     def __init__(self, nome_refeicao,leva_sobremesa, mesa_cliente):
#         self.nome_refeicao = nome_refeicao
#         self.leva_sobremesa = leva_sobremesa
#         self.mesa_cliente = mesa_cliente

# def cadastrar(obj):
#     dicio = {}
#     for i in range(3):
#         nome_refeicao = input('')
#         leva_sobremesa = input('')
#         if leva_sobremesa == 'True':
#             leva_sobremesa = True
#         else:
#             leva_sobremesa = False
#         mesa_cliente = int(input('numero da mesa: '))
#         pedido = obj(nome_refeicao,leva_sobremesa, mesa_cliente)
#         dicio[mesa_cliente] = pedido
#     return dicio

# def sobremesa(dicio):
#     for i in dicio.keys():
#         if dicio[i].leva_sobremesa == True:
#             print('{} para a mesa {}'.format(dicio[i].nome_refeicao, dicio[i].mesa_cliente))

# def removeped(num,dicio):
#     dicio.pop(num, None)
#     return dicio


# dicio = cadastrar(Pedido)
# sobremesa(dicio)
# remove = int(input(''))
# newDicio = removeped(remove,dicio)


# for key in sorted(newDicio.keys()):
#     print('{} para a mesa {}'.format(dicio[key].nome_refeicao, dicio[key].mesa_cliente))
#WHEN YOU PUT MONEY IN THE BANK ANNNDDD IT'S GONE

# class Conta_corrente:
#     def __init__(self,id_pedido,numero_conta, nome_correntista,servicos_extras, saldo_conta):
#         self.id_pedido = 0
#         self.numero_conta = numero_conta
#         self.nome_correntista = nome_correntista
#         self.servicos_extras = servicos_extras
#         self.saldo_conta = saldo_conta

# def cadastrar(object):
#     listaDeContas = []
#     for i in range(3):
#         id += 1
#         numero_conta = 

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
        servicos_extras = input('')
        if servicos_extras == 'True':
            servicos_extras = True
        else:
            servicos_extras = False
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