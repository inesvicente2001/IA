import tkinter as tk

class BaseConhecimento(tk.Frame):
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
        
        tk.button_bc = tk.Button(
            self,
            text="Ver Base de Conhecimento",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
            command = lambda: master.switch_frame(VerBaseConhecimento)
        ).pack()
        
        
        tk.button_ae = tk.Button(
            self,
            text="Adicionar à Base de Conhecimento",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
            command = lambda: master.switch_frame(AdicionarBaseConhecimento)
        ).pack()
               
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
            command = lambda: master.switch_frame(PaginaInicial)
        ).pack() 
         
from PaginaInicial import *
from VerBaseConhecimento import *
from AdicionarBaseConhecimento import *