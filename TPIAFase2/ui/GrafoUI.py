import sys
from db import *
import tkinter as tk
from igraph import *
import igraph as ig
#import IA.TPIAFase2.dl.db #TODO Depois mudar isto pq a ui n pode comunicar com a dl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class GrafoUI(tk.Frame) :

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Grafo",
            fg="white",
            bg="black",
            width=15,
            height=5
        ).pack()
       
        
        tk.buttonGraph = tk.Button(
            self,
            text="Adicionar Rua",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
            command = lambda: master.switch_frame(AdicionarRua)
        ).pack()
        
        tk.buttonDL = tk.Button(
            self,
            text="Ver base de conhecimento",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
        ).pack()
        
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
            command = lambda: master.switch_frame(PaginaInicial)
        ).pack()
        
        tk.graph = self.show_graph()
        
    def show_graph(self):
        g = Graph.Read_GraphML("teste.graphml")
        fig, axs = plt.subplots(figsize=(8, 4))
        prefs = create_prefs()
        ig.plot(g, target = axs, **prefs)
        plt.axis('off')
        


        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack()

        
from PaginaInicial import *
from AdicionarRua import *