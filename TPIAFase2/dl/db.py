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
clientes = pd.read_csv("DB/Clientes.csv")
encomendas = pd.read_csv("DB/Encomendas.csv")
estafetas = pd.read_csv("DB/Estafetas.csv")
servicos = pd.read_csv("DB/Servicos.csv")


clientes_lst = clientes['nome'].tolist()
ruas_lst = ruas['rua'].tolist()
freguesias_lst = ruas['freguesia'].tolist()
coordenadas_lst_with_quotes = ruas['coordenadas'].tolist()
conexoes_lst_with_quotes = conexoes['Arestas'].tolist()
distancias_lst = conexoes['Distancias'].tolist()


conexoes_lst = [make_tuple(x.strip()) for x in conexoes_lst_with_quotes]
coordenadas_lst = [make_tuple(y.strip()) for y in coordenadas_lst_with_quotes]

#print(conexoes_lst)
#print(coordenadas_lst)
def create_clientes(clientes):
    cliente_class = []
    for cliente in clientes:
        client = Cliente(cliente)
        cliente_class.append(client)
    return cliente_class

def get_client_by_name(name):
    for client in clientes_final:
        if client.nome == name:
            return client

def create_encomendas(encomendas):
    encomendas_class = []
    for index, row in encomendas.iterrows():
        client = get_client_by_name(row[5])
        tempoAux = row[6]
        #print(tempoAux)
        tempo = tempoAux.split(";") 
        tempo_final = time(int(tempo[0]), int(tempo[1]))
        #print(tempo_final)
        encomendas_class.append(Encomenda(row[0],row[1],row[2],row[3],row[4],client,tempo_final,row[7]))
    return encomendas_class

def create_servicos(s):
    lista = []
    for index, row in s.iterrows():
        if row[4] == "true":
            c = True
        else:
            c = False        
        if row[6] == "carro":
            t = Transporte.Carro
        elif row[6] == "mota":
            t = Transporte.Mota
        else:
            t = Transporte.Bicicleta
        lista.append(Servico(row[0],row[1],row[2],row[3],c,row[5], t))
    return lista

def get_encomenda_by_id(i):
    for e in encomendas_final:
        if e.id == int(i):
            return e

def find_encomendas(e):
    package = [] #Estou a ficar sem nomes para variaveis
    split = e.split(";")
    for s in split:
        package.append(get_encomenda_by_id(s))
    return package

def get_servico_by_id(ow):
    for s in servicos_final:
        print(s)
        if s.id == int(ow):
            return s
    
def find_servicos(s):
    package = []
    split = s.split(";")
    for aux in split:
        package.append(get_servico_by_id(aux))
    return package

def create_estafetas(estafetas):
    estafetas_class = []
    for index, row in estafetas.iterrows():
        e = row[3]
        s = row[4]
        if e != ";":
            es_en = find_encomendas(e)
        else:
            es_en = []
        if s != ";":
            es_s = find_servicos(s)
        else:
            es_s = []
        estafetas_class.append(Estafeta(row[0],row[1],row[2],es_en, es_s, row[5]))
    return estafetas_class




class Cliente:
    def __init__(self, nome): 
        self.nome = nome


class Transporte(Enum):
    Carro = 0
    Mota = 1
    Bicicleta = 2

class Servico :
    def __init__(self, index, nome, rua ,classificacao, chegada_a_tempo, penalizacao, transporte):
        self.id = index
        self.nome = nome
        self.rua = rua
        self.classificacao = classificacao
        self.chegada = chegada_a_tempo
        self.penalizacao = penalizacao
        self.transporte = transporte

#N sei se vamos ter uma encomenda a ter um id para não haver repetidos
class Encomenda:
    def __init__(self,index,nome,peso,volume,rua,cliente,prazo,urgencia):
        self.id = index
        self.nome = nome 
        self.peso = peso
        self.volume = volume
        self.rua = rua
        self.cliente = cliente
        self.prazo = prazo
        self.urgencia = urgencia
    
class Estafeta:
    def __init__(self, nome, classificacao, nr_classificacoes, encomendas, servicos, castigo):
        self.nome = nome
        self.classificacao = classificacao
        self.nr_classificacoes = nr_classificacoes
        self.encomendas = encomendas
        self.servicos = servicos
        self.castigo = castigo
        
        
#    def add_encomenda(encomenda):
        
clientes_final = create_clientes(clientes_lst)
encomendas_final = create_encomendas(encomendas)
servicos_final = create_servicos(servicos)
estafetas_final = create_estafetas(estafetas)

    
def get_client_names():
    nomes = []
    for c in clientes_final:
        nomes.append(c.nome)
    return nomes

def add_cliente(nome):
    clientes_final.append(Cliente(nome))
    names = get_client_names()
    aux = pd.DataFrame(names, columns = ['nome']) 
    aux.to_csv('DB/Clientes.csv', index=False)   


def convert_estafetas(estafetas):
    lista = []
    for e in estafetas:
        l_aux = []
        l_aux.append(e.nome)
        l_aux.append(e.classificacao)
        l_aux.append(e.nr_classificacoes)
        if e.encomendas == []:
            l_aux.append(";")
        else:
            string = ""
            for en in e.encomendas:
                string += str(en.id)
                string += ";"
            string = string[:-1]
            l_aux.append(string)
        if e.servicos == []:
            l_aux.append(";")
        else:
            string = ""
            for en in e.servicos:
                string += str(en.id)
                string += ";"
            string = string[:-1]
            l_aux.append(string)
        l_aux.append(e.castigo)
        lista.append(l_aux)
    print(lista)  
    return lista  
            
