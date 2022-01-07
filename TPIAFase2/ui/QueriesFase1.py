#TODO aqui vão ficar as queries da fase 1
import tkinter as tk
from tkinter import ttk
import sys
sys.path.insert(1, 'ln')
from queries import *
sys.path.insert(1, 'dl')
from db import *
from datetime import time

estafetas = estafetas_final
clientes = clientes_final

def estafetas_to_string(estafetas):
    string = ""
    for e in estafetas:
        string += e.nome + "\n"
    if string == "":
        string += "Nenhum estafeta fez entrega a este cliente"
    return string

def clients_to_string(clientes):
    string = ""
    for c in clientes:
        string += c.nome + "\n"
    if string == "":
        string += "Este estafeta não serviu nenhum cliente"
    return string


def veiculos_to_string(lista_veiculo):
    string = ""
    for (carro, valor) in lista_veiculo:
        string += carro + ": " + str(valor) + "\n"
    return string

def estafetas_e_encomendas_to_string(estafeta_e_encomendas):
    string = ""
    for (nome, nr) in estafeta_e_encomendas:
        string += nome + ": " + str(nr) + "\n"
    return string

def entregues_e_nao_to_string(entregues_e_nao):
    string = ""
    string += "Encomendas entregues: " + str(entregues_e_nao[0]) + "\n"
    string += "Encomendas não entregues: " + str(entregues_e_nao[1])
    return string

def q10_to_string(estafetas):
    string = ""
    for (e, a) in estafetas:
        string += e.nome + ": " + str(a) + "\n"
    return string
    

