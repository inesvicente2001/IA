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
from itertools import groupby,chain 
from queue import PriorityQueue
import numpy as np
import datetime
from datetime import *
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
        #print(name)
        ids_target.append(g.vs["rua"].index(name))
    #print(ids_target)
    
    for (i, node) in enumerate(path[1:]):
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
    # Set of visited nodes to prevent loops
    visited = set()
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
def heuristic(vertix,goal,graph,D):
    #Heuristica com todos os nodos a 1 ou a 0, consoante o valor que se coloque lá
    #H = dict.fromkeys(g.vs.indices, 1)
    #return H[n]

    #Heuristica com distância Euclideana
    #D é o número de vizinhos do nodo n

    coordenadas_vertix = graph.vs["coordenadas"][vertix]
    coordenadas_goal = graph.vs["coordenadas"][goal]

    dx = abs(coordenadas_vertix[0] - coordenadas_goal[0])
    dy = abs(coordenadas_vertix[1] - coordenadas_goal[1])

    point_a = np.array([coordenadas_vertix[0],coordenadas_goal[0]])
    point_b = np.array([coordenadas_vertix[1],coordenadas_goal[1]])
   
    #TESTAR COM E SEM D
    #return D * np.linalg.norm(point_a - point_b)

    #D = len(graph.neighbors(vertix))
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
                #mudar para 1 para outra heuristica
                if n == None or g[v] + heuristic(v,stop_node,graph,len(graph.neighbors(v))) < g[n] + heuristic(n,stop_node,graph,len(graph.neighbors(v))):
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



def travessia_varias_encomendas_distancia_uma(encomendas_nomes, procura, estafeta, profundidade):
    veiculo = escolhe_veiculo_velocidade(estafeta)
    print(veiculo)
    tempo = 0
    path_completo = []
    vel = calcula_velocidade(veiculo, estafeta.encomendas)
    for rua in encomendas_nomes:
        #print(rua)
        if procura == "Depth-first" :
            path = dfs("Green Distribution", rua)
        elif procura == "Breadth-first":
            path = bfs("Green Distribution", rua)
        elif procura == "A*":
            path = a_star_algorithm("Green Distribution", rua)
        elif procura == "Iterativa":
            print(rua)
            path = bilp("Green Distribution", rua, int(profundidade))
        elif procura == "Gulosa":
            path = greedy_search("Green Distribution", rua, True)

        inverse_path = path[:]
        inverse_path.reverse()
        path_completo += path + inverse_path[1:-1]
        servico = estafeta.encomendas.pop(0)
        custo = calcula_custo(path)
        tempo += calcula_tempo(custo, vel)
        criar_servico(estafeta, servico, tempo, veiculo)
        vel = calcula_velocidade(veiculo, estafeta.encomendas)
        tempo += calcula_tempo(custo, vel)
    path_completo.append(697)
    print(tempo)
    #print(path_completo)
    return (path_completo, tempo)

def calcula_dinheiro(encomenda, hora_entrega, veiculo):
    dinheiro = encomenda.peso * encomenda.volume
    if encomenda.prazo < hora_entrega:
        dinheiro = dinheiro * 0.8
    if veiculo == Transporte.Carro:
        dinheiro = dinheiro * 1.2
    elif veiculo == Transporte.Mota:
        dinheiro = dinheiro * 1.1
    return dinheiro
    

def calcula_classificacao(tempo_atual, tempo_destino, estafeta, veiculo):
    tempo_atual_minutos = tempo_atual.hour * 60 + tempo_atual.minute
    tempo_destino_minutos = tempo_destino.hour * 60 + tempo_destino.minute
    if (tempo_destino_minutos / tempo_atual_minutos) >= 1.5:
        estafeta.castigo -= 1
        return random.randint(3,5)
    
    if (tempo_destino_minutos / tempo_atual_minutos) <= 1.5:
        estafeta.castigo += 2
        return random.randint(1,3)
    else:
        return random.randint(2,4)

        
