import sys
sys.path.insert(1, 'dl')
from db import *
import tkinter as tk
from igraph import *
  
g = Graph.Read_GraphML("teste.graphml")
e = estafetas_final
c = clientes_final
es = encomendas_final
s = servicos_final

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
    string = string + "Encomendas por fazer: " + str(len(estafeta.encomendas))
    string += "\n"
    string = string + "Serviços feitos: " + str(len(estafeta.servicos))
    string += "\n"
    string = string + "Castigo: " + str(estafeta.castigo)
    return string


class VerBaseConhecimento(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text = "Ver conhecimento", font=("Arial", 30)).pack(pady = 25)
        

        
        tk.Button(
            self,
            text="Ver Clientes",
            width=25,
            height=5,
            command = lambda: master.switch_frame(VerClientes)
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
            command = lambda: master.switch_frame(VerEncomendas)
        ).pack()
        
        tk.Button(
            self,
            text="Ver Serviços",
            width=25,
            height=5,
            command = lambda: master.switch_frame(VerServico)
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
        
        tk.Label(self, text = "Ver ruas", font=("Arial", 30)).pack(pady = 25)
        
        tk.Label(self, text="Seleciona a freguesia").pack()
        combo = ttk.Combobox(self, value = get_freguesias())
        combo.pack()
        
        frame = tk.LabelFrame(self, text = "")
        msg = tk.Label(frame, text = "")
        tk.Button(self, text = "Ver ruas", command = lambda:  self.show_ruas(combo.get(), msg, frame)).pack()
        
        tk.Button(self, text = "Voltar", command = lambda: master.switch_frame(VerBaseConhecimento)).pack()
        
            
    def show_ruas(self, freguesia, msg, frame):
        ruas = get_ruas_freguesia(freguesia)
        frame.config(text = freguesia)  
        frame.pack()
        msg.config(text = ruas_to_string(ruas))
        msg.pack()
            
class VerEstafetas(tk.Frame):
    
    
    def get_estafetas_names(self):
        names = []
        for estafeta in e:
            names.append(estafeta.nome) 
        return names
    
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text = "Ver Estafetas", font=("Arial", 30)).pack(pady = 25)
        
        tk.Label(self, text="Seleciona o estafeta").pack()
        combo = ttk.Combobox(self, value = self.get_estafetas_names())
        combo.pack()
        
        frame = tk.LabelFrame(self, text = "")
        msg = tk.Label(frame, text = "")
        tk.Button(self, text = "Ver estafeta", command = lambda:  self.show_estafeta(combo.get(), msg, frame)).pack()
        
        tk.Button(self, text = "Voltar", command = lambda: master.switch_frame(VerBaseConhecimento)).pack()
            
    def show_estafeta(self, estafeta_name, msg, frame):
        frame.config(text = estafeta_name)
        for es in e:
            if es.nome == estafeta_name:
                estafeta = es
        frame.pack()
        msg.config(text = estafeta_to_string(estafeta))
        msg.pack()


class VerClientes(tk.Frame):
    
    def get_clientes(self):
        string = ""
        for cliente in c:
            string += cliente.nome
            string += "\n"
        return string
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        
        tk.Label(self, text = "Ver Clientes", font=("Arial", 30)).pack(pady = 25)
        
        frame = tk.LabelFrame(self, text = "Clientes")
        msg = tk.Label(frame, text = self.get_clientes())
        frame.pack()
        msg.pack()
        #tk.Button(self, text = "Ver estafeta", command = lambda:  self.show_estafeta(combo.get(), msg, frame)).pack()
        
        tk.Button(self, text = "Voltar", command = lambda: master.switch_frame(VerBaseConhecimento)).pack()
        
class VerEncomendas(tk.Frame):
    
    def encomenda_to_string(self, encomenda):
        string = ""
        string += "id: " + str(encomenda.id) + "\n"
        string += "nome: " + encomenda.nome + "\n"
        string += "peso: " + str(encomenda.peso) + "\n"
        string += "volume: " + str(encomenda.volume) + "\n"
        string += "rua a ser entregue: " + encomenda.rua + "\n"
        string += "cliente: " + encomenda.cliente.nome + "\n"
        string += "prazo da entrega: " + str(encomenda.prazo) 
        return string
    
    def get_encomenda_names(self):
        names = []
        for encomenda in es:
            names.append(encomenda.nome) 
        return names
    
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text = "Ver Encomenda", font=("Arial", 30)).pack(pady = 25)
        
        tk.Label(self, text="Seleciona a encomenda").pack()
        combo = ttk.Combobox(self, value = self.get_encomenda_names())
        combo.pack()
        
        frame = tk.LabelFrame(self, text = "")
        msg = tk.Label(frame, text = "")
        tk.Button(self, text = "Ver encomenda", command = lambda:  self.show_encomenda(combo.get(), msg, frame)).pack()
        
        tk.Button(self, text = "Voltar", command = lambda: master.switch_frame(VerBaseConhecimento)).pack()
            
    def show_encomenda(self, encomenda_name, msg, frame):
        frame.config(text = encomenda_name)
        for e in es:
            if e.nome == encomenda_name:
                encomenda = e
        frame.pack()
        msg.config(text = self.encomenda_to_string(encomenda))
        msg.pack()


class VerServico(tk.Frame):
    
    def servico_to_string(self, s):
        string = ""
        string += "id: " + str(s.id) + "\n"
        string += "nome: " + s.nome + "\n"
        string += "rua que foi entregue: " + s.rua + "\n"
        string += "classificacao: " + str(s.classificacao) + "\n"
        string += "Chegou a tempo? " + str(s.chegada) + "\n"
        string += "penalização: " + str(s.penalizacao) + "\n"
        string += "transporte usado: " + str(s.transporte)
        return string
    
    def get_servico_names(self):
        names = []
        for servico in s:
            names.append(servico.nome) 
        return names
    
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text = "Ver Serviços", font=("Arial", 30)).pack(pady = 25)
        
        tk.Label(self, text="Seleciona o serviço").pack()
        combo = ttk.Combobox(self, value = self.get_servico_names())
        combo.pack()
        
        frame = tk.LabelFrame(self, text = "")
        msg = tk.Label(frame, text = "")
        tk.Button(self, text = "Ver servico", command = lambda:  self.show_servico(combo.get(), msg, frame)).pack()
        
        tk.Button(self, text = "Voltar", command = lambda: master.switch_frame(VerBaseConhecimento)).pack()
            
    def show_servico(self, servico_name, msg, frame):
        frame.config(text = servico_name)
        for ser in s:
            if ser.nome == servico_name:
                servico = ser
        frame.pack()
        msg.config(text = self.servico_to_string(servico))
        msg.pack()

        
from BaseConhecimento import *