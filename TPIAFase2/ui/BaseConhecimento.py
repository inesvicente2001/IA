import tkinter as tk

class BaseConhecimento(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text = "Base de conhecimento", font=("Arial", 30)).pack(pady = 25)
        
        tk.button_bc = tk.Button(
            self,
            text="Ver Base de Conhecimento",
            width=25,
            height=5,

            command = lambda: master.switch_frame(VerBaseConhecimento)
        ).pack()
        
        
        tk.button_ae = tk.Button(
            self,
            text="Adicionar à Base de Conhecimento",
            width=25,
            height=5,

            command = lambda: master.switch_frame(AdicionarBaseConhecimento)
        ).pack()
               
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,

            command = lambda: master.switch_frame(PaginaInicial)
        ).pack() 
        
        
        
         
from PaginaInicial import *
from VerBaseConhecimento import *
from AdicionarBaseConhecimento import *