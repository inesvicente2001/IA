from enum import Enum
from ast import literal_eval as make_tuple
import igraph
from igraph import *
import pandas as pd
import random
import tkinter as tk
import networkx
from pyvis.network import Network

ruas = pd.read_csv("/home/arkimedez/Desktop/IA/TPIAFase2/DB/SantoTirsoStreetsFinal.csv")
conexoes = pd.read_csv("/home/arkimedez/Desktop/IA/TPIAFase2/DB/ConexoesRuas.csv")

ruas_lst = ruas['rua'].tolist()
freguesias_lst = ruas['freguesia'].tolist()
conexoes_lst_with_quotes = conexoes['Arestas'].tolist()
distancias_lst = conexoes['Distancias'].tolist()

conexoes_lst = [make_tuple(x.strip()) for x in conexoes_lst_with_quotes]

#print(conexoes_lst)

class Cliente:
    def __init__(self, nome): 
        self.nome = nome
        
class Rua:
    def __init__(self, nome, freguesia, nr_entregas):
        self.nome = nome
        self.freguesia = freguesia
        self.nr_entregas = nr_entregas

class Transporte(Enum):
    Carro = 0
    Mota = 1
    Bicicleta = 2


##class Servico(Transporte) #vamos precisar por causa das entregas

##class Localizacao:
##    def __init__(self, rua, freguesia): 
##        self.rua = rua 
##        self.freguesia = freguesia


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
#c = Cliente("joao")
#l = Localizacao("Barros", "Gualtar")
#e = Encomenda("ola", 21, 21, Transporte.Carro, 21, c, l, 3)



#Isto é um exemplo básico de grafos, há outras maneiras de os definir que se calhar não ficam tão confusos
def create_graph():
    g = Graph(conexoes_lst)
    g.vs["rua"] = ruas_lst
    g.vs["freguesia"] = freguesias_lst
    g.es["distancia"] =  distancias_lst #distancia dos vertices
   
    g.save("teste.graphml")
    return g
    #figure(g, layout=layout, bbox=(1000, 1000), margin=20) #funcao para mostrar o grafo
    

def create_prefs():
    #g = Graph.Read_GraphML("teste.graphml")
    color_dict = {"Gualtar": "green", "Arcozelo": "pink"} 
    prefs = {}
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    prefs["bbox"] = (screen_width, screen_width)
    prefs["layout"] = g.layout("circle")
    prefs["vertex_label"] = g.vs["rua"] #dizer que a label dos nodos vão ser o nome das ruas(a label é o nome que aparece em baixo dos vértices no grafo)
    prefs["vertex_label_size"] = 20
    #prefs["vertex_color"] = [color_dict[freguesia] for freguesia in g.vs["freguesia"]] #Percorres as freguesias todas do grafo e as que forem "Gualtar" vão passar a "blue" e "Arcozelo" a "pink"
    prefs["edge_label"] = g.es["distancia"] #o label de cada aresta vai ser a distancia
    prefs["edge_label_size"] = 20
    prefs["edge_width"] = 1
    prefs["edge_color"] = "grey" 
    prefs["margin"] = 20
    prefs["vertex_color"] = ["red"] * 698
    prefs["vertex_color"][g.vs["rua"].index("Green Distribution")] = "green"
    prefs["vertex_size"] = [30] * 698
    prefs["vertex_size"][g.vs["rua"].index("Green Distribution")] = 35
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
#print(g)

##A = g.get_edgelist()
##G = networkx.Graph(A)
##size = g.vcount()
##
##net = Network(notebook=True)
##net.from_nx(G)
##net.show("example.html")

#create_graph()
#create_prefs()
#add_vertice("Arcozelo", "new", ["fds", "desisto"], [3,4])


[vertices, parents] = g.dfs(g.vs["rua"].index("Green Distribution"))

vertices
parents

print(vertices)
print(parents)

load_graph()



    