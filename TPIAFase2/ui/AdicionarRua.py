import tkinter as tk
from igraph import *
from db import *
import igraph as ig
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
    
    
nome_freguesia = ""
rua_a_adicionar = ""
ruas = []
distancias = []
        
        
        
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
        variable.set("Freguesia a escolher") #oq aparece antes de ver as opções do dropdown
        options = tk.OptionMenu(self, variable, *self.get_freguesias()).pack() #Drop down menu com freguesias a escolher
        
        #criar caixa com várias opções
        lista = tk.Listbox(self, selectmode = tk.MULTIPLE)
        ruas = self.get_ruas()
        for item in ruas:
            lista.insert(tk.END, item) #no idea how this works: https://www.geeksforgeeks.org/creating-a-multiple-selection-using-tkinter/
            #lista.itemconfig(item, bg = "yellow" if item % 2 == 0 else "cyan") #meter cores alternadas
        lista.pack()
        
        #criar caixa de texto
        text_label = tk.Label(self, text = "Nome da nova rua")
        entry = tk.Entry(self)
        text_label.pack()
        entry.pack()
            
         
        tk.buttonConfirmar = tk.Button(
            self,
            text="Confirmar",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
            command = lambda: self.confirmar(lista, entry.get(), variable.get())
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
            
    def confirmar(self, lista, nova_rua, freguesia):
        flag = True
        if not lista.curselection():
            tk.Label(self, text = "Erro, seleciona ruas para conectar à nova rua").pack()
            flag = False
        if not nova_rua:
            tk.Label(self, text = "Erro, escreve o nome da rua que queres").pack()
            flag = False
        if freguesia == "Freguesia a escolher":
            tk.Label(self, text = "Erro, seleciona ruas para conectar à nova rua").pack()
            flag = False
            
        if nova_rua in self.get_ruas():
            tk.Label(self, text = "Erro, rua a adicionar já existe").pack()
            flag = False
            
        if flag == False:
            return
        
        selecionados = lista.curselection()
    
       
        selecionados_name = []
        for i in selecionados:
            selecionados_name.append(lista.get(i))
            
        global nome_freguesia 
        nome_freguesia = freguesia
        global rua_a_adicionar 
        rua_a_adicionar = nova_rua
        global ruas 
        ruas = selecionados_name
        print("//////////////////////////////////")
        print(nome_freguesia)
        print(rua_a_adicionar)
        print(ruas)
        print("/////////////////////////////////")


        self.create_distancias(nova_rua, selecionados_name)
        #add_vertice(freguesia, nova_rua, selecionados)
    
    def create_distancias(self, nova_rua, selecionados):
        window = tk.Tk()
        entries = [tk.Entry(window) for _ in range(len(selecionados))]
        for rua, entry in zip(selecionados, entries):
            tk.Label(window, text = f"Distancia de {nova_rua} a {rua}:").pack()
            entry.pack()
            
        print(len(entries))
        buttonConfirmar = tk.Button(
            window,
            text="Confirmar",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
            command = lambda: self.get_distancias(entries, window)
        ).pack()
        
    def get_distancias(self, entries, window):
        dists = []
        for entry in entries:
            dists.append(entry.get())
        global distancias 
        distancias = dists
        print("//////////////////////////////////")
        print(nome_freguesia)
        print(rua_a_adicionar)
        print(ruas)
        print("/////////////////////////////////")
        add_vertice(nome_freguesia, rua_a_adicionar, ruas, distancias)
        window.destroy()
        
        
    
from GrafoUI import *