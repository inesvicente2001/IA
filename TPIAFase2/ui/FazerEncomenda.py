#TODO depois é preciso adicionar a encomenda e o serviço à base de conhecimento

import sys
sys.path.insert(1, 'dl')
sys.path.insert(1, 'ln')
from db import *
from ln import *
import tkinter as tk
from igraph import *
import igraph as ig
#import IA.TPIAFase2.dl.db #TODO Depois mudar isto pq a ui n pode comunicar com a dl
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tkinter as ttk


procuras = [
    "Depth-first",
    "Iterativa",
    "Breadth-first",
    "Gulosa",
    "A*",
]


def calcula_caminho(rua, procura):
    if procura == "Depth-first":
        return dfs(rua)
    #TODO acabar isto com as outras procuras
    
def show_graph():
    load_graph()   
    
def show_search_graph(path):
    load_search_graph(path)

class FazerEncomenda(tk.Frame) :

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Fazer uma encomenda",
            width=15,
            height=5
        ).pack()
        
        ruas = self.get_ruas()
        ruas.sort()
        
        
        #rua = tk.StringVar()
        #rua.set("Rua para onde fazer a entrega") #oq aparece antes de ver as opções do dropdown
        #optionsR = tk.OptionMenu(self, rua, *ruas).pack() #Drop down menu com freguesias a escolher
        
        #Drop down menu
        tk.Label(self, text="Seleciona a rua para fazer a entrega").pack()
        comboRua = ttk.Combobox(self, value = ruas)
        comboRua.pack()
        
        tk.Label(self, text="Seleciona o tipo de procura").pack()
        comboProcura = ttk.Combobox(self, value = procuras)
        comboProcura.pack()
        
        
        #procura = tk.StringVar()
        #procura.set("Seleciona tipo de procura") #oq aparece antes de ver as opções do dropdown
        #optionsP = tk.OptionMenu(self, procura, *procuras).pack() #Drop down menu com procuras a escolher
        
        tk.buttonConfirmar = tk.Button(
            self,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: self.confirmar(comboRua.get(), comboProcura.get())
        ).pack()
        
        tk.buttonGrafo = tk.Button(
            self,
            text="Ver grafo",
            width=25,
            height=5,
            command = show_graph
        ).pack()
       
    
        
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: master.switch_frame(GrafoUI)
        ).pack()
        
        
        
    def get_ruas(self):
        g = Graph.Read_GraphML("teste.graphml")
        return g.vs["rua"]
    
    def confirmar(self, rua, procura):
        flag = True
        if rua == "":
            tk.Label(self, text = "Erro, seleciona uma rua para fazer a entrega").pack()
            flag = False
            
        if procura == "":
            tk.Label(self, text = "Erro, seleciona o tipo de procura").pack()
            flag = False
            
        if flag == False:
            return
        
        path = calcula_caminho(rua, procura)
        
        search_window = tk.Tk()
        tk.label = tk.Label(
            search_window,
            text="Procura efetuada com sucesso!",
            width=50,
            height=5
        ).pack()
        
        tk.buttonGrafo = tk.Button(
            search_window,
            text="Ver grafo com procura",
            width=25,
            height=5,
            command = lambda: show_search_graph(path)
        ).pack()
        
        
        tk.buttonVoltar = tk.Button(
            search_window,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: search_window.destroy()
        ).pack()
        
from GrafoUI import *