def criar_servico(estafeta, encomenda, tempo, veiculo):
    tempo_atual = datetime.combine(date.today(), time(0,0)) + timedelta(hours = tempo)
    tempo_destino = encomenda.prazo
    
    #atualizar classificacao
    classificacao = calcula_classificacao(tempo_atual, tempo_destino, estafeta, veiculo)
    media_classificacao = (classificacao + (estafeta.classificacao) * estafeta.nr_classificacoes) / (estafeta.nr_classificacoes + 1)
    estafeta.classificacao = media_classificacao
    estafeta.nr_classificacoes  += 1
    
    #criar servico
    hora_da_entrega = time(tempo_atual.hour, tempo_atual.minute)
    if hora_da_entrega > tempo_destino:
        a_tempo = False
    else:
        a_tempo = True
    
        
    dinheiro = calcula_dinheiro(encomenda, hora_da_entrega, veiculo)
        
    servico = Servico(encomenda.id, encomenda.nome, encomenda.rua, classificacao, hora_da_entrega, a_tempo, encomenda.peso, veiculo, dinheiro)
    estafeta.servicos.append(servico)
    lista_estafetas = convert_estafetas(estafetas_final)
    add_servico(servico)
    df = pd.DataFrame(lista_estafetas, columns=['nome','classificacao','nr_classificacao','encomendas','servicos','castigo'])
    df.to_csv('DB/Estafetas.csv', index=False)
    
    
    

def travessia_varias_encomendas_distancia(encomendas_nomes, procura, estafeta, profundidade):
    veiculo = escolhe_veiculo_velocidade(estafeta)
    servicos = estafeta.encomendas[:]
    print(veiculo)
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
        print(vel)
        for encomenda_nome in encomendas_nomes:
            if procura == "Depth-first" :
                path = dfs(nome, encomenda_nome)
            elif procura == "Breadth-first":
                path = bfs(nome, encomenda_nome)
            elif procura == "A*":
                path = a_star_algorithm(nome, encomenda_nome)
            elif procura == "Iterativa":
                path = bilp(nome, encomenda_nome, int(profundidade))
            elif procura == "Gulosa":
                path = greedy_search(nome, encomenda_nome, True)
            paths.append(path)
            custo = calcula_custo(path)
            custos.append(custo)
            path = []
        id_menor_custo = custos.index(min(custos))
        nome = encomendas_nomes.pop(id_menor_custo)
        servico = estafeta.encomendas.pop(id_menor_custo)
        path_completo += paths[id_menor_custo]
        #print(paths[id_menor_custo])
        custo_total += min(custos)
        tempo += calcula_tempo(min(custos), vel)
        criar_servico(estafeta, servico, tempo, veiculo)
        custos = []
        paths = []
    if procura == "Depth-first" :
        path = dfs(nome, "Green Distribution")
    elif procura == "Breadth-first":
        path = bfs(nome, "Green Distribution")
    elif procura == "A*":
        path = a_star_algorithm(nome, "Green Distribution")
    elif procura == "Iterativa":
        path = a_star_algorithm(nome, "Green Distribution")
    elif procura == "Gulosa":
        path = a_star_algorithm(nome, "Green Distribution")
    path_completo += path
    custo = calcula_custo(path)
    custos.append(custo)
    final_path = [i[0] for i in groupby(path_completo)]
    
    print(tempo)
    return (final_path, tempo)


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
    #print(path)
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


def bilp(start, target, limit):
    max_depth = limit
    path = []
    print(start)
    print(target)
    bilp_aux(g, g.vs["rua"].index(start), g.vs["rua"].index(target), path, max_depth, set())
    print(path)
    #load_search_graph(path)
    return path


####################################################################################################


def calcula_tempo(distancia, velocidade):
    return (distancia)/velocidade*pow(10,-3)
    
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


