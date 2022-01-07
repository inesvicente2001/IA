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
import time as time_

e = estafetas_final
estafeta = []

procuras = [
    "Depth-first",
    "Iterativa",
    "Breadth-first",
    "Gulosa",
    "A*",
]

criterios = [
    "distância",
    "ecológico (tempo)"
]

def get_ruas_encomendas(encomendas):
    ruas = []
    for encomenda in encomendas:
        ruas.append(encomenda.rua)
    return ruas

def calcula_caminho_bilp(root, ruas, procura, criterio, opcao, estafeta, profundidade):
    root.destroy()
    ruas = get_ruas_encomendas(estafeta.encomendas)
    ruas_aux = ruas[:]
    if criterio == "distância" and opcao == "Sim":
        start_time = time_.time()
        (path, tempo) = travessia_varias_encomendas_distancia_uma(ruas, procura, estafeta, profundidade)
        tempo_r = (time_.time() - start_time)
    if criterio == "distância" and opcao == "Nao":
        start_time = time_.time()
        (path, tempo) = travessia_varias_encomendas_distancia(ruas, procura, estafeta, profundidade)
        tempo_r = (time_.time() - start_time)
    #TODO acabar com as outras opções
    search_window = tk.Tk()
    tk.Label(
        search_window,
        text="Entregas efetuadas com sucesso!",
        font = ("Arial", 20)
    ).pack(pady=10)
    
    tk.buttonGrafo = tk.Button(
        search_window,
        text="Ver grafo com procura",
        width=25,
        height=5,
        command = lambda: show_search_graph(path, ruas_aux)
    ).pack()
    
    
    tk.buttonVoltar = tk.Button(
        search_window,
        text="Voltar",
        width=25,
        height=5,
        command = lambda: search_window.destroy()
    ).pack()
    
    
    frame = tk.LabelFrame(search_window, text = "tempo do estafeta")
    frame.pack()
    #print("{:.2f}". format(total_cost)) # para ser dado print só com 2 casas decimais
    msg = tk.Label(frame, text = "{:.2f} horas". format(tempo))
    msg.pack()
    
    
    frame3 = tk.LabelFrame(search_window, text = "tempo a calcular a procura")
    frame3.pack()
    msg3 = tk.Label(frame3, text =  "{:.2f} segundos". format(tempo_r))
    msg3.pack()
    
    frame2 = tk.LabelFrame(search_window, text = "Caminho percorrido")
    frame2.pack()
    
    ruas_path = get_ruas(path)
    #print(ruas_path)
    
    msg2 = tk.Label(frame2, text = path_to_string(ruas_path))
    msg2.pack()
        
        
def calcula_caminho(ruas, procura, criterio, opcao, estafeta):
    print(opcao)
    profundidade = 0
    if procura == "Iterativa" :
        root = tk.Tk()
        tk.Label(root, text="Seleciona a profundidade").pack()
        comboC = ttk.Combobox(root, value = list(range(nr_vertices)))
        comboC.pack()
        tk.buttonConfirmar = tk.Button(
            root,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: calcula_caminho_bilp(root, ruas, procura, criterio, opcao, estafeta, comboC.get())
        ).pack()()
        
    #if procura == "Gulosa" :
    #    root = tk.Tk()
    #    tk.Label(root, text="Seleciona a heuristica").pack()
    #    comboC = ttk.Combobox(root, value = list(range(nr_vertices)))
    #    comboC.pack()
    #    tk.buttonConfirmar = tk.Button(
    #        root,
    #        text="Confirmar",
    #        width=25,
    #        height=5,
    #        command = lambda: calcula_caminho_bilp(root, ruas, procura, criterio, opcao, estafeta, comboC.get())
    #    ).pack()
        
        
    if criterio == "distância" and opcao == "Sim":
        start_time = time_.time()
        (path, tempo_e) = travessia_varias_encomendas_distancia_uma(ruas, procura, estafeta, profundidade)
        tempo_r = (time_.time() - start_time)
        return (path, tempo_e, tempo_r)
    if criterio == "distância" and opcao == "Nao":
        start_time = time_.time()
        (path, tempo_e) = travessia_varias_encomendas_distancia(ruas, procura, estafeta, profundidade)
        tempo_r = (time_.time() - start_time)
        return (path, tempo_e, tempo_r)

    #TODO acabar isto com as outras procuras
    
def show_graph():
    load_graph()   
    
def show_search_graph(path, ruas):
    print(ruas)
    load_search_graph(path, ruas)

