import tkinter as tk
from PaginaInicial import *
import GrafoUI
import AdicionarRua
import BaseConhecimento

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(PaginaInicial)
        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            print("Hello")
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
app = App()
app.mainloop()