import tkinter as tk

class GrafoUI(tk.Frame) :

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.label = tk.Label(
            self,
            text="Hello, Tkinter",
            fg="white",
            bg="black",
            width=15,
            height=5
        ).pack()
       
        
        tk.buttonGraph = tk.Button(
            self,
            text="Adicionar Rua",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
        ).pack()
        
        tk.buttonDL = tk.Button(
            self,
            text="Ver base de conhecimento",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
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