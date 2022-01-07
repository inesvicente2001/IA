import tkinter as tk

class PaginaInicial(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Green Distribution",
            font = ('Arial', 50)
        ).pack(pady=40)
        
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
        
  

from GrafoUI import *
from BaseConhecimento import *
from QueriesFase1 import *