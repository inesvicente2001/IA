from enum import Enum
import igraph
from igraph import *

class Cliente:
    def __init__(self, nome): 
        self.nome = nome
        
class Rua:
    def __init__(self, nome, nr_entregas):
        self.nome = nome
        self.nr_entregas = nr_entregas

class Transporte(Enum):
    Carro = 0
    Mota = 1
    Bicicleta = 2

class Localizacao:
    def __init__(self, rua, freguesia): 
        self.rua = rua 
        self.freguesia = freguesia


class Servico :
    def __init__(self, classificacao, chegada_a_tempo, penalizacao, transporte):
        self.classificacao = classificacao
        self.chegada = chegada_a_tempo
        self.penalizacao = penalizacao
        self.transporte = transporte    
    
#N sei se vamos ter uma encomenda a ter um id para não haver repetidos
class Encomenda:
    def __init__(self, nome, peso, volume, transporte, prazo, cliente, ponto_chegada): 
        self.nome = nome 
        self.peso = peso
        self.volume = volume
        self.transporte = transporte #n sei se isto fica aqui
        self.prazo = prazo
        self.cliente = cliente
        self.localizacao = ponto_chegada
    
class Estafeta:
    def __init__(self, nome):
        self.nome = nome
        self.classificacao = 0
        self.nr_classificacoes = 0
        self.encomendas = []
        self.registos = []
        self.castigo = 0
        
#    def add_encomenda(encomenda):
        

 
#Exemplo para criar uma encomenda   
c = Cliente("joao")
l = Localizacao("Barros", "Gualtar")
e = Encomenda("ola", 21, 21, Transporte.Carro, 21, c, l, 3)

#Isto é um exemplo básico de grafos, há outras maneiras de os definir que se calhar não ficam tão confusos
def create_graph():
    g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
    g.vs["rua"] = ["Sol", "Barros", "Nova", "Presa", "Vilar", "fds", "desisto"] #7 ruas para 7 nodos
    g.vs["freguesia"] = ["Gualtar", "Gualtar", "Gualtar", "Gualtar", "Arcozelo", "Arcozelo", "Arcozelo"] #freguesias para os 7 nodos (precisa de ser 7 ao todo)
    g.es["distancia"] = [10, 14, 40, 32, 1, 6, 43, 98, 3] #distancia dos vertices
   
    g.save("teste.graphml")
    return g
    #figure(g, layout=layout, bbox=(1000, 1000), margin=20) #funcao para mostrar o grafo
    
def create_prefs():
    #g = Graph.Read_GraphML("teste.graphml")
    color_dict = {"Gualtar": "blue", "Arcozelo": "pink"} 
    prefs = {}
    prefs["layout"] = g.layout("kk")
    prefs["vertex_label"] = g.vs["rua"] #dizer que a label dos nodos vão ser o nome das ruas(a label é o nome que aparece em baixo dos vértices no grafo)
    prefs["vertex_color"] = [color_dict[freguesia] for freguesia in g.vs["freguesia"]] #Percorres as freguesias todas do grafo e as que forem "Gualtar" vão passar a "blue" e "Arcozelo" a "pink"
    prefs["edge_label"] = g.es["distancia"] #o label de cada aresta vai ser a distancia
    prefs["edge_width"] = 3
    prefs["edge_color"] = "grey" 
    prefs["margin"] = 20
    prefs["vertex_size"] = 20
    return prefs
    

def load_graph():
    g = Graph.Read_GraphML("teste.graphml")
    prefs = create_prefs()
    plot(g, **prefs) #funcao para mostrar o grafo
    
def add_vertice(freguesia, new_vertice, vertices, distancias):
    #g = Graph.Read_GraphML("teste.graphml")
    sizeV = g.vcount()
    sizeE = g.ecount()
    print(g.vs["rua"])
    g.add_vertices(1)
    print(new_vertice)
    g.vs[sizeV]["rua"] = new_vertice
    g.vs[sizeV]["freguesia"] = freguesia
    print(g.vs["rua"])
    vertices_id = []
    for i, vertice_to_add in enumerate(vertices):
        print(vertice_to_add)
        g.add_edge(g.vs[sizeV], g.vs["rua"].index(vertice_to_add))
        g.es[i+sizeE]["distancia"] = distancias[i]
    g.save("teste.graphml")
    prefs = create_prefs()
    print(prefs)

    #plot(g, **prefs)
        
#plot(g, layout=layout, bbox=(300, 300), margin=20, target=ax) # matplotlib version
#plot(g, layout=layout)

#print(e)


#variáveis globais
g = create_graph()
size = g.vcount()

create_graph()
create_prefs()
#add_vertice("Arcozelo", "new", ["fds", "desisto"], [3,4])
#load_graph()
    
    
    