class FazerEncomenda(tk.Frame) :

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Fazer entregas",
            font = ("Arial", 30)
        ).pack(pady = 25)
        
        ruas = self.get_ruas()
        ruas.sort()
        
        
        #rua = tk.StringVar()
        #rua.set("Rua para onde fazer a entrega") #oq aparece antes de ver as opções do dropdown
        #optionsR = tk.OptionMenu(self, rua, *ruas).pack() #Drop down menu com freguesias a escolher
        
        #Drop down menu
        tk.Label(self, text="Seleciona o estafeta").pack()
        combo = ttk.Combobox(self, value = self.get_estafetas_names(e))
        combo.pack()
        
        frame = tk.LabelFrame(self, text = "")
        msg = tk.Label(frame, text = "")
        tk.Button(self, text = "Ver estafeta", command = lambda:  self.show_estafeta(combo.get(), msg, frame)).pack()
        
            
        tk.Label(self, text="Seleciona a procura").pack()
        comboP = ttk.Combobox(self, value = procuras)
        comboP.pack()

        
        tk.Label(self, text="Seleciona o critério").pack()
        comboC = ttk.Combobox(self, value = criterios)
        comboC.pack()
        
        
        tk.Label(self, text="Voltar à base depois de cada encomenda").pack()
        opcoes = ["Sim", "Nao"]
        comboO = ttk.Combobox(self, value = opcoes)
        comboO.pack()
        #procura = tk.StringVar()
        #procura.set("Seleciona tipo de procura") #oq aparece antes de ver as opções do dropdown
        #optionsP = tk.OptionMenu(self, procura, *procuras).pack() #Drop down menu com procuras a escolher
        
        #tk.Label(self, text="Seleciona o critério").pack()
        #combo = ttk.Combobox(self, value = *procuras)
        #combo.pack()
        
        tk.buttonConfirmar = tk.Button(
            self,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: self.confirmar(combo.get(), comboP.get(), comboC.get(), comboO.get())
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
        
    def get_estafetas_names(self, estafetas):
        names = []
        for estafeta in estafetas:
            names.append(estafeta.nome) 
        return names

    def show_estafeta(self, estafeta_name, msg, frame):
        frame.config(text = estafeta_name)
        for es in e:
            if es.nome == estafeta_name:
                estafeta = es
        frame.pack()
        msg.config(text = estafeta_to_string(estafeta))
        msg.pack()
    
    def get_ruas(self):
        g = Graph.Read_GraphML("teste.graphml")
        return g.vs["rua"]
    
    def confirmar(self, estafeta_name, procura, criterio, opcao):
        global estafeta
        for es in e:
            if es.nome == estafeta_name:
                estafeta = es
                print(estafeta)
        flag = True
        if estafeta_name == "":
            tk.Label(self, text = "Erro, seleciona um estafeta para fazer a entrega").pack()
            flag = False
            
        if procura == "":
            tk.Label(self, text = "Erro, seleciona o tipo de procura").pack()
            flag = False
            
        if criterio == "":
            tk.Label(self, text = "Erro, seleciona o critério").pack()
            flag = False
        
        if opcao == "":
            tk.Label(self, text = "Erro, seleciona se queres que ele volte à base depois de cada encomenda").pack()
            flag = False
            
        if estafeta.encomendas == []:
            tk.Label(self, text = "Erro, este estafeta não tem encomendas pendentes").pack()
            flag = False
        
        if flag == False:
            return
        
        ruas = get_ruas_encomendas(estafeta.encomendas)
        ruas_aux = ruas[:]
        (path, tempo, tempo_r) = calcula_caminho(ruas, procura, criterio, opcao, estafeta)
        
        
        search_window = tk.Tk()
        tk.Label(
            search_window,
            text="Entregas efetuadas com sucesso!",
            font = ("Arial", 20)
        ).pack(pady=10)
        
        tk.buttonGrafo = tk.Button(
            search_window,
            text="Ver grafo com procura",
            width=25,
            height=5,
            command = lambda: show_search_graph(path, ruas_aux)
        ).pack()
        
        
        tk.buttonVoltar = tk.Button(
            search_window,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: search_window.destroy()
        ).pack()
        
        
        frame = tk.LabelFrame(search_window, text = "tempo do estafeta")
        frame.pack()
        msg = tk.Label(frame, text =  "{:.2f} horas". format(tempo))
        msg.pack()
        
        frame3 = tk.LabelFrame(search_window, text = "tempo a calcular a procura")
        frame3.pack()
        msg3 = tk.Label(frame3, text =  "{:.2f} segundos". format(tempo_r))
        msg3.pack()
        
        frame2 = tk.LabelFrame(search_window, text = "Caminho percorrido")
        frame2.pack()
        
        ruas_path = get_ruas(path)
        #print(ruas_path)
        
        msg2 = tk.Label(frame2, text = path_to_string(ruas_path))
        msg2.pack()


def path_to_string(path):
    string = ""
    for e in path:
        string += e + "\n"
    return string        
        
        
from GrafoUI import *
from VerBaseConhecimento import estafeta_to_string