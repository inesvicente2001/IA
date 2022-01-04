import sys
sys.path.insert(1, 'dl')
from db import *
from enum import Enum
from ast import literal_eval as make_tuple
import igraph
from igraph import *
import igraph as ig
import pandas as pd
import random
import tkinter as tk
import networkx


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


def dfs(target):
    path = []
    dfs_aux(g, g.vs["rua"].index("Green Distribution"), g.vs["rua"].index(target), path, set())
    print(path)
    #load_search_graph(path)
    return path
    
    
def load_search_graph(path):
    prefs = create_prefs()
    print(path)
    total_cost = 0
    
    
    for (i, node) in enumerate(path[1:]):
        prefs["vertex_color"][node] = "blue"
        prefs["vertex_size"][node] = 20
        edge_id = g.get_eid(path[i], path[i+1], error = False)
        prefs["edge_color"][edge_id] = "red"
        prefs["edge_width"][edge_id] = 4
        total_cost += g.es["distancia"][edge_id]
    #prefs["vertex_color"][g.vs["rua"].index("Green Distribution")] = "green"
    prefs["vertex_color"][path[len(path)-1]] = "yellow"
    print(total_cost)
    plot(g, **prefs)