def veiculos_possiveis_lst(estafeta):
    soma_peso = 0
    for e in estafeta.encomendas:
        soma_peso += e.peso
    if soma_peso <= 5:
        return [Transporte.Bicicleta,Transporte.Mota,Transporte.Carro]
    elif soma_peso <= 20:
        return [Transporte.Mota,Transporte.Carro]
    else:
        return [Transporte.Carro]



def fator_urgencia_e_prazo(urgencia, prazo):
    #15 minutos: fator urgencia
    #cria um novo prazo representativo de urgencia
    tempo = datetime.combine(date.today(), prazo) - timedelta(minutes = 15*urgencia)
    new_prazo = tempo.time()
    return new_prazo




def select_most_urgent(encomendas, lst_proibidos):
    most_urgent = " " 
    urgency = time(23,59) #urgencia maxima -> começa no ultimo minuto antes de mudança de dia
    for encomenda in encomendas:
        prazo_fatorizado = fator_urgencia_e_prazo(encomenda.urgencia, encomenda.prazo)
        if prazo_fatorizado < urgency and encomenda.rua not in lst_proibidos:
            most_urgent = encomenda.rua
            urgency = prazo_fatorizado
    return most_urgent



###################################################################################################
def greedy_search_aux(graph,start, target, euclidean):
    # greedy search algorithm
    #d_dict = {1: [(1, 2), (2, 15), (3, 30)], 2: [(1, 30), (7, 10)]}  # dict of lists of tuples such that nodei : [ (neighbourj, distancej), .... ]
    currentCity = start
    tour = []   # list of covered nodes
    tour.append(currentCity)
    #distanceTravelled = 0   # distance travelled in tour
    while len( set([neighbourCity for neighbourCity in graph.neighbors(currentCity)]).difference(set(tour))) > 0:  # set(currentCityNeighbours) - set(visitedNodes)
        # way 1 starts
        minDistanceNeighbour = None
        minDistance = None
        for neighbour in graph.neighbors(currentCity):
            if neighbour == target:
                tour.append(neighbour)
                break
            #for eachNeighbour, eachNeighbourdDistance in 
            if neighbour != currentCity and neighbour not in tour:
                if euclidean:
                    if minDistance is not None:
                        if minDistance > heuristic(currentCity,neighbour,graph,1) :
                            minDistance = heuristic(currentCity,neighbour,graph,1)
                            minDistanceNeighbour = neighbour
                    else:
                        minDistance = heuristic(currentCity,neighbour,graph,1)
                        minDistanceNeighbour = neighbour
                else:
                    edge_id = graph.get_eid(currentCity, neighbour)
                    cost = graph.es["distancia"][edge_id]
                    if minDistance is not None:
                        if minDistance > cost :
                            minDistance = cost
                            minDistanceNeighbour = neighbour
                    else:
                        minDistance = cost
                        minDistanceNeighbour = neighbour

        nearestNeigbhourCity = (minDistanceNeighbour, minDistance)
        # way 1 ends
        # way 2 starts
        # nearestNeigbhourCity = min(d_dict[currentCity], key=lambda someList: someList[1] if someList[0] not in tour else 1000000000)  # else part returns some very large number
        # way 2 ends
        tour.append(nearestNeigbhourCity[0])
        currentCity = nearestNeigbhourCity[0]
        #distanceTravelled += nearestNeigbhourCity[1]
    #print(tour)
    #print(distanceTravelled)
    return tour


def greedy_search(start, target, euclidean):
    path = greedy_search_aux(g, g.vs["rua"].index(start), g.vs["rua"].index(target), euclidean)
    if path[-1] != g.vs["rua"].index(target):
        path.clear()
        print("Pesquisa gulosa não encontrou caminho")
    #print(path)
    #load_search_graph(path)
    return path


####################################################################################################


