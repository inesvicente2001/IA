import sys
sys.path.insert(1, 'dl')
from db import *
import math
from enum import Enum
from ast import literal_eval as make_tuple
import igraph
from igraph import *
import igraph as ig
import pandas as pd
import random
import tkinter as tk
import networkx
from queue import Queue
from itertools import groupby 
from queue import PriorityQueue
####################################################################################################


def dfs_aux(g, start, target, path, visited = set()):
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for neighbour in g.neighbors(start):
        if neighbour not in visited:
            result = dfs_aux(g, neighbour, target, path, visited)
            if result is not None:
                return result
    path.pop()
    return None


def dfs(start, target):
    path = []
    dfs_aux(g, g.vs["rua"].index(start), g.vs["rua"].index(target), path, set())
    #print(path)
    #load_search_graph(path)
    return path
    


####################################################################################################


def load_search_graph(path, names):
    prefs = create_prefs()
    ids_target = [] #ids dos targets
    total_cost = 0
    for name in names:
        print(name)
        ids_target.append(g.vs["rua"].index(name))
    print(ids_target)
    
    for (i, node) in enumerate(path[1:]):
        if node==697: 
            print("oof")
        prefs["vertex_color"][node] = "blue"
        prefs["vertex_size"][node] = 20
        edge_id = g.get_eid(path[i], path[i+1])
        total_cost += g.es["distancia"][edge_id]
        prefs["edge_color"][edge_id] = "red"
        prefs["edge_width"][edge_id] = 4
    #prefs["vertex_color"][g.vs["rua"].index("Green Distribution")] = "green"
    prefs["vertex_color"][path[len(path)-1]] = "yellow"
    prefs["vertex_color"][g.vs["rua"].index("Green Distribution")] = "green"
    #print(path)
    print("{:.2f}". format(total_cost)) # para ser dado print só com 2 casas decimais
    for i in ids_target:
        prefs["vertex_color"][i] = "yellow"
    plot(g, **prefs)



####################################################################################################

def bfs_aux(graph, start_node, target_node):
    # Set of visited nodes to prevent loops30
    visited = set()
    queue = Queue()

    # Add the start_node to the queue and visited list
    queue.put(start_node)
    visited.add(start_node)
    
    # start_node
    parent = dict()
    parent[start_node] = None

    # Perform step 3
    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == target_node:
            path_found = True
            break

        for next_node in g.neighbors(current_node):
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)
                
    # Path reconstruction
    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node]) 
            target_node = parent[target_node]
        path.reverse()
    return path



def bfs(start, target):
    path = bfs_aux(g, g.vs["rua"].index(start), g.vs["rua"].index(target))
    #print(path)
    #load_search_graph(path)
    return path


####################################################################################################

# heuristic function with equal values for all nodes
def heuristic(vertix,goal,graph):
    #Heuristica com todos os nodos a 1 ou a 0, consoante o valor que se coloque lá
    #H = dict.fromkeys(g.vs.indices, 1)
    #return H[n]

    #Heuristica com distância Euclideana
    #D é o número de vizinhos do nodo n

    coordenadas_vertix = graph.vs["coordenadas"][vertix]
    coordenadas_goal = graph.vs["coordenadas"][goal]

    dx = abs(coordenadas_vertix[0] - coordenadas_goal[0])
    dy = abs(coordenadas_vertix[1] - coordenadas_goal[1])
    D = len(graph.neighbors(vertix))
    #D = 1
    return D * math.sqrt(dx * dx + dy * dy)


def a_star_algorithm(start, target):
    path = a_star_algorithm_aux(g, g.vs["rua"].index(start), g.vs["rua"].index(target))
    #print(path)
    #load_search_graph(path)
    return path


