from enum import Enum
import igraph
from igraph import *

class Cliente:
    def __init__(self, nome): 
        self.nome = nome

class Transporte(Enum):
    Carro = 0
    Mota = 1
    Bicicleta = 2

class Localizacao:
    def __init__(self, rua, freguesia): 
        self.rua = rua 
        self.freguesia = freguesia

    
#N sei se vamos ter uma encomenda a ter um id para não haver repetidos
class Encomenda:
    def __init__(self, nome, peso, volume, transporte, prazo, cliente, ponto_chegada, classificacao): 
        self.nome = nome 
        self.peso = peso
        self.volume = volume
        self.Transporte = transporte #n sei se isto fica aqui
        self.prazo = prazo
        self.cliente = cliente
        self.localizacao = ponto_chegada
        self.classificacao = classificacao  #n sei se isto fica aqui
    
class Estafeta:
    def __init__(self, nome):
        self.nome = nome
        self.classificacao = 0
        self.nr_classificacoes = 0
        self.encomendas = []
        
    def add_encomenda(encomenda):
        

 
#Exemplo para criar uma encomenda   
c = Cliente("joao")
l = Localizacao("Barros", "Gualtar")
e = Encomenda("ola", 21, 21, Transporte.Carro, 21, c, l, 3)

#Isto é um exemplo básico de grafos, há outras maneiras de os definir que se calhar não ficam tão confusos
g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
g.vs["rua"] = ["Sol", "Barros", "Nova", "Presa", "Vilar", "fds", "desisto"] #7 ruas para 7 nodos
g.vs["freguesia"] = ["Gualtar", "Gualtar", "Gualtar", "Gualtar", "Arcozelo", "Arcozelo", "Arcozelo"] #freguesias para os 7 nodos (precisa de ser 7 ao todo)
g.es["distancia"] = [10, 14, 40, 32, 1, 6, 43, 98, 3] #distancia dos vertices

layout = g.layout("kk")
g.vs["label"] = g.vs["rua"] #dizer que a label dos nodos vão ser o nome das ruas(a label é o nome que aparece em baixo dos vértices no grafo)


color_dict = {"Gualtar": "blue", "Arcozelo": "pink"} 
g.vs["color"] = [color_dict[gender] for gender in g.vs["freguesia"]] #Percorres as freguesias todas do grafo e as que forem "Gualtar" vão passar a "blue" e "Arcozelo" a "pink"


g.vs["label_dist"] = [1] * 7  # criar uma lista de 7 elementos com tudo a 1


g.es["label"] = g.es["distancia"] #o label de cada aresta vai ser a distancia
g.es["width"] = [5] * 9
g.es["color"] = ["grey"] * 9

plot(g, layout=layout, bbox=(1000, 1000), margin=20) #funcao para mostrar o grafo

#plot(g, layout=layout, bbox=(300, 300), margin=20, target=ax) # matplotlib version
#plot(g, layout=layout)

#print(e)
    
    
    