import sys
sys.path.insert(1, 'dl')
from db import *
import tkinter as tk
from igraph import *
  
g = Graph.Read_GraphML("teste.graphml")

def get_freguesias():
    aux = list(dict.fromkeys(g.vs["freguesia"]))
    return aux

def get_ruas_freguesia(freguesia):
    freguesias = g.vs["freguesia"]
    rua_freguesia_id = []
    rua_freguesia = []
    for (i, freg) in enumerate(freguesias):
        if freg == freguesia:
            rua_freguesia_id.append(i)
            
    for i in rua_freguesia_id:
        rua_freguesia.append(g.vs["rua"][i])
        
    #    if freguesia == n
    #        rua_freguesia.append(n)
    return rua_freguesia

    
def ruas_to_string(lista):
    string = ''
    for element in lista:
        string += element
        string += "\n"
        #string.join("\n")
        print(string)
    return string

def estafeta_to_string(estafeta):
    string = ''
    string = string + "Nome: " + estafeta.nome
    string += "\n"
    string = string + "Classificação: " + str(estafeta.classificacao)
    string += "\n"
    string = string + "Número de classificações: " + str(estafeta.nr_classificacoes)
    string += "\n"
    string = string + "Encomendas feitas: " + str(len(estafeta.encomendas))
    string += "\n"
    string = string + "Serviços por fazer: " + str(len(estafeta.servicos))
    string += "\n"
    string = string + "Castigo: " + str(estafeta.castigo)
    return string


class VerBaseConhecimento(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Base de conhecimento",
            fg="white",
            bg="black",
            width=15,
            height=5
        ).pack()
        
        tk.Button(
            self,
            text="Ver Clientes",
            width=25,
            height=5,
        ).pack()
        
        
        tk.Button(
            self,
            text="Ver Freguesias/Ruas",
            width=25,
            height=5,
            command = lambda: master.switch_frame(VerRuas)
        ).pack()
        
        tk.Button(
            self,
            text="Ver Encomendas",
            width=25,
            height=5,
        ).pack()
        
        tk.Button(
            self,
            text="Ver Serviços",
            width=25,
            height=5,
        ).pack()
        
        tk.Button(
            self,
            text="Ver Estafetas",
            width=25,
            height=5,
            command = lambda: master.switch_frame(VerEstafetas)
        ).pack()
        
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: master.switch_frame(BaseConhecimento)
        ).pack() 
       
       
class VerRuas(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Seleciona a freguesia").pack()
        combo = ttk.Combobox(self, value = get_freguesias())
        combo.pack()
        
        frame = tk.LabelFrame(self, text = "")
        msg = tk.Label(frame, text = "")
        tk.Button(self, text = "Ver ruas", command = lambda:  self.show_ruas(combo.get(), msg, frame)).pack()
        
            
    def show_ruas(self, freguesia, msg, frame):
        ruas = get_ruas_freguesia(freguesia)
        frame.config(text = freguesia)  
        frame.pack()
        msg.config(text = ruas_to_string(ruas))
        msg.pack()
            
class VerEstafetas(tk.Frame):
    
    def get_estafetas_names(self, estafetas):
        names = []
        for estafeta in estafetas:
            names.append(estafeta.nome) 
        return names
    
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="Seleciona o estafeta").pack()
        combo = ttk.Combobox(self, value = self.get_estafetas_names(estafetas))
        combo.pack()
        
        frame = tk.LabelFrame(self, text = "")
        msg = tk.Lab(frame, text = "")
        tk.Button(self, text = "Ver estafeta", command = lambda:  self.show_estafeta(combo.get(), msg, frame)).pack()
        
            
    def show_estafeta(self, estafeta_name, msg, frame):
        frame.config(text = estafeta_name)
        for e in estafetas:
            if e.nome == estafeta_name:
                estafeta = e
        frame.pack()
        msg.config(text = estafeta_to_string(estafeta))
        msg.pack()

     
from BaseConhecimento import *