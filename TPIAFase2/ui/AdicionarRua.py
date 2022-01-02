import tkinter as tk
from igraph import *
from db import *
import igraph as ig
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
    
    
    
def confirmar(lista):
    selecionados = lista.curselection()
    print(len(selecionados))
    print("OLA")
    for i in selecionados:
        print(lista.get(i))
        
        
class AdicionarRua(tk.Frame) :

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Adicionar Rua",
            fg="white",
            bg="black",
            width=15,
            height=5
        ).pack()
       
        #criar um dropdown menu
        variable = tk.StringVar()
        variable.set("freguesia a escolher") #oq aparece antes de ver as opções do dropdown
        tk.dd = tk.OptionMenu(self, variable, *self.get_freguesias()).pack() #Drop down menu com freguesias a escolher
        
        #criar caixa com várias opções
        lista = tk.Listbox(self, selectmode = tk.MULTIPLE)
        ruas = self.get_ruas()
        for item in ruas:
            lista.insert(tk.END, item) #no idea how this works: https://www.geeksforgeeks.org/creating-a-multiple-selection-using-tkinter/
            #lista.itemconfig(item, bg = "yellow" if item % 2 == 0 else "cyan") #meter cores alternadas
        lista.pack()
            
         
        tk.buttonConfirmar = tk.Button(
            self,
            text="Confirmar",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
            command = lambda: confirmar(lista)
        ).pack()

        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
            command = lambda: master.switch_frame(GrafoUI)
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
    
    def get_freguesias(self):
        g = Graph.Read_GraphML("teste.graphml")
        aux = list(dict.fromkeys(g.vs["freguesia"]))
        return aux
    
    def get_ruas(self):
        g = Graph.Read_GraphML("teste.graphml")
        return g.vs["rua"]
        
    
    
from GrafoUI import *