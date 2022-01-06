import sys
sys.path.insert(1, 'dl')
from db import *
import tkinter as tk
from igraph import *
import igraph as ig
#import IA.TPIAFase2.dl.db #TODO Depois mudar isto pq a ui n pode comunicar com a dl
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def show_graph():
    load_graph()
    
    
class GrafoUI(tk.Frame) :

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Grafo",
            font = ('Arial', 30)
        ).pack(pady = 25)
        
        tk.buttonGrafo = tk.Button(
            self,
            text="Ver grafo",
            width=25,
            height=5,
            command = show_graph
        ).pack()
       
       #TODO provavelmente vamos ter de mudar 
        tk.buttonRua = tk.Button(
            self,
            text="Adicionar Rua",
            width=25,
            height=5,
            command = lambda: master.switch_frame(AdicionarRua)
        ).pack()
        
        
        
        tk.buttonEncomenda = tk.Button(
            self,
            text="Fazer entrega",
            width=25,
            height=5,
            command = lambda: master.switch_frame(FazerEncomenda)
        ).pack()
        
        
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: master.switch_frame(PaginaInicial)
        ).pack()
        
        

        
from PaginaInicial import *
from AdicionarRua import *
from FazerEncomenda import *