def ecologic_path_uma(encomendas_nomes, procura, estafeta, profundidade):
    veiculo = escolhe_veiculo_velocidade(estafeta)
    print(veiculo)
    tempo = 0
    path_completo = []
    vel = calcula_velocidade(veiculo, estafeta.encomendas)
    while encomendas_nomes:
        #escolhe a  mais urgente
        #nome da rua para a encomenda mais urgente
        most_urgent = select_most_urgent(estafeta.encomendas, [])
        most_urgent_id = estafeta.encomendas.index(most_urgent)

        #print(rua)
        if procura == "Depth-first" :
            path = dfs("Green Distribution", most_urgent)
        elif procura == "Breadth-first":
            path = bfs("Green Distribution", most_urgent)
        elif procura == "A*":
            path = a_star_algorithm("Green Distribution", most_urgent)
        elif procura == "Iterativa":
            print(rua)
            path = bilp("Green Distribution", most_urgent, int(profundidade))
        elif procura == "Gulosa":
            path = greedy_search("Green Distribution", most_urgent, False)

        inverse_path = path[:]
        inverse_path.reverse()
        path_completo += path + inverse_path[1:-1]
        encomenda_removida = estafeta.encomendas.pop(most_urgent_id)
        custo = calcula_custo(path)
        tempo += calcula_tempo(custo, vel)
        criar_servico(estafeta, encomenda_removida , tempo, veiculo)
        vel = calcula_velocidade(veiculo, estafeta.encomendas)
        tempo += calcula_tempo(custo, vel)
    path_completo.append(697)
    print(tempo)
    #print(path_completo)
    return (path_completo, tempo)



