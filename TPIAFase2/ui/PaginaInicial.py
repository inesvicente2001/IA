import tkinter as tk

class PaginaInicial(tk.Frame):
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
        
        tk.button_graph = tk.Button(
            self,
            text="Grafo",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
            command = lambda: master.switch_frame(GrafoUI)
        ).pack()
        
        
        tk.button_dL = tk.Button(
            self,
            text="Base de conhecimento",
            width=25,
            height=5,
            bg="yellow",
            fg="blue",
            command = lambda: master.switch_frame(BaseConhecimento)
        ).pack()
                
    

from GrafoUI import *
from BaseConhecimento import *