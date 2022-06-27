import pickle

class Disciplinas:
    def __init__(self,nome,dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade

def cadDis(obj,n):
    listadeDis = []
    for i in range(n):
        nomedadis = input('digite o nome da disciplina: ')
        dificuldadedadis = int(input('digite a dificuldade: '))
        assert 0 <=dificuldadedadis <= 5
        discip = obj(nomedadis,dificuldadedadis)
        listadeDis.append(discip)
    return listadeDis

n = int(input('quantas pegou cumpadi: '))
lista = cadDis(Disciplinas,n)

with open('disciplinas.bin', 'w+b') as disciplinas:
    pickle.dump(lista, disciplinas)


listabin = pickle.load(open('disciplinas.bin', 'rb'))    
for i in listabin:
    print(i.nome)
    print(i.dificuldade)