def ecologic_on_time_path(encomendas_nomes, procura, estafeta, profundidade):

    max_num_tries = 10 * len(encomendas_nomes)


    custo_atual = 0 #distancia
    tempo_atual = time(0,0) #tempo
    path_final = []

    #lista com veiculos que serão possiveis de usar, tendo em conta o peso total da encomenda
    veiculos_possiveis = veiculos_possiveis_lst(estafeta)

    #lista encomendas estafeta
    #encomendas = estafeta.encomendas

    paths = []
    custos = []


    nome = "Green Distribution" #nodo inicial
    #para todos os veiculos possiveis:
    #dicionário que diz se cada nodo será entregue a tempo  
    on_time_dictionary = {}
    for veiculo in veiculos_possiveis:
        on_time_dictionary.update({veiculo:dict()})
        for encomenda_nome in encomendas_nomes:
            on_time_dictionary[veiculo].update({encomenda_nome:True})

    #dicionário que diz se encontrou caminho
    found_path_dictionary = {}
    for veiculo in veiculos_possiveis:
        found_path_dictionary.update({veiculo:False})

    
    #tempos para os diferentes veiculos num dicionário
    times_dictionary = {}
    #guarda valor anterior no primeiro elemento da lista e o atual no segundo
    for veiculo in veiculos_possiveis:
        times_dictionary.update({veiculo:[time(0,0),time(0,0)]})


    #em floats
    #tempos para os diferentes veiculos num dicionário
    float_times_dictionary = {}
    #guarda valor anterior no primeiro elemento da lista e o atual no segundo
    for veiculo in veiculos_possiveis:
        float_times_dictionary.update({veiculo:[0,0]})

    #velocidades para os diferentes veiculos num dicionário
    velocities_dictionary = {}
    #guarda valor anterior no primeiro elemento da lista e o atual no segundo
    for veiculo in veiculos_possiveis:
        velocities_dictionary.update({veiculo:[-1,-1]})


    #encomendas para os diferentes veiculos num dicionário
    encomendas_dictionary = {}
    #guarda copia encomendas para cada veiculo
    for veiculo in veiculos_possiveis:
        encomendas_dictionary.update({veiculo:estafeta.encomendas.copy()})

    #nomes encomendas para os diferentes veiculos num dicionário
    nomes_encomendas_dictionary = {}
    #guarda copia nome encomendas para cada veiculo
    for veiculo in veiculos_possiveis:
        nomes_encomendas_dictionary.update({veiculo:encomendas_nomes.copy()})

    #lista dos proibidos para os diferentes veiculos num dicionário
    lst_proibidos_dictionary = {}
    #guarda copia nome encomendas para cada veiculo
    for veiculo in veiculos_possiveis:
        lst_proibidos_dictionary.update({veiculo:[]})


    #lista dos custos para os diferentes veiculos num dicionário
    custos_dictionary = {}
    for veiculo in veiculos_possiveis:
        custos_dictionary.update({veiculo:[]})


    #lista dos paths para os diferentes veiculos num dicionário
    path_dictionary = {}
    for veiculo in veiculos_possiveis:
        path_dictionary.update({veiculo:[]})



    #travessia para os diupdate({veiculo:ferentes veiculos
    #faz isso para os diferentes veiculos
    #o que para um veiculo pode dar, para outro pode não dar
    for veiculo in veiculos_possiveis:

        num_tries = 0

        while nomes_encomendas_dictionary[veiculo] and num_tries < max_num_tries and len(lst_proibidos_dictionary[veiculo]) < len(nomes_encomendas_dictionary[veiculo]):
            old_name = nome
            #ver velocidades de todos os veiculos
            #o procedimento deve ser feito para os veiculos todos
            #atualizar valor no dicionário velocidades
        
            velocities_dictionary[veiculo][0] = velocities_dictionary[veiculo][1]
            velocities_dictionary[veiculo][1] = calcula_velocidade(veiculo, encomendas_dictionary[veiculo])
            #vel = calcula_velocidade(veiculo, estafeta.encomendas)

            #nome da rua para a encomenda mais urgente
            most_urgent = select_most_urgent(encomendas_dictionary[veiculo], lst_proibidos_dictionary[veiculo])
            most_urgent_id = nomes_encomendas_dictionary[veiculo].index(most_urgent)

            #voltar a meter lista de proibidos nula
            lst_proibidos_dictionary[veiculo] = []

            if procura == "Depth-first" :
                fst_path = dfs(nome, most_urgent)
            elif procura == "Breadth-first":
                fst_path = bfs(nome, most_urgent)
            elif procura == "A*":
                fst_path = a_star_algorithm(nome, most_urgent)
            elif procura == "Iterativa":
                print(rua)
                fst_path = bilp(nome, most_urgent, int(profundidade))
            elif procura == "Gulosa":
                fst_path = greedy_search(nome, most_urgent, False)


            #nome = most_urgent
            custo = calcula_custo(fst_path)
            custo_atual = custo_atual + custo

            #atualizar valor no dicionário
            tempo_demorado = calcula_tempo(custo, velocities_dictionary[veiculo][1])

            tmp_float = float_times_dictionary[veiculo][1]
            float_times_dictionary[veiculo][0] = tmp_float
            float_times_dictionary[veiculo][1] = tmp_float + tempo_demorado


            minutes_to_add = int((tempo_demorado*60) % 60)
            aux = times_dictionary[veiculo][1]
            tempo_atual = datetime.combine(date.today(), aux) + timedelta(minutes = minutes_to_add)
            times_dictionary[veiculo][0] = aux
            times_dictionary[veiculo][1] = tempo_atual.time()



            #percorrer lista e ver se os bools não se alteram drasticamente
            #exceto encomenda para a qual avançamos
            nome = nomes_encomendas_dictionary[veiculo].pop(most_urgent_id)
            encomenda_retirada = encomendas_dictionary[veiculo].pop(most_urgent_id)
            

            for encomenda_nome in nomes_encomendas_dictionary[veiculo]:

                if procura == "Depth-first" :
                    path = dfs(nome, encomenda_nome)
                elif procura == "Breadth-first":
                    path = bfs(nome, encomenda_nome)
                elif procura == "A*":
                    path = a_star_algorithm(nome, encomenda_nome)  
                elif procura == "Iterativa":
                    print(rua)
                    path = bilp(nome, encomenda_nome, int(profundidade))
                elif procura == "Gulosa":
                    path = greedy_search(nome, encomenda_nome, False)

                #fazer cálculos
                #dicionário dos bools
                #dicionário dos tempos --> faz uma cópia e usa-a para fazer verificações e preencher o dos bools
                #tmb é preciso uma cópia para o das velocidades para simular dimiunição do peso
                on_time_dictionary_copy = on_time_dictionary.copy()
                times_dict_copy = times_dictionary.copy()
                velocities_dictionary_copy = velocities_dictionary.copy()
                custo_tmp = calcula_custo(path)
                custo_atual_tmp = custo_atual + custo_tmp

                #atualizar valores no dicionário cópia das velocidades
                velocities_dictionary_copy[veiculo][0] = velocities_dictionary_copy[veiculo][1]
                velocities_dictionary_copy[veiculo][1] = calcula_velocidade(veiculo, encomendas_dictionary[veiculo])

                #ver tempos e depois meter no dicionário de booleanos
                #atualizar valores no dicionário cópia dos tempos
                tempo_demorado_tmp = calcula_tempo(custo_tmp, velocities_dictionary_copy[veiculo][1])

                tmp_demorado_float = float_times_dictionary[veiculo][1]
                float_times_dictionary[veiculo][0] = tmp_demorado_float
                float_times_dictionary[veiculo][1] = tmp_demorado_float + tempo_demorado_tmp



                minutes_to_add = int((tempo_demorado*60) % 60)
                aux = times_dict_copy[veiculo][1]
                tempo_atual = datetime.combine(date.today(), aux) + timedelta(minutes = minutes_to_add)
                times_dict_copy[veiculo][0] = aux
                times_dict_copy[veiculo][1] = tempo_atual.time()


                if times_dict_copy[veiculo][1] > get_prazo_encomenda(estafeta, encomenda_nome):
                    #colocar a false no dicionário
                    print("Aqui")
                    new_dictionary = on_time_dictionary[veiculo]
                    new_dictionary[encomenda_nome] = False
                    on_time_dictionary[veiculo] = new_dictionary

           
            #não esquecer quando correr mal de voltar a colocar os valores anteriores
            #adicionar nome node à lista proibidos
            #adicionar de novo às encomendas do estafeta, pq n foi entregue. adicionar à cópia no caso
            #fazer  o dicionario dos bools e os outros voltam a ter o estado atual igual ao antigo
            #recomeçar while
            #remover ultimo path dos paths / não adicionar
            #nome volta o antigo
        
            #quando corre bem --> Quando tem Lista com Trues
            #adiciona o path atual à lista dos paths
            #paths.append(fst_path)
            #custos.append(custo)
            #path = []   

            
            #analisar dicionário completo dos tempos já com as modificações
            all_on_time = True
            for encomenda_nome,boolean in on_time_dictionary[veiculo].items():
                if boolean == False:
                    all_on_time = False

            if all_on_time == True:
                #pode avançar. correu bem. adiciona aos dicionários de custos e paths
                custos_atuais_lst = custos_dictionary[veiculo]
                paths_atuais_lst = path_dictionary[veiculo]

                custos_atuais_lst.append(custo)
                paths_atuais_lst.append(fst_path)
                
                custos_dictionary[veiculo] = custos_atuais_lst
                path_dictionary[veiculo] = paths_atuais_lst

                num_tries = 0

            else:
                #não pode avançar 
                #não adiciona nada aos dicionários de custos e paths
                atual_nome = nome
                nome = old_name
                proibidos_atuais_lst = lst_proibidos_dictionary[veiculo]
                proibidos_atuais_lst.append(nome)
                lst_proibidos_dictionary[veiculo] = proibidos_atuais_lst


                #voltar a adicionar a encomenda
                encomendas_lst = encomendas_dictionary[veiculo]
                encomendas_lst.append(encomenda_retirada)
                encomendas_dictionary[veiculo] = encomendas_lst

                num_encomendas = num_encomendas+1

                #voltar a adicionar o nome da encomenda
                nomes_encomendas_lst = nomes_encomendas_dictionary[veiculo]
                nomes_encomendas_lst.append(atual_nome)
                nomes_encomendas_dictionary[veiculo] = nomes_encomendas_lst


                #dicionário de on_time volta a estar True
                for encomenda_nome,boolean in on_time_dictionary[veiculo].items():
                    on_time_dictionary[veiculo][encomenda_nome] = True

                #dicionário dos tempos fica com os tempos atuais a serem iguais aos antigos
                times_atuais_lst = times_dictionary[veiculo]
                times_atuais_lst[1] = times_atuais_lst[0]
                times_dictionary[veiculo] = times_atuais_lst

                float_times_atuais_lst = float_times_dictionary[veiculo]
                float_times_atuais_lst[1] = float_times_atuais_lst[0]
                float_times_dictionary[veiculo] = float_times_atuais_lst

                #dicionário das velocidades fica com as veloccidades atuais a serem iguais as antigas
                velocities_atuais_lst = velocities_dictionary[veiculo]
                velocities_atuais_lst[1] = velocities_atuais_lst[0]
                velocities_dictionary[veiculo] = velocities_atuais_lst

                num_tries = num_tries - 1

    #saiu do while.
    #se correu bem, algum dos veiculos terá o caminho todo 
    #entregas feitas: esvazia encomendas do estafeta
    #escolhe o veículo

    #senão: não encontrou caminho q satisfaz o objetivo
    for veiculo in veiculos_possiveis:
        all_on_time_final = True
        for encomenda_nome,boolean in on_time_dictionary[veiculo].items():
                if boolean == False:
                    all_on_time_final = False

        if all_on_time_final:
            found_path_dictionary[veiculo] = True


    veiculos_com_path = []
    for veiculo,boolean in found_path_dictionary.items():
        if found_path_dictionary[veiculo] == True:
            veiculos_com_path.append(veiculo)

    if len(veiculos_com_path)>0:
        found_a_path = True
        if Transporte.Bicicleta in veiculos_com_path:
            veiculo_usado = Transporte.Bicicleta
        elif Transporte.Mota in veiculos_com_path:
            veiculo_usado = Transporte.Mota
        else:
            veiculo_usado = Transporte.Carro
        

    if found_a_path:
        #tirar encomendas do estafeta
        estafeta.encomendas.clear()


        #back to Green Distribution  
        if procura == "Depth-first" :
            path_back_gd = dfs(nome, "Green Distribution")
        elif procura == "Breadth-first":
            path_back_gd = bfs(nome, "Green Distribution")
        elif procura == "A*":
            path_back_gd = a_star_algorithm(nome, "Green Distribution")
        elif procura == "Iterativa":
            print(rua)
            path_back_gd = bilp(nome, "Green Distribution", int(profundidade))
        elif procura == "Gulosa":
            path_back_gd = greedy_search(nome, "Green Distribution", False)

        #adiciona aos paths

        path_dictionary[veiculo_usado] += [path_back_gd]
        custo_back_gd = calcula_custo(path_back_gd)
        custos_dictionary[veiculo_usado] += [custo_back_gd]
        custo_final = sum(custos_dictionary[veiculo_usado])

        #atualiza tempo
        tempo_demorado = calcula_tempo(custo_back_gd, velocities_dictionary[veiculo][1])
        minutes_to_add = int((tempo_demorado*60) % 60)
        aux = times_dictionary[veiculo][1]
        tempo_atual = datetime.combine(date.today(), aux) + timedelta(minutes = minutes_to_add)
        #times_dictionary[veiculo][0] = aux
        #times_dictionary[veiculo][1] = tempo_atual.time()
        tempo_atual_float = float_times_dictionary[veiculo][1] + tempo_demorado

        print(tempo_atual.time())
        print(veiculo_usado)

        flat=chain.from_iterable(path_dictionary[veiculo_usado])
        path_lst = list(flat)
        final_path = [i[0] for i in groupby(path_lst)]
        return (final_path, tempo_atual_float) #depois mudar isto... para time(_,_)

    else:
        print("Não foi possivel entregar todas as encomendas a tempo")
        return ([], -1) #depois mudar isto... para time(_,_)


