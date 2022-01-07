#TODO aqui vão ficar as queries da fase 1
import tkinter as tk
from tkinter import ttk

class QueriesFase1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Escolha a Query que quer fazer",
            font = ('Arial', 50)
        ).pack(pady=40)
        tk.Label(self, text = "Query 1 - identificar o estafeta que utilizou mais vezes um meio de transporte mais ecológico").pack()
        tk.Label(self, text = "Query 2 - identificar que estafetas entregaram determinada(s) encomenda(s) a um determinado cliente").pack()
        tk.Label(self, text = "Query 3 - identificar os clientes servidos por um determinado estafeta").pack()
        tk.Label(self, text = "Query 4 - calcular o valor faturado pela Green Distribution num determinado dia").pack()
        tk.Label(self, text = "Query 5 - identificar  quais  as  zonas  (e.g.,  rua  ou  freguesia)  com  maior  volume  de entregas por parte da Green Distribution").pack()
        tk.Label(self, text = "Query 6 - calcular a classificação média de satisfação de cliente para um determinado estafeta").pack()
        tk.Label(self, text = "Query 7 - identificar o número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo; ").pack()
        tk.Label(self, text = "Query 8 - identificar  o  número  total  de  entregas  pelos  estafetas,  num  determinado intervalo de tempo").pack()
        tk.Label(self, text = "Query 9 - calcular  o  número  de  encomendas  entregues  e  não  entregues  pela  Green Distribution, num determinado período de tempo").pack()
        tk.Label(self, text = "Query 10 - calcular o peso total transportado por estafeta num determinado dia").pack()
        
        
        tk.Label(self, text="Seleciona a procura").pack()
        comboP = ttk.Combobox(self, value = list(range(1,11)))
        comboP.pack()
        frame = tk.LabelFrame(self, text = "")
        msg = tk.Label(frame, text = "")
        
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
            frame.config(text = "Query 1")
            frame.pack()
            msg.config(text = "Olá!")
            msg.pack()
        
        if query=="2":
            frame.config(text = "Query 2")
            frame.pack()
            msg.config(text = "Olá2!")
            msg.pack()        

        if query=="3":
            frame.config(text = "Query 3")
            frame.pack()
            msg.config(text = "Olá!")
            msg.pack()
        
        if query=="4":
            frame.config(text = "Query 4")
            frame.pack()
            msg.config(text = "Olá2!")
            msg.pack()        

        if query=="5":
            frame.config(text = "Query 5")
            frame.pack()
            msg.config(text = "Olá!")
            msg.pack()
        
        if query=="6":
            frame.config(text = "Query 6")
            frame.pack()
            msg.config(text = "Olá2!")
            msg.pack()        

        if query=="7":
            frame.config(text = "Query 7")
            frame.pack()
            msg.config(text = "Olá!")
            msg.pack()
        
        if query=="8":
            frame.config(text = "Query 8")
            frame.pack()
            msg.config(text = "Olá2!")
            msg.pack()        

        if query=="9":
            frame.config(text = "Query 9")
            frame.pack()
            msg.config(text = "Olá!")
            msg.pack()
        
        if query=="10":
            frame.config(text = "Query 10")
            frame.pack()
            msg.config(text = "Olá2!")
            msg.pack()