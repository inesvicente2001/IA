import tkinter as tk

class AdicionarBaseConhecimento(tk.Frame):
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
            text="Adicionar Clientes",
            width=25,
            height=5,
        ).pack()
        
        #n sei se vou deixar isto aqui
        tk.Button(
            self,
            text="Adicionar Rua",
            width=25,
            height=5,
            command = lambda: master.switch_frame(AdicionarRua)
        ).pack()
        
        tk.Button(
            self,
            text="Adicionar Encomenda",
            width=25,
            height=5,
            command = lambda: master.switch_frame(FazerEncomenda)
        ).pack()
        
        
        tk.Button(
            self,
            text="Criar Estafetas",
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
from FazerEncomenda import *
from AdicionarRua import *