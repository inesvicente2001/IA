import tkinter as tk
import sys
sys.path.insert(1, 'dl')
from db import *


class AdicionarBaseConhecimento(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text = "Adicionar Conhecimento", font=("Arial", 30)).pack(pady = 25)

        
        tk.Button(
            self,
            text="Adicionar Clientes",
            width=25,
            height=5,
            command = lambda: master.switch_frame(AdicionarCliente)
        ).pack()
        
        
        tk.Button(
            self,
            text="Adicionar Encomenda",
            width=25,
            height=5,
            command = lambda: master.switch_frame(AdicionarEncomenda)
        ).pack()
        
        
        tk.Button(
            self,
            text="Criar Estafetas",
            width=25,
            height=5,
            command = lambda: master.switch_frame(AdicionarEstafeta)
        ).pack()
        
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: master.switch_frame(BaseConhecimento)
        ).pack()
        
        
class AdicionarCliente(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        
        tk.Label(self, text = "Adicionar Cliente", font=("Arial", 30)).pack(pady = 25)
        
        text_label = tk.Label(self, text = "Nome do novo Cliente")
        entry = tk.Entry(self)
        text_label.pack()
        entry.pack()
        
        tk.buttonAdd = tk.Button(
            self,
            text="Adicionar",
            width=25,
            height=5,
            command = lambda: self.adicionar(entry.get())
        ).pack()
        
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: master.switch_frame(AdicionarBaseConhecimento)
        ).pack()
        
    def adicionar(self, nome):
        flag = True
        clientes = get_client_names()
        name = tk.Label(self, text = "")
        if nome in clientes:
            name.config(text = "Erro, cliente com esse nome já existe")
            name.pack()
            flag = False
        if flag == False:
            return
        
        add_cliente(nome)
        
        name.config(text = "Cliente adicionado com sucesso")
        name.pack()
 
 
class AdicionarEstafeta(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text = "Adicionar Estafeta", font=("Arial", 30)).pack(pady = 25)
        
        text_label = tk.Label(self, text = "Nome do novo Estafeta")
        entry = tk.Entry(self)
        text_label.pack()
        entry.pack()
        
        tk.buttonAdd = tk.Button(
            self,
            text="Adicionar",
            width=25,
            height=5,
            command = lambda: self.adicionar(entry.get())
        ).pack()
        
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: master.switch_frame(AdicionarBaseConhecimento)
        ).pack()
        
    def adicionar(self, nome):
        flag = True
        estafetas = get_estafetas_names()
        name = tk.Label(self, text = "")
        if nome in estafetas:
            name.config(text = "Erro, estafeta com esse nome já existe")
            name.pack()
            flag = False
        if flag == False:
            return
        
        add_estafeta(nome)
        
        name.config(text = "Estafeta adicionado com sucesso")
        name.pack()
        

class AdicionarEncomenda(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text = "Adicionar Encomenda", font=("Arial", 30)).pack(pady = 25)
        
       
        text_label1 = tk.Label(self, text = "Nome da nova Encomenda")
        entry1 = tk.Entry(self)
        text_label1.pack()
        entry1.pack()
        
        text_label2 = tk.Label(self, text = "Peso da nova Encomenda(máx: 100kg)")
        entry2 = tk.Entry(self)
        text_label2.pack()
        entry2.pack()
        
        
        text_label3 = tk.Label(self, text = "Volume da nova Encomenda(máx: 20)")
        entry3 = tk.Entry(self)
        text_label3.pack()
        entry3.pack()
        
        text_label4 = tk.Label(self, text = "Rua para onde vai a encomenda")
        text_label4.pack()
        combo = ttk.Combobox(self, value = ruas_lst)
        combo.pack()
                
        text_label5 = tk.Label(self, text = "A que cliente pertence a encomenda")
        text_label5.pack()
        combo2 = ttk.Combobox(self, value = get_client_names())
        combo2.pack()
        
        
        text_label6 = tk.Label(self, text = "Prazo da entrega(horas)")
        text_label6.pack()
        combo3 = ttk.Combobox(self, value = list(range(24)))
        combo3.pack()
        
        
        text_label7 = tk.Label(self, text = "Prazo da entrega(minutos)")
        text_label7.pack()
        combo4 = ttk.Combobox(self, value = list(range(60)))
        combo4.pack()
        
        text_label8 = tk.Label(self, text = "Urgencia da encomenda")
        text_label8.pack()
        combo5 = ttk.Combobox(self, value = [0,1])
        combo5.pack()
        
        tk.buttonAdd = tk.Button(
            self,
            text="Adicionar",
            width=25,
            height=5,
            command = lambda: self.adicionar(entry1.get(), entry2.get(), entry3.get(), combo.get(), combo2.get(), combo3.get(), combo4.get(), combo5.get())
        ).pack()
        
        tk.buttonVoltar = tk.Button(
            self,
            text="Voltar",
            width=25,
            height=5,
            command = lambda: master.switch_frame(AdicionarBaseConhecimento)
        ).pack()
        
    def adicionar(self, nome, peso, volume, rua, client_nome, horas, minutos, boolean):
        
        if nome == "":
            tk.Label(self, text = "Erro, insira uma nome").pack()
            flag = False
            
        
        #verificar peso
        flag = True
        isInt = True
        try:
            p = int(peso)
        except ValueError:
            isInt = False
        if isInt:
            if p > 100 or p < 0:
                tk.Label(self, text = "Valor inválido para o peso").pack()
                flag = False
        else:
            tk.Label(self, text = "Valor inválido para o peso").pack()
            flag = False
            
        #verificar volume
        isInt = True
        try:
            v = int(volume)
        except ValueError:
            isInt = False
        if isInt:
            if v > 100 or v < 0:
                tk.Label(self, text = "Valor inválido para o volume").pack()
                flag = False
        else:
            tk.Label(self, text = "Valor inválido para o volume").pack()
            flag = False
            
        if rua == "":
            tk.Label(self, text = "Erro, escolha uma rua").pack()
            flag = False
            
        if client_nome == "":
            tk.Label(self, text = "Erro, escolha um cliente").pack()
            flag = False
        
        if horas == "":
            tk.Label(self, text = "Erro, escolha uma hora para a entrega").pack()
            flag = False
            
        if minutos == "":
            tk.Label(self, text = "Erro, escolha os minutos para a entrega").pack()
            flag = False
            
        if boolean == "":
            tk.Label(self, text = "Erro, escolha os minutos para a entrega").pack()
            flag = False
            
        
        if flag == False:
            return
        
        add_encomenda(nome, int(peso), int(volume), rua, client_nome, int(horas), int(minutos), int(boolean))
        tk.Label(self, text = "Encomenda adicionada com sucesso!", font = ("Arial", 20)).pack()
            
        print("passei os testes")
        return
            
            
        
        
from BaseConhecimento import *
from FazerEncomenda import *
from AdicionarRua import *