class QueriesFase1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global frame
        global msg
        frame = tk.LabelFrame(self, text = "")
        msg = tk.Label(frame, text = "")
        tk.label = tk.Label(
            self,
            text="Escolha a Query que quer fazer",
            font = ('Arial', 50)
        ).pack(pady=40)
        tk.Label(self, text = "Query 1 - identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico").pack()
        tk.Label(self, text = "Query 2 - identificar que estafetas entregaram determinada(s) encomenda(s) a um determinado cliente").pack()
        tk.Label(self, text = "Query 3 - identificar os clientes servidos por um determinado estafeta").pack()
        tk.Label(self, text = "Query 4 - calcular o valor faturado pela Green Distribution num determinado dia").pack()
        tk.Label(self, text = "Query 5 - identificar  qual  a rua com  maior  volume  de entregas por parte da Green Distribution").pack()
        tk.Label(self, text = "Query 6 - calcular a classificação média de satisfação de cliente para um determinado estafeta").pack()
        tk.Label(self, text = "Query 7 - identificar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo; ").pack()
        tk.Label(self, text = "Query 8 - identificar  o  número  total  de  entregas  pelos  estafetas,  num  determinado intervalo de tempo").pack()
        tk.Label(self, text = "Query 9 - calcular  o  número  de  encomendas  entregues  e  não  entregues  pela  Green Distribution, num determinado período de tempo").pack()
        tk.Label(self, text = "Query 10 - calcular o peso total transportado por estafeta num determinado dia").pack()
        
        
        tk.Label(self, text="Seleciona a procura").pack()
        comboP = ttk.Combobox(self, value = list(range(1,11)))
        comboP.pack()
        
        tk.button_graph = tk.Button(
            self,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: self.fazer_queries(comboP.get(), frame, msg)
        ).pack()
       
       
    def fazer_queries(self, query, frame, msg):
        flag = True
        if query == "":
            tk.Label(self, text = "Erro, seleciona uma query").pack()
            flag = False
        if flag == False:
            return   
        
        if query=="1":
            e = query1(estafetas)
            frame.config(text = "Query 1")
            frame.pack()
            msg.config(text = e.nome)
            msg.pack()
        
        if query=="2":
            self.query2()
     

        if query=="3":
            self.query3()
        
        #TODO n ter dia como argumento maybe e só fazer o rendimento total
        if query=="4":
            e = query4(estafetas)
            frame.config(text = "Query 4")
            frame.pack()
            msg.config(text = e)
            msg.pack()        

        if query=="5":
            most_frequent = query5(estafetas)
            print(most_frequent)
            frame.config(text = "Query 5")
            frame.pack()
            msg.config(text = most_frequent)
            msg.pack()
        
        if query=="6":
            self.query6()    

        if query=="7":
            self.query7()
        
        if query=="8":
            self.query8() 

        if query=="9":
            self.query9()
        
        if query=="10":
            e = query10(estafetas)
            frame.config(text = "Query 10")
            frame.pack()
            msg.config(text = q10_to_string(e))
            msg.pack()
            
            
    def query2(self): 
        window = tk.Tk()
        tk.Label(window, text = "Escolha o cliente").pack()
        lista = get_client_names()
        combo = ttk.Combobox(window, value = lista)
        combo.pack()
        tk.button_graph = tk.Button(
            window,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: self.query2_result(window, combo.get())
        ).pack()
        
    def query2_result(self, window, cliente):
        window.destroy()
        c = get_client_by_name(cliente)
        print(c.nome)
        print(estafetas)
        list_estafetas = query2(c, estafetas)
        
        frame.config(text = "Query 2")
        frame.pack()
        msg.config(text = estafetas_to_string(list_estafetas))
        msg.pack()        
       
       
    def query3(self): 
        window = tk.Tk()
        tk.Label(window, text = "Escolha o estafeta").pack()
        lista = get_estafetas_names()
        combo = ttk.Combobox(window, value = lista)
        combo.pack()
        tk.button_graph = tk.Button(
            window,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: self.query3_result(window, combo.get())
        ).pack()
        
    def query3_result(self, window, estafeta):
        window.destroy()
        e = get_estafeta_by_name(estafeta)
        list_clients = query3(e)
        
        frame.config(text = "Query 3")
        frame.pack()
        msg.config(text = clients_to_string(list_clients))
        msg.pack()         
            
        
    def query6(self): 
        window = tk.Tk()
        tk.Label(window, text = "Escolha o estafeta").pack()
        lista = get_estafetas_names()
        combo = ttk.Combobox(window, value = lista)
        combo.pack()
        tk.button_graph = tk.Button(
            window,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: self.query6_result(window, combo.get())
        ).pack()
        
    def query6_result(self, window, estafeta):
        window.destroy()
        e = get_estafeta_by_name(estafeta)
        classificacao = query6(e)
        
        frame.config(text = "Query 6")
        frame.pack()
        msg.config(text = classificacao)
        msg.pack()
        
    
    def query7(self): 
        window = tk.Tk()
        tk.Label(window, text = "Escolha a hora inicial").pack()
        combo1 = ttk.Combobox(window, value = list(range(24)))
        combo1.pack()
        tk.Label(window, text = "Escolha o minuto inicial").pack()
        combo2 = ttk.Combobox(window, value = list(range(60)))
        combo2.pack()
        tk.Label(window, text = "Escolha a hora final").pack()
        combo3 = ttk.Combobox(window, value = list(range(24)))
        combo3.pack()
        tk.Label(window, text = "Escolha o minuto final").pack()
        combo4 = ttk.Combobox(window, value = list(range(60)))
        combo4.pack()
        tk.button_graph = tk.Button(
            window,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: self.query7_result(window, combo1.get(), combo2.get(), combo3.get(), combo4.get())
        ).pack()
        
    def query7_result(self, window, hi, mi, hf, mf):
        window.destroy()
        tempo1 = time(int(hi), int(mi))
        tempo2 = time(int(hf), int(mf))
        lista_veiculo = query7(tempo1, tempo2, estafetas)
        
        frame.config(text = "Query 7")
        frame.pack()
        msg.config(text = veiculos_to_string(lista_veiculo))
        msg.pack()
        
        
    def query8(self): 
        window = tk.Tk()
        tk.Label(window, text = "Escolha a hora inicial").pack()
        combo1 = ttk.Combobox(window, value = list(range(24)))
        combo1.pack()
        tk.Label(window, text = "Escolha o minuto inicial").pack()
        combo2 = ttk.Combobox(window, value = list(range(60)))
        combo2.pack()
        tk.Label(window, text = "Escolha a hora final").pack()
        combo3 = ttk.Combobox(window, value = list(range(24)))
        combo3.pack()
        tk.Label(window, text = "Escolha o minuto final").pack()
        combo4 = ttk.Combobox(window, value = list(range(60)))
        combo4.pack()
        tk.button_graph = tk.Button(
            window,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: self.query8_result(window, combo1.get(), combo2.get(), combo3.get(), combo4.get())
        ).pack()
        
    def query8_result(self, window, hi, mi, hf, mf):
        window.destroy()
        tempo1 = time(int(hi), int(mi))
        tempo2 = time(int(hf), int(mf))
        estafeta_e_encomendas = query8(tempo1, tempo2, estafetas)
        
        frame.config(text = "Query 8")
        frame.pack()
        msg.config(text = estafetas_e_encomendas_to_string(estafeta_e_encomendas))
        msg.pack()
        
    def query9(self): 
        window = tk.Tk()
        tk.Label(window, text = "Escolha a hora inicial").pack()
        combo1 = ttk.Combobox(window, value = list(range(24)))
        combo1.pack()
        tk.Label(window, text = "Escolha o minuto inicial").pack()
        combo2 = ttk.Combobox(window, value = list(range(60)))
        combo2.pack()
        tk.Label(window, text = "Escolha a hora final").pack()
        combo3 = ttk.Combobox(window, value = list(range(24)))
        combo3.pack()
        tk.Label(window, text = "Escolha o minuto final").pack()
        combo4 = ttk.Combobox(window, value = list(range(60)))
        combo4.pack()
        tk.button_graph = tk.Button(
            window,
            text="Confirmar",
            width=25,
            height=5,
            command = lambda: self.query9_result(window, combo1.get(), combo2.get(), combo3.get(), combo4.get())
        ).pack()
        
    def query9_result(self, window, hi, mi, hf, mf):
        window.destroy()
        tempo1 = time(int(hi), int(mi))
        tempo2 = time(int(hf), int(mf))
        entregues_e_nao = query9(tempo1, tempo2, estafetas)
        
        frame.config(text = "Query 9")
        frame.pack()
        msg.config(text = entregues_e_nao_to_string(entregues_e_nao))
        msg.pack()