def a_star_algorithm_aux(graph, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + heuristic(v,stop_node,graph) < g[n] + heuristic(n,stop_node,graph):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            lst_neighbors = graph.neighbors(n)
            lst_distances = []
            for i in range(len(lst_neighbors)):
                lst_distances.append(graph.es["distancia"][lst_neighbors[i]])

            lst_tuples_node_distance = tuple(zip(lst_neighbors, lst_distances))
            for (m, weight) in lst_tuples_node_distance :
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

#calcula o custo de um caminho
def calcula_custo(path):
    total_cost = 0
    for (i, smt) in enumerate(path[1:]):
        edge_id = g.get_eid(path[i], path[i+1])
        total_cost += g.es["distancia"][edge_id]
    return total_cost

def travessia_varias_encomendas_distancia_dfs(encomendas):
    custo_total = 0
    path_completo = [] #path completo a passar em todas as encomendas
    paths = [] #paths em cada for loop
    nome = "Green Distribution" #nodo inicial
    custos = [] #lista que vai ter os custos de todas as encomendas
    #fazer travessia do Green Distribution a todas as encomendas
    while encomendas :
        for encomenda in encomendas:
            path = dfs(nome, encomenda)
            paths.append(path)
            custo = calcula_custo(path)
            custos.append(custo)
            path = []
        id_menor_custo = custos.index(min(custos))
        nome = encomendas.pop(id_menor_custo)
        path_completo += paths[id_menor_custo]
        print(paths[id_menor_custo])
        custo_total += min(custos)
        custos = []
        paths = []
    final_path = [i[0] for i in groupby(path_completo)]
    return final_path


def travessia_varias_encomendas_distancia(encomendas_nomes, procura, estafeta):
    veiculo = escolhe_veiculo_velocidade(estafeta)
    peso_total = 0
    custo_total = 0
    tempo = 0
    path_completo = [] #path completo a passar em todas as encomendas
    paths = [] #paths em cada for loop
    nome = "Green Distribution" #nodo inicial
    custos = [] #lista que vai ter os custos de todas as encomendas
    #fazer travessia do Green Distribution a todas as encomendas
    while encomendas_nomes :
        vel = calcula_velocidade(veiculo, estafeta.encomendas)
        for encomenda_nome in encomendas_nomes:
            if procura == "Depth-first" :
                path = dfs(nome, encomenda_nome)
            elif procura == "Breadth-first":
                path = bfs(nome, encomenda_nome)
            elif procura == "A*":
                path = a_star_algorithm(nome, encomenda_nome)
            paths.append(path)
            custo = calcula_custo(path)
            custos.append(custo)
            path = []
        id_menor_custo = custos.index(min(custos))
        nome = encomendas_nomes.pop(id_menor_custo)
        estafeta.encomendas.pop(id_menor_custo)
        path_completo += paths[id_menor_custo]
        print(paths[id_menor_custo])
        custo_total += min(custos)
        tempo += calcula_tempo(min(custos), vel)
        custos = []
        paths = []
    if procura == "Depth-first" :
        path = dfs(nome, "Green Distribution")
    elif procura == "Breadth-first":
        path = bfs(nome, "Green Distribution")
    elif procura == "A*":
        path = a_star_algorithm(nome, "Green Distribution")
    path_completo += path
    custo = calcula_custo(path)
    custos.append(custo)
    final_path = [i[0] for i in groupby(path_completo)]
    print(tempo)
    return final_path



def travessia_varias_encomendas_distancia_bfs(encomendas):
    
    custo_total = 0
    path_completo = [] #path completo a passar em todas as encomendas
    paths = [] #paths em cada for loop
    nome = "Green Distribution" #nodo inicial
    custos = [] #lista que vai ter os custos de todas as encomendas
    #fazer travessia do Green Distribution a todas as encomendas
    while encomendas :
        for encomenda in encomendas:
            path = bfs(nome, encomenda)
            paths.append(path)
            custo = calcula_custo(path)
            custos.append(custo)
            path = []
        id_menor_custo = custos.index(min(custos))
        nome = encomendas.pop(id_menor_custo)
        path_completo += paths[id_menor_custo]
        print(paths[id_menor_custo])
        custo_total += min(custos)
        custos = []
        paths = []
    final_path = [i[0] for i in groupby(path_completo)]
    return final_path


def travessia_varias_encomendas_distancia_a_star(encomendas):
    custo_total = 0
    path_completo = [] #path completo a passar em todas as encomendas
    paths = [] #paths em cada for loop
    nome = "Green Distribution" #nodo inicial
    custos = [] #lista que vai ter os custos de todas as encomendas
    #fazer travessia do Green Distribution a todas as encomendas
    while encomendas :
        for encomenda in encomendas:
            path = a_star_algorithm(nome, encomenda)
            paths.append(path)
            custo = calcula_custo(path)
            custos.append(custo)
            path = []
        id_menor_custo = custos.index(min(custos))
        nome = encomendas.pop(id_menor_custo)
        path_completo += paths[id_menor_custo]
        print(paths[id_menor_custo])
        custo_total += min(custos)
        custos = []
        paths = []
    final_path = [i[0] for i in groupby(path_completo)]
    return final_path

####################################################################################################

#Fazer o dijkstra devolver caminhos de alguma forma...


def dijkstra(graph, start_vertex):
    visited = []

    #paths = {v:[start_vertex] for v in range(graph.vcount())}
    D = {v:float('inf') for v in range(graph.vcount())}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in g.neighbors(current_vertex):
            try:
                index_coordenadas = graph.get_eid(current_vertex, neighbor)               
                distance = graph.es["distancia"][index_coordenadas]
                if neighbor not in visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
            except IndexError:
                print('Indice não existente')  
    return D

####################################################################################################

#VARIAÇÃO PARA PESQUISA INFORMADA DO BFS

def best_first_search(target):
    path = best_first_search_aux(g, g.vs["rua"].index("Green Distribution"), g.vs["rua"].index(target), g.vcount())
    print(path)
    #load_search_graph(path)
    return path



def best_first_search_aux(graph ,source, target, n):
    #path = []

    visited = [0] * n
    visited[source] = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        #path.append(u)
        if u == target:
            break
 
        for neighbor in g.neighbors(u):
            index_coordenadas = graph.get_eid(u, neighbor)               
            distance = graph.es["distancia"][index_coordenadas]
            if visited[neighbor] == False:
                visited[neighbor] = True
                pq.put((distance, neighbor))
    print()

    return path

####################################################################################################

def bilp_aux(g, start, target, path, limit, visited = set()):
    for i in range(limit):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        if i != limit: 
            for neighbour in g.neighbors(start):
                if neighbour not in visited:
                    result = bilp_aux(g, neighbour, target, path, limit-1, visited)
                    if result is not None:
                        return result
        path.pop()
        return None


def bilp(target, limit):
    max_depth = limit
    path = []
    bilp_aux(g, g.vs["rua"].index("Green Distribution"), g.vs["rua"].index(target), path, max_depth, set())
    print(path)
    #load_search_graph(path)
    return path


####################################################################################################


def calcula_tempo(distancia, velocidade):
    return (distancia/1000)/velocidade
    
def calcula_velocidade(veiculo, encomendas):
    soma_peso = 0
    for e in encomendas:
        soma_peso += e.peso
    if veiculo == Transporte.Bicicleta:
        return 10 - 0.7*soma_peso
    elif veiculo == Transporte.Mota:
        return 35 - 0.5*soma_peso
    else:
        return 25 - 0.1*soma_peso
    
def escolhe_veiculo_velocidade(estafeta):
    soma_peso = 0
    for e in estafeta.encomendas:
        soma_peso += e.peso
    if soma_peso <= 5:
        return Transporte.Bicicleta
    elif soma_peso <= 20:
        return Transporte.Mota
    else:
        return Transporte.Carro



###################################################################################################
#name = "Alameda João Paulo II"
#name = "Rua de Santa Luzia"
#name = "Rua do Monte Lombo" #onde dá bug
#name = "Rua Mira Rio"
#path= dfs(name)
#load_search_graph(path)
#name = "Travessa de Sandim"
name = "Travessa de Santa Eulália"
#name = "Travessa de Santo André"
#name = "Travessa de Sarnados"
#name = "Travessa do Agrelo"
#name = "Travessa do Alcaide"
#name = "Travessa do Alto do Monte"
#name = "Travessa do Barreiro"
#name = "Travessa do Bitareu"
#name = "Travessa do Calvário"
#name = "Travessa do Campo Grande"
#name = "Travessa do Cinco de Outubro"
#name = "Travessa do Cruzeiro"
#name = "Travessa do Facho"
name2 = "Travessa do Fial"
#name3 = "Travessa do Juncal"
#name = "Travessa do Monte Lombão"
#name2 = "Travessa do Outeiro"
#name3 = "Travessa do Rioberto"
name4 = "Travessa do Salgueirinho"
#name = "Travessa do Senhor dos Aflitos"
#name = "Travessa do Valongueiro"
name5 = "Travessa do Vau"
#name = "Travessa do tapado"
name6 = "Travessa dos Campinhos"
#name = "Travessa dos Corgos"
name3 = "Urbanização Pé de Prata"

#name = "Rua de Santa Luzia"
##name = "Rua do Monte Lombo" #onde dá bug
#path= bfs(name)

#path= dfs(name)
#path= bfs(name)
#path = a_star_algorithm(name)
#print(dijkstra(g, g.vs["rua"].index("Green Distribution"))) #Não é possível dar print com o create prefs porque faz bracktracing
#print(best_first_search(name)) #Não é possível dar print com o create prefs porque faz bracktracing
#path= bilp(name,10)
#if len(path)>1:
#    load_search_graph(path)
#print(dijkstra(g, g.vs["rua"].index("Green Distribution")))


#print(g)
#print(graph_as_adjacency_list(g))


##[630, 125, 111, 39, 505, 203]
##[630, 125, 111, 39, 505, 203]
##434

nomes = [name2, name, name3, name4, name5, name6]
nomes_aux = nomes[:]



#lista = []
#lista.append([1])
#lista.append([2,3])
#print(lista)
#path = travessia_varias_encomendas_distancia_dfs(nomes)
#load_search_graph(path, nomes_aux)