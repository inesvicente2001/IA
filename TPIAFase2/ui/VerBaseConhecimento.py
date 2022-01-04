import tkinter as tk

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
        ).pack()
        
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: master.switch_frame(BaseConhecimento)
        ).pack() 
        
from BaseConhecimento import *