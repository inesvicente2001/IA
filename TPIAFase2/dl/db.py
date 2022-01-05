from enum import Enum
from ast import literal_eval as make_tuple
import igraph
from igraph import *
import igraph as ig
import pandas as pd
import random
import tkinter as tk
import networkx
from datetime import time
#from pyvis.network import Network

ruas = pd.read_csv("DB/SantoTirsoStreetsFinal.csv")
conexoes = pd.read_csv("DB/ConexoesRuas.csv")

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

class Servico :
    def __init__(self, classificacao, chegada_a_tempo, penalizacao, transporte ):
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
        self.servicos = []
        self.castigo = 0
        
        
#    def add_encomenda(encomenda):
        
cliente1 = Cliente("Tomás")
cliente2 = Cliente("Miguel")
cliente3 = Cliente("Diogo")

estafeta1 = Estafeta("Jorge")
estafeta2 = Estafeta("Inês")
estafeta3 = Estafeta("Guilherme")

rua1 = Rua("São José","Gualtar",3)
rua2 = Rua("São João","Gualtar",4)
rua3 = Rua("São Pedro","Gualtar",5)

encomenda1 = Encomenda("Cama",90,1050,Transporte(0),time(00,00),cliente1,rua1) 
encomenda2 = Encomenda("Cacto",15,10,Transporte(1),time(14,25),cliente2,rua2)
encomenda3 = Encomenda("Candeeiro",3,25,Transporte(2),time(17,35),cliente3,rua3)

# Let's start the methods.

def add_punishment(x):
    # x is Estafeta
    if (x.servicos.notNull()):
        for y in x.servicos:
            if (not y.chegada):
                x.castigo = x.castigo + y.penalizacao


#Problema : Precisa de uma forma de calcular o tempo e o custo ambos económico e ecológico.
#def back_or_switch():

#Problema : O servico precisa de variáveis que um utilizador precisa de dar para completar a review. Os outros podem ter algumas ideias.
#def new_servico_from_encomenda():

#Problema : Vamos precisar de uma lista de encomendas, o Jorge pode saber disso. Já agora, quantas encomendas é que permitimos por dia? Também devo perguntar.
#def new_encomendas(x):
    
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
    root.destroy()
    prefs["bbox"] = (screen_width, screen_width)
    prefs["layout"] = g.layout("lgl") #circle é mais estético 
    prefs["vertex_label"] = g.vs["rua"] #dizer que a label dos nodos vão ser o nome das ruas(a label é o nome que aparece em baixo dos vértices no grafo)
    prefs["vertex_label_size"] = 7
    #prefs["vertex_color"] = [color_dict[freguesia] for freguesia in g.vs["freguesia"]] #Percorres as freguesias todas do grafo e as que forem "Gualtar" vão passar a "blue" e "Arcozelo" a "pink"
    prefs["edge_label"] = g.es["distancia"] #o label de cada aresta vai ser a distancia
    prefs["edge_label_size"] = 7
    prefs["edge_width"] = [1] * nr_arestas 
    prefs["edge_color"] = ["grey"] * nr_arestas 
    prefs["margin"] = 20
    prefs["vertex_color"] = ["red"] * nr_vertices
    prefs["vertex_color"][g.vs["rua"].index("Green Distribution")] = "green"
    prefs["vertex_size"] = [5] * nr_vertices
    prefs["vertex_size"][g.vs["rua"].index("Green Distribution")] = 20
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
    global nr_arestas
    global nr_vertices
    nr_arestas += len(distancias)
    nr_vertices += 1
    g.save("teste.graphml")
    prefs = create_prefs()
    print(prefs)

    #plot(g, **prefs)
        
#plot(g, layout=layout, bbox=(300, 300), margin=20, target=ax) # matplotlib version
#plot(g, layout=layout)

#print(e)


#variáveis globais
g = create_graph()
nr_vertices = g.vcount()
nr_arestas = g.ecount()
#print(g)

##A = g.get_edgelist()
##G = networkx.Graph(A)
###size = g.vcount()
###
###net = Network(notebook=True)
###net.from_nx(G)
###net.show("example.html")
#
##create_graph()
##create_prefs()
##add_vertice("Arcozelo", "new", ["fds", "desisto"], [3,4])
#
#
#def dfs_aux(g, start, target, path, visited = set()):
#    path.append(start)
#    visited.add(start)
#    if start == target:
#        return path
#    for neighbour in g.neighbors(start):
#        if neighbour not in visited:
#            result = dfs_aux(g, neighbour, target, path, visited)
#            if result is not None:
#                return result
#    path.pop()
#    return None
#
#
#def dfs(target):
#    path = []
#    dfs_aux(g, g.vs["rua"].index("Green Distribution"), g.vs["rua"].index(target), path, set())
#    print(path)
#    #load_search_graph(path)
#    return path
#    
#    
#def load_search_graph(path):
#    prefs = create_prefs()
#    print(path)
#    total_cost = 0
#    
#    
#    for (i, node) in enumerate(path[1:]):
#        prefs["vertex_color"][node] = "blue"
#        prefs["vertex_size"][node] = 20
#        edge_id = g.get_eid(path[i], path[i+1], error = False)
#        prefs["edge_color"][edge_id] = "red"
#        prefs["edge_width"][edge_id] = 4
#        total_cost += g.es["distancia"][edge_id]
#    #prefs["vertex_color"][g.vs["rua"].index("Green Distribution")] = "green"
#    prefs["vertex_color"][path[len(path)-1]] = "yellow"
#    print(total_cost)
#    plot(g, **prefs)
#    
    
#dfs(43)
#plot(path, layout = "tree")

#[vertices, parents] = g.dfs(g.vs["rua"].index("Green Distribution"))



#vertices
#parents
#gaux = g.get_adjacency(type=GET_ADJACENCY_BOTH, attribute=None, default=0, eids=False)
#print(neighbors(g, g.vs[5]))

#print(g.neighbors(g.vs[5]))

#load_graph()



    