def add_estafeta(nome):
    estafetas_final.append(Estafeta(nome, 0, 0, [], [], 0))
    lista_estafetas = convert_estafetas(estafetas_final)
    df = pd.DataFrame(lista_estafetas, columns=['nome','classificacao','nr_classificacao','encomendas','servicos','castigo'])
    df.to_csv('DB/Estafetas.csv', index=False)
    
def get_estafetas_names():
    nomes = []
    for e in estafetas_final:
        nomes.append(e.nome)
    return nomes

def get_client_names():
    nomes = []
    for c in clientes_final:
        nomes.append(c.nome)
    return nomes
    
#add_estafeta("JOJO")

def filtra_estafetas_peso(encomenda):
    final = []
    for e in estafetas_final:
        soma = 0
        for p in e.encomendas:
            soma += p.peso
        if soma + encomenda.peso < 100:
            final.append(e)
    return final

def get_classificacoes_estafeta(estafetas):
    lista = []
    for e in estafetas:
        lista.append(e.classificacao)
    return lista

def add_encomenda_to_estafeta(encomenda):
    e_copy = filtra_estafetas_peso(encomenda)
    print(e_copy)
    classificacoes = get_classificacoes_estafeta(e_copy)
    print(classificacoes)
    print(classificacoes.index(max(classificacoes)))
    melhor_estafeta = e_copy[classificacoes.index(max(classificacoes))]
    for e in estafetas_final:
        if e.nome == melhor_estafeta.nome :
            e.encomendas.append(encomenda)
            print(e)
    lista_estafetas = convert_estafetas(estafetas_final)
    df = pd.DataFrame(lista_estafetas, columns=['nome','classificacao','nr_classificacao','encomendas','servicos','castigo'])
    df.to_csv('DB/Estafetas.csv', index=False)
    
        
    
    
        


def convert_encomendas(encomendas):
    lista = []
    for e in encomendas:
        l_aux = []
        l_aux.append(e.id)
        l_aux.append(e.nome)
        l_aux.append(e.peso)
        l_aux.append(e.volume)
        l_aux.append(e.rua)
        l_aux.append(e.cliente.nome)
        string = ""
        string = str(e.prazo.hour) + ";" + str(e.prazo.minute)
        l_aux.append(string)
        l_aux.append(e.urgencia)
        lista.append(l_aux)
    return lista
 
def add_encomenda(nome, peso, volume, rua, client_nome, horas, minutos):
    tempo = time(horas, minutos)
    i = encomendas_final[-1].id
    encomenda = Encomenda(i+1, nome, peso, volume, rua, Cliente(client_nome), tempo, 0)
    encomendas_final.append(encomenda)
    add_encomenda_to_estafeta(encomenda)
    lista_encomendas = convert_encomendas(encomendas_final)
    df = pd.DataFrame(lista_encomendas, columns=['id','nome','peso','volume','rua','cliente','prazo','urgencia'])
    df.to_csv('DB/Encomendas.csv', index=False)
    

    
#TODO fazer o add_encomenda e o add_servico 
#estafeta1 = Estafeta("Jorge")
#estafeta2 = Estafeta("Inês")
#estafeta3 = Estafeta("Guilherme")
#estafetas = [estafeta1, estafeta2, estafeta3]

#rua1 = Rua("São José","Gualtar",3)
#rua2 = Rua("São João","Gualtar",4)
#rua3 = Rua("São Pedro","Gualtar",5)
#ruas = [rua1, rua2, rua3]
#
#encomenda1 = Encomenda("Cama",90,1050,Transporte(0),time(00,00),cliente1,rua1) 
#encomenda2 = Encomenda("Cacto",15,10,Transporte(1),time(14,25),cliente2,rua2)
#encomenda3 = Encomenda("Candeeiro",3,25,Transporte(2),time(17,35),cliente3,rua3)
#encomendas = [encomenda1, encomenda2, encomenda3]

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
    g.vs["coordenadas"] = coordenadas_lst
    g.es["distancia"] =  distancias_lst #distancia dos vertices
   
    g.save("teste.graphml")
    return g
    #figure(g, layout=layout, bbox=(1000, 1000), margin=20) #funcao para mostrar o grafo
    

def create_prefs():
    #g = Graph.Read_GraphML("teste.graphml")
    #color_dict = {"Gualtar": "green", "Arcozelo": "pink"} 
    prefs = {}
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    prefs["bbox"] = (screen_width, screen_width)
    #prefs["layout"] = g.layout("lgl") #circle é mais estético 
    prefs["layout"] = g.layout("lgl") 
    prefs["vertex_label"] = g.vs["rua"] #dizer que a label dos nodos vão ser o nome das ruas(a label é o nome que aparece em baixo dos vértices no grafo)
    prefs["vertex_label_size"] = 7
    #prefs["vertex_color"] = [color_dict[freguesia] for freguesia in g.vs["freguesia"]] #Percorres as freguesias todas do grafo e as que forem "Gualtar" vão passar a "blue" e "Arcozelo" a "pink"
    prefs["edge_label"] = [ '%.2f' % elem for elem in g.es["distancia"] ]  #o label de cada aresta vai ser a distancia
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



    