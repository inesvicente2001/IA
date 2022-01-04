import tkinter as tk

class PaginaInicial(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Hello, Tkinter",
            width=15,
            height=5
        ).pack()
        
        tk.button_graph = tk.Button(
            self,
            text="Grafo",
            width=25,
            height=5,
            command = lambda: master.switch_frame(GrafoUI)
        ).pack()
        
        
        tk.button_dL = tk.Button(
            self,
            text="Base de conhecimento",
            width=25,
            height=5,
            command = lambda: master.switch_frame(BaseConhecimento)
        ).pack()
          
        tk.button_queries1 = tk.Button(
            self,
            text="Queries Fase 1",
            width=25,
            height=5,
            command = lambda: master.switch_frame(QueriesFase1)
        ).pack()   
        
           
        tk.button_queries2 = tk.Button(
            self,
            text="Queries Fase 2",
            width=25,
            height=5,
            command = lambda: master.switch_frame(QueriesFase2)
        ).pack()      

from GrafoUI import *
from BaseConhecimento import *