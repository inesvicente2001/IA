import tkinter as tk
from tkinter import ttk
from math import *
from argparse import ArgumentParser
from pyswip import Prolog

class App(tk.Tk):
    def __init__(self):
        #PROLOG
        self.swipl = Prolog()
        self.swipl.consult("PartePratica.pl")
        ##self.STATIONS = [ans["S"] for ans in self.swipl.query("station(S)")]


        super().__init__()
        self.geometry("1000x1000")
        self.geometry()
        self.title('Green  Distribution')

        self.options = tk.StringVar()
        self.options.set("Selecione a query") # default value


        self.options_rua_freguesia = tk.StringVar()
        self.options_rua_freguesia.set("Selecione a opção desejada")  # default value



        self.queries = ["1: Identificação do estafeta que utilizou mais vezes um meio de transporte mais ecológico", 
                                "2: Identificação dos estafetas que entregaram  determinada(s)  encomenda(s)  a  um determinado cliente",
                                "3: Identificação dos clientes servidos por um determinado estafeta",
                                "4: Cálculo do valor faturado pela Green Distribution num determinado dia", 
                                "5: Identificação das  zonas  (e.g.,  rua  ou  freguesia)  com  maior  volume  de entregas por parte da Green Distribution", 
                                "6: Cálculo da classificação média de satisfação de cliente para um determinado estafeta", 
                                "7: Identificação do número total de entregas pelos diferentes meios de transporte, num determinado intervalo de tempo",
                                "8: Identificação do  número  total  de  entregas  pelos  estafetas,  num  determinado intervalo de tempo",
                                "9: Cálculo do  número  de  encomendas  entregues  e  não  entregues  pela  Green Distribution, num determinado período de tempo",
                                "10: Cálculo do peso total transportado por estafeta num determinado dia",
                                "11 (extra): Ver qual o cliente que pediu mais encomendas num certo período de tempo"]


        self.ops_queries = ["Query 1","Query 2","Query 3","Query 4","Query 5","Query 6","Query 7","Query 8","Query 9","Query 10","Query11 (extra)"]


        self.ops_rua_freguesia = ["Rua","Freguesia"]

        # create widget
        self.init_ops()

        #self.queries_fun()


    def init_ops(self):

        for widget in self.winfo_children():
             widget.destroy()

        label = ttk.Label(self,
                         text="Bem vindo à aplicação da Green Distribution.\nPor favor selecione o que pretende fazer:")

        label.pack(pady=10)

        # a button widget which will open a
        # new window on button click
        btn1 = ttk.Button(self,
                        text="Adicionar conhecimento",
                        command=self.ad_conhecimento)
        btn1.pack(pady=10)

        btn2 = tk.Button(self,
                        text="Testar queries",
                        command=self.queries_fun)
        btn2.pack(pady=10)

        btn3 = tk.Button(self,
                        text="Sair",
                        command=quit)
        btn3.pack(pady=10)



    def ad_conhecimento(self):
        for widget in self.winfo_children():
             widget.destroy()

        back = tk.Button(self,
                         text="Voltar",
                         command=self.init_ops)
        back.pack(pady=10)

        # A Label widget to show in toplevel
        ttk.Label(self,
                  text="Neste menu é possível criar um novo estafeta com a sua primeira encomenda ou adicionar uma encomenda a 1 estafeta já existente\n").pack()


        btn_conh = ttk.Button(self,
                          text="Adicionar estafeta",
                          command=self.conhe_selected)
        btn_conh.pack(pady=10)



        # output label
        self.output_label_conh = ttk.Label(self)
        self.output_label_conh.pack()




    def conhe_selected(self, *args):

            ttk.Label(self, text="Nome do estafeta:").pack()
            self.nome_estafeta = tk.Entry(self)
            self.nome_estafeta.bind("<Return>", self.ad_enc_estaf)
            self.nome_estafeta.pack()

            ttk.Label(self, text="Nome da encomenda:").pack()
            self.nome_encomenda = tk.Entry(self)
            self.nome_encomenda.bind("<Return>", self.ad_enc_estaf)
            self.nome_encomenda.pack()

            ttk.Label(self, text="Meio de transporte (bicicleta/mota/carro):").pack()
            self.meio_transporte = tk.Entry(self)
            self.meio_transporte.bind("<Return>", self.ad_enc_estaf)
            self.meio_transporte.pack()

            ttk.Label(self, text="Peso da encomenda:").pack()
            self.peso_encomenda = tk.Entry(self)
            self.peso_encomenda.bind("<Return>", self.ad_enc_estaf)
            self.peso_encomenda.pack()

            ttk.Label(self, text="Volume da encomenda:").pack()
            self.volume_encomenda = tk.Entry(self)
            self.volume_encomenda.bind("<Return>", self.ad_enc_estaf)
            self.volume_encomenda.pack()

            ttk.Label(self, text="Prazo de entrega:").pack()
            self.prazo_entrega = tk.Entry(self)
            self.prazo_entrega.bind("<Return>", self.ad_enc_estaf)
            self.prazo_entrega.pack()

            ttk.Label(self, text="Rua de entrega:").pack()
            self.rua_entrega = tk.Entry(self)
            self.rua_entrega.bind("<Return>", self.ad_enc_estaf)
            self.rua_entrega.pack()

            ttk.Label(self, text="Freguesia de entrega:").pack()
            self.freguesia_entrega = tk.Entry(self)
            self.freguesia_entrega.bind("<Return>", self.ad_enc_estaf)
            self.freguesia_entrega.pack()

            ttk.Label(self, text="Nome do cliente:").pack()
            self.nome_cliente = tk.Entry(self)
            self.nome_cliente.bind("<Return>", self.ad_enc_estaf)
            self.nome_cliente.pack()

            ttk.Label(self, text="Dia de entrega:").pack()
            self.dia_entrega = tk.Entry(self)
            self.dia_entrega.bind("<Return>", self.ad_enc_estaf)
            self.dia_entrega.pack()

            ttk.Label(self, text="Mês de entrega:").pack()
            self.mes_entrega = tk.Entry(self)
            self.mes_entrega.bind("<Return>", self.ad_enc_estaf)
            self.mes_entrega.pack()

            ttk.Label(self, text="Ano de entrega:").pack()
            self.ano_entrega = tk.Entry(self)
            self.ano_entrega.bind("<Return>", self.ad_enc_estaf)
            self.ano_entrega.pack()

            ttk.Label(self, text="Hora de entrega:").pack()
            self.hora_entrega = tk.Entry(self)
            self.hora_entrega.bind("<Return>", self.ad_enc_estaf)
            self.hora_entrega.pack()

            ttk.Label(self, text="Classificação (De (-1) a 5):").pack()
            self.classificacao = tk.Entry(self)
            self.classificacao.bind("<Return>", self.ad_enc_estaf)
            self.classificacao.pack()





            self.res_ad = tk.Label(self)
            self.res_ad.pack()

            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label_conh['text'] = f'Insira o nome do novo estafeta ou de um estafeta já existente e uma encomenda para o mesmo\n'
            self.ok_buton_conh()



    def check_values(self):

        if (self.meio_transporte.get() != "mota" and self.meio_transporte.get() != "bicicleta" and self.meio_transporte.get() != "carro" ):
            self.bool_check = False
            self.output_label_transporte = ttk.Label(self, foreground='red')
            self.output_label_transporte.pack()
            self.output_label_transporte['text'] = f'Por favor insira um dos seguintes meios de transporte: bicicleta/mota/carro'


        if (self.meio_transporte.get() == "bicicleta"):
            if(int(self.peso_encomenda.get()) < 1 or int(self.peso_encomenda.get()) > 5):
                self.bool_check = False
                self.output_label_peso_b = ttk.Label(self, foreground='red')
                self.output_label_peso_b.pack()
                self.output_label_peso_b['text'] = f'Por favor insira um valor de peso válido para a bicicleta(entre 1 e 5)'

        if (self.meio_transporte.get() == "mota"):
            if(int(self.peso_encomenda.get()) < 1 or int(self.peso_encomenda.get()) > 20):
                self.bool_check = False
                self.output_label_peso_m = ttk.Label(self, foreground='red')
                self.output_label_peso_m.pack()
                self.output_label_peso_m[ 'text'] = f'Por favor insira um valor de peso válido para a mota (entre 1 e 20)'

        if (self.meio_transporte.get() == "carro"):
            if(int(self.peso_encomenda.get()) < 1 or int(self.peso_encomenda.get()) > 100):
                self.bool_check = False
                self.output_label_peso_c = ttk.Label(self, foreground='red')
                self.output_label_peso_c.pack()
                self.output_label_peso_c['text'] = f'Por favor insira um valor de peso válido para o carro (entre 1 e 100)'


        if (int(self.prazo_entrega.get()) < 1):
            self.bool_check = False
            self.output_label_prazo = ttk.Label(self, foreground='red')
            self.output_label_prazo.pack()
            self.output_label_prazo['text'] = f'Por favor insira um prazo superior a 0'

        if(int(self.dia_entrega.get()) < 1 or int(self.dia_entrega.get()) > 31 ):
            self.bool_check = False
            self.output_label_dia = ttk.Label(self,foreground='red')
            self.output_label_dia.pack()
            self.output_label_dia['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_entrega.get()) < 1 or int(self.mes_entrega.get()) > 12):
            self.bool_check = False
            self.output_label_mes = ttk.Label(self, foreground='red')
            self.output_label_mes.pack()
            self.output_label_mes['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_entrega.get()) > 2021):
            self.bool_check = False
            self.output_label_ano = ttk.Label(self, foreground='red')
            self.output_label_ano.pack()
            self.output_label_ano['text'] = f'Por favor insira um ano igual ou anterior a 2021'

        if (int(self.hora_entrega.get()) < 0 or int(self.hora_entrega.get()) > 23):
            self.bool_check = False
            self.output_label_hora = ttk.Label(self, foreground='red')
            self.output_label_hora.pack()
            self.output_label_hora['text'] = f'Por favor insira uma hora entre 0 e 23'

        if (int(self.classificacao.get()) < (-1) or int(self.classificacao.get()) > 5):
            self.bool_check = False
            self.output_label_classificacao = ttk.Label(self, foreground='red')
            self.output_label_classificacao.pack()
            self.output_label_classificacao['text'] = f'Por favor insira uma classificacao entre -1 e 5'





    def ad_enc_estaf(self,event):

        self.bool_check = True
        #add_estafeta(gaspar, [encomenda(saco,1, 1, bicicleta, 1, rua(capa, gualtar), roger, tempo(3,1), 3)])

        self.check_values()



        if self.bool_check :
            # self.output_label_dia.destroy()
            self.res_ad.configure(
               text=next(self.swipl.query(
                   f"add_estafeta(L,{self.nome_estafeta.get()},encomenda({self.nome_encomenda.get()},{self.peso_encomenda.get()},{self.volume_encomenda.get()},{self.meio_transporte.get()},{self.prazo_entrega.get()},rua({self.rua_entrega.get()},{self.freguesia_entrega.get()}),{self.nome_cliente.get()},tempo({self.ano_entrega.get()},{self.mes_entrega.get()},{self.dia_entrega.get()},{self.hora_entrega.get()}),{self.classificacao.get()}))")))

    def queries_fun(self):

        for widget in self.winfo_children():
             widget.destroy()

        back = tk.Button(self,
                         text="Voltar",
                         command=self.init_ops)
        back.pack(pady=10)

        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        

        # A Label widget to show in toplevel
        ttk.Label(self,
                text ="São possíveis testar as seguintes queries:\n" + self.queries[0] + "\n" + self.queries[1] + "\n" + self.queries[2] + "\n"
                    + self.queries[3] + "\n" + self.queries[4] + "\n" + self.queries[5] + "\n" + self.queries[6] + "\n" + self.queries[7] + "\n"
                    + self.queries[8] + "\n" + self.queries[9] + "\n" + self.queries[10] + "\n").pack()
    
    
        option_menu = ttk.OptionMenu(
            self,
            self.options,
            self.ops_queries[0],
            *self.ops_queries,
            command = self.query_selected
        )
    
        option_menu.pack()

        # output label
        self.output_label = ttk.Label(self)
        self.output_label.pack()


    def ok_buton(self):
        back_to_queries = tk.Button(self,
                                    text="OK",
                                    command=self.queries_fun)
        back_to_queries.pack(pady=10)


    def ok_buton_conh(self):
        back_to_queries = tk.Button(self,
                                    text="OK",
                                    command=self.ad_conhecimento)
        back_to_queries.pack(pady=10)


    def clean(self):
        for widget in self.winfo_children():
             widget.destroy()


    def query_1_ans(self):
        #testagem com função prolog
        self.res.configure(text = next(self.swipl.query(f"query1(R)"))["R"])




    def query_2_ans(self,event):

        self.li = list(self.encs.get().split(","))
        self.res.configure(text=next(self.swipl.query(f"query2(Est,{self.li},{self.cl.get()})"))["Est"])


    def query_3_ans(self,event):
        #self.res.configure(text="Clientes servidos: " + str(eval(self.estafeta.get())))
        self.res.configure(
            text=next(self.swipl.query(f"query3(L,{self.estafeta.get()})"))["L"])

    def query_4_ans(self,event):
        self.bool_check_q4 = True

        if(int(self.dia_q4.get())<1 or int(self.dia_q4.get())>31):
            self.bool_check_q4 = False
            self.output_dia_q4 = ttk.Label(self, foreground='red')
            self.output_dia_q4.pack()
            self.output_dia_q4['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_q4.get()) < 1 or int(self.mes_q4.get()) > 12):
            self.bool_check_q4 = False
            self.output_mes_q4 = ttk.Label(self, foreground='red')
            self.output_mes_q4.pack()
            self.output_mes_q4['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_q4.get()) > 2021):
            self.bool_check_q4 = False
            self.output_ano_q4 = ttk.Label(self, foreground='red')
            self.output_ano_q4.pack()
            self.output_ano_q4['text'] = f'Por favor insira um ano anterior a 2021'



        if(self.bool_check_q4):
            self.res.configure(
                text=next(self.swipl.query(f"query4(L,{self.ano_q4.get()},{self.mes_q4.get()},{self.dia_q4.get()})"))["L"])

    def query_5_ans(self,event):
        ops_rua_freguesia = self.options_rua_freguesia.get()

        if(ops_rua_freguesia == "Rua"):
            # self.res.destroy()
            self.res.configure(
                text=next(self.swipl.query(f"query5(L,rua)"))["L"])

        if (ops_rua_freguesia == "Freguesia"):
            #self.res.destroy()
            self.res.configure(
                text=next(self.swipl.query(f"query5(L,freguesia)"))["L"])


    def query_6_ans(self,event):
        self.res.configure(
            text=next(self.swipl.query(f"query6(L,{self.estafeta_q6.get()})"))["L"])

    def query_7_ans(self,event):

        self.bool_check_q7 = True

        if (int(self.dia_inicio_q7.get()) < 1 or int(self.dia_inicio_q7.get()) > 31):
            self.bool_check_q7 = False
            self.output_dia_q7 = ttk.Label(self, foreground='red')
            self.output_dia_q7.pack()
            self.output_dia_q7['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_inicio_q7.get()) < 1 or int(self.mes_inicio_q7.get()) > 12):
            self.bool_check_q7 = False
            self.output_mes_q7 = ttk.Label(self, foreground='red')
            self.output_mes_q7.pack()
            self.output_mes_q7['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_inicio_q7.get()) > 2021):
            self.bool_check_q7 = False
            self.output_ano_q7 = ttk.Label(self, foreground='red')
            self.output_ano_q7.pack()
            self.output_ano_q7['text'] = f'Por favor insira um ano anterior a 2021'

        if (int(self.hora_inicio_q7.get()) < 0 or int(self.hora_inicio_q7.get()) > 23):
            self.bool_check_q7 = False
            self.output_hora_q7 = ttk.Label(self, foreground='red')
            self.output_hora_q7.pack()
            self.output_hora_q7['text'] = f'Por favor insira uma hora entre 0 e 23'

        if (int(self.dia_fim_q7.get()) < 1 or int(self.dia_fim_q7.get()) > 31):
            self.bool_check_q7 = False
            self.output_dia_q7f = ttk.Label(self, foreground='red')
            self.output_dia_q7f.pack()
            self.output_dia_q7f['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_fim_q7.get()) < 1 or int(self.mes_fim_q7.get()) > 12):
            self.bool_check_q7 = False
            self.output_mes_q7f = ttk.Label(self, foreground='red')
            self.output_mes_q7f.pack()
            self.output_mes_q7f['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_fim_q7.get()) > 2021):
            self.bool_check_q7 = False
            self.output_ano_q7f = ttk.Label(self, foreground='red')
            self.output_ano_q7f.pack()
            self.output_ano_q7f['text'] = f'Por favor insira um ano anterior a 2021'

        if (int(self.hora_fim_q7.get()) < 0 or int(self.hora_fim_q7.get()) > 23):
            self.bool_check_q7 = False
            self.output_hora_q7f = ttk.Label(self, foreground='red')
            self.output_hora_q7f.pack()
            self.output_hora_q7f['text'] = f'Por favor insira uma hora entre 0 e 23'




        if(self.bool_check_q7):
            self.res_bicicleta.configure(
                text=next(self.swipl.query(
                    f"query7(X,Y,Z,tempo({self.ano_inicio_q7.get()},{self.mes_inicio_q7.get()},{self.dia_inicio_q7.get()},{self.hora_inicio_q7.get()}),tempo({self.ano_fim_q7.get()},{self.mes_fim_q7.get()},{self.dia_fim_q7.get()},{self.hora_fim_q7.get()}))"))[
                    "Z"])
            self.res_mota.configure(
                text=next(self.swipl.query(
                    f"query7(X,Y,Z,tempo({self.ano_inicio_q7.get()},{self.mes_inicio_q7.get()},{self.dia_inicio_q7.get()},{self.hora_inicio_q7.get()}),tempo({self.ano_fim_q7.get()},{self.mes_fim_q7.get()},{self.dia_fim_q7.get()},{self.hora_fim_q7.get()}))"))[
                    "Y"])
            self.res_carro.configure(
                text=next(self.swipl.query(
                    f"query7(X,Y,Z,tempo({self.ano_inicio_q7.get()},{self.mes_inicio_q7.get()},{self.dia_inicio_q7.get()},{self.hora_inicio_q7.get()}),tempo({self.ano_fim_q7.get()},{self.mes_fim_q7.get()},{self.dia_fim_q7.get()},{self.hora_fim_q7.get()}))"))[
                    "X"])


    def query_8_ans(self,event):
        self.bool_check_q8 = True

        if (int(self.dia_inicio_q8.get()) < 1 or int(self.dia_inicio_q8.get()) > 31):
            self.bool_check_q8 = False
            self.output_dia_q8 = ttk.Label(self, foreground='red')
            self.output_dia_q8.pack()
            self.output_dia_q8['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_inicio_q8.get()) < 1 or int(self.mes_inicio_q8.get()) > 12):
            self.bool_check_q8 = False
            self.output_mes_q8 = ttk.Label(self, foreground='red')
            self.output_mes_q8.pack()
            self.output_mes_q8['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_inicio_q8.get()) > 2021):
            self.bool_check_q8 = False
            self.output_ano_q8 = ttk.Label(self, foreground='red')
            self.output_ano_q8.pack()
            self.output_ano_q8['text'] = f'Por favor insira um ano anterior a 2021'

        if (int(self.hora_inicio_q8.get()) < 0 or int(self.hora_inicio_q8.get()) > 23):
            self.bool_check_q8 = False
            self.output_hora_q8 = ttk.Label(self, foreground='red')
            self.output_hora_q8.pack()
            self.output_hora_q8['text'] = f'Por favor insira uma hora entre 0 e 23'

        if (int(self.dia_fim_q8.get()) < 1 or int(self.dia_fim_q8.get()) > 31):
            self.bool_check_q8 = False
            self.output_dia_q8f = ttk.Label(self, foreground='red')
            self.output_dia_q8f.pack()
            self.output_dia_q8f['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_fim_q8.get()) < 1 or int(self.mes_fim_q8.get()) > 12):
            self.bool_check_q8 = False
            self.output_mes_q8f = ttk.Label(self, foreground='red')
            self.output_mes_q8f.pack()
            self.output_mes_q8f['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_fim_q8.get()) > 2021):
            self.bool_check_q8 = False
            self.output_ano_q8f = ttk.Label(self, foreground='red')
            self.output_ano_q8f.pack()
            self.output_ano_q8f['text'] = f'Por favor insira um ano anterior a 2021'

        if (int(self.hora_fim_q8.get()) < 0 or int(self.hora_fim_q8.get()) > 23):
            self.bool_check_q8 = False
            self.output_hora_q8f = ttk.Label(self, foreground='red')
            self.output_hora_q8f.pack()
            self.output_hora_q8f['text'] = f'Por favor insira uma hora entre 0 e 23'

        if (self.bool_check_q8):
            self.res_q8.configure(
                text=next(self.swipl.query(
                    f"query8(L,tempo({self.ano_inicio_q8.get()},{self.mes_inicio_q8.get()},{self.dia_inicio_q8.get()},{self.hora_inicio_q8.get()}),tempo({self.ano_fim_q8.get()},{self.mes_fim_q8.get()},{self.dia_fim_q8.get()},{self.hora_fim_q8.get()}))"))[
                    "L"])

    def query_9_ans(self,event):
        self.bool_check_q9 = True

        if (int(self.dia_inicio_q9.get()) < 1 or int(self.dia_inicio_q9.get()) > 31):
            self.bool_check_q9 = False
            self.output_dia_q9 = ttk.Label(self, foreground='red')
            self.output_dia_q9.pack()
            self.output_dia_q9['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_inicio_q9.get()) < 1 or int(self.mes_inicio_q9.get()) > 12):
            self.bool_check_q9 = False
            self.output_mes_q9 = ttk.Label(self, foreground='red')
            self.output_mes_q9.pack()
            self.output_mes_q9['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_inicio_q9.get()) > 2021):
            self.bool_check_q9 = False
            self.output_ano_q9 = ttk.Label(self, foreground='red')
            self.output_ano_q9.pack()
            self.output_ano_q9['text'] = f'Por favor insira um ano anterior a 2021'

        if (int(self.hora_inicio_q9.get()) < 0 or int(self.hora_inicio_q9.get()) > 23):
            self.bool_check_q9 = False
            self.output_hora_q9 = ttk.Label(self, foreground='red')
            self.output_hora_q9.pack()
            self.output_hora_q9['text'] = f'Por favor insira uma hora entre 0 e 23'

        if (int(self.dia_fim_q9.get()) < 1 or int(self.dia_fim_q9.get()) > 31):
            self.bool_check_q9 = False
            self.output_dia_q9f = ttk.Label(self, foreground='red')
            self.output_dia_q9f.pack()
            self.output_dia_q9f['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_fim_q9.get()) < 1 or int(self.mes_fim_q9.get()) > 12):
            self.bool_check_q9 = False
            self.output_mes_q9f = ttk.Label(self, foreground='red')
            self.output_mes_q9f.pack()
            self.output_mes_q9f['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_fim_q9.get()) > 2021):
            self.bool_check_q9 = False
            self.output_ano_q9f = ttk.Label(self, foreground='red')
            self.output_ano_q9f.pack()
            self.output_ano_q9f['text'] = f'Por favor insira um ano anterior a 2021'

        if (int(self.hora_fim_q9.get()) < 0 or int(self.hora_fim_q9.get()) > 23):
            self.bool_check_q9 = False
            self.output_hora_q9f = ttk.Label(self, foreground='red')
            self.output_hora_q9f.pack()
            self.output_hora_q9f['text'] = f'Por favor insira uma hora entre 0 e 23'

        if (self.bool_check_q9):
            self.res_q9_val.configure(
                text=next(self.swipl.query(
                    f"query9(V,I,tempo({self.ano_inicio_q9.get()},{self.mes_inicio_q9.get()},{self.dia_inicio_q9.get()},{self.hora_inicio_q9.get()}),tempo({self.ano_fim_q9.get()},{self.mes_fim_q9.get()},{self.dia_fim_q9.get()},{self.hora_fim_q9.get()}))"))[
                    "V"])
            self.res_q9_inval.configure(
                text=next(self.swipl.query(
                    f"query9(V,I,tempo({self.ano_inicio_q9.get()},{self.mes_inicio_q9.get()},{self.dia_inicio_q9.get()},{self.hora_inicio_q9.get()}),tempo({self.ano_fim_q9.get()},{self.mes_fim_q9.get()},{self.dia_fim_q9.get()},{self.hora_fim_q9.get()}))"))[
                    "I"])


    def query_10_ans(self,event):
        self.bool_check_q10 = True

        if (int(self.dia.get()) < 1 or int(self.dia.get()) > 31):
            self.bool_check_q10 = False
            self.output_dia_q10 = ttk.Label(self, foreground='red')
            self.output_dia_q10.pack()
            self.output_dia_q10['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes.get()) < 1 or int(self.mes.get()) > 12):
            self.bool_check_q10 = False
            self.output_mes_q10 = ttk.Label(self, foreground='red')
            self.output_mes_q10.pack()
            self.output_mes_q10['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano.get()) > 2021):
            self.bool_check_q10 = False
            self.output_ano_q10 = ttk.Label(self, foreground='red')
            self.output_ano_q10.pack()
            self.output_ano_q10['text'] = f'Por favor insira um ano anterior a 2021'


        if(self.bool_check_q10):
            self.res_q10.configure(
                text=next(self.swipl.query(
                    f"query10(L,{self.ano.get()},{self.mes.get()},{self.dia.get()})"))[
                    "L"])

    def query_11_ans(self,event):
        self.bool_check_q11 = True

        if (int(self.dia_inicio_q11.get()) < 1 or int(self.dia_inicio_q11.get()) > 31):
            self.bool_check_q11 = False
            self.output_dia_q11 = ttk.Label(self, foreground='red')
            self.output_dia_q11.pack()
            self.output_dia_q11['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_inicio_q11.get()) < 1 or int(self.mes_inicio_q11.get()) > 12):
            self.bool_check_q11 = False
            self.output_mes_q11 = ttk.Label(self, foreground='red')
            self.output_mes_q11.pack()
            self.output_mes_q11['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_inicio_q11.get()) > 2021):
            self.bool_check_q11 = False
            self.output_ano_q11 = ttk.Label(self, foreground='red')
            self.output_ano_q11.pack()
            self.output_ano_q11['text'] = f'Por favor insira um ano anterior a 2021'

        if (int(self.hora_inicio_q11.get()) < 0 or int(self.hora_inicio_q11.get()) > 23):
            self.bool_check_q11 = False
            self.output_hora_q11 = ttk.Label(self, foreground='red')
            self.output_hora_q11.pack()
            self.output_hora_q11['text'] = f'Por favor insira uma hora entre 0 e 23'

        if (int(self.dia_fim_q11.get()) < 1 or int(self.dia_fim_q11.get()) > 31):
            self.bool_check_q11 = False
            self.output_dia_q11f = ttk.Label(self, foreground='red')
            self.output_dia_q11f.pack()
            self.output_dia_q11f['text'] = f'Por favor insira um dia entre 1 e 31'

        if (int(self.mes_fim_q11.get()) < 1 or int(self.mes_fim_q11.get()) > 12):
            self.bool_check_q11 = False
            self.output_mes_q11f = ttk.Label(self, foreground='red')
            self.output_mes_q11f.pack()
            self.output_mes_q11f['text'] = f'Por favor insira um mês entre 1 e 12'

        if (int(self.ano_fim_q11.get()) > 2021):
            self.bool_check_q11 = False
            self.output_ano_q11f = ttk.Label(self, foreground='red')
            self.output_ano_q11f.pack()
            self.output_ano_q11f['text'] = f'Por favor insira um ano anterior a 2021'

        if (int(self.hora_fim_q11.get()) < 0 or int(self.hora_fim_q11.get()) > 23):
            self.bool_check_q11 = False
            self.output_hora_q11f = ttk.Label(self, foreground='red')
            self.output_hora_q11f.pack()
            self.output_hora_q11f['text'] = f'Por favor insira uma hora entre 0 e 23'

        if (self.bool_check_q11):
            self.res_q11.configure(
                text=next(self.swipl.query(
                    f"query11(C,tempo({self.ano_inicio_q11.get()},{self.mes_inicio_q11.get()},{self.dia_inicio_q11.get()},{self.hora_inicio_q11.get()}),tempo({self.ano_fim_q11.get()},{self.mes_fim_q11.get()},{self.dia_fim_q11.get()},{self.hora_fim_q11.get()}))"))[
                    "C"])




    def query_selected(self, *args):
        op = self.options.get()

        #self.output_label['text'] = f'You selected: {op}'


        if op == "Query 1":

            ttk.Label(self, text="Estafeta que utiizou mais vezes um meio de transporte ecológico:").pack()
            #self.estafeta = tk.Entry(self)
            #self.estafeta.bind("<Return>", self.query_1_ans)
            #self.estafeta.pack()

            self.resposta = ttk.Button(self,
                              text="Resposta",
                              command=self.query_1_ans)
            self.resposta.pack(pady=10)

            self.res = tk.Label(self)
            self.res.pack()


            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'\n'
            self.ok_buton()

        if op == "Query 2":
            ttk.Label(self, text="Cliente:").pack()
            self.cl = tk.Entry(self)
            self.cl.bind("<Return>", self.query_2_ans)
            self.cl.pack()
            self.res = tk.Label(self)
            self.res.pack()

            ttk.Label(self, text="Nome(s) da(s) encomenda(s):").pack()
            self.encs = tk.Entry(self)
            self.encs.bind("<Return>", self.query_2_ans)
            self.encs.pack()
            self.res = tk.Label(self)
            self.res.pack()

            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'Identifique o cliente'
            self.ok_buton()

        if op == "Query 3":
            ttk.Label(self, text="Estafeta:").pack()
            self.estafeta = tk.Entry(self)
            self.estafeta.bind("<Return>", self.query_3_ans)
            self.estafeta.pack()
            self.res = tk.Label(self)
            self.res.pack()

            #Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'Identifique o estafeta\n'
            self.ok_buton()

        if op == "Query 4":
            ttk.Label(self, text="Dia:").pack()
            self.dia_q4 = tk.Entry(self)
            self.dia_q4.bind("<Return>", self.query_4_ans)
            self.dia_q4.pack()

            ttk.Label(self, text="Mês:").pack()
            self.mes_q4 = tk.Entry(self)
            self.mes_q4.bind("<Return>", self.query_4_ans)
            self.mes_q4.pack()

            ttk.Label(self, text="Ano:").pack()
            self.ano_q4 = tk.Entry(self)
            self.ano_q4.bind("<Return>", self.query_4_ans)
            self.ano_q4.pack()

            self.res = tk.Label(self)
            self.res.pack()


            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'Valor faturado pela Green Distribution no dia'
            self.ok_buton()

        if op == "Query 5":
            self.res = tk.Label(self)
            self.res.pack()

            option_menu_conh = ttk.OptionMenu(
                self,
                self.options_rua_freguesia,
                self.ops_rua_freguesia[0],
                *self.ops_rua_freguesia,
                command=self.query_5_ans
            )

            option_menu_conh.pack()


            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'Identifique se pretende ver a rua com o valor máximo ou a freguesia com valor máximo'
            self.ok_buton()

        if op == "Query 6":
            self.res = tk.Label(self)
            self.res.pack()

            ttk.Label(self, text="Estafeta:").pack()
            self.estafeta_q6 = tk.Entry(self)
            self.estafeta_q6.bind("<Return>", self.query_6_ans)
            self.estafeta_q6.pack()
            self.res = tk.Label(self)
            self.res.pack()


            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'Classificação média dos clientes para um determinado estafeta'
            self.ok_buton()

        if op == "Query 7":
            self.res_bicicleta = tk.Label(self)
            self.res_bicicleta.pack()

            self.res_mota = tk.Label(self)
            self.res_mota.pack()

            self.res_carro = tk.Label(self)
            self.res_carro.pack()

            # Data Inicio
            ttk.Label(self, text="Dia Inicio:").pack()
            self.dia_inicio_q7 = tk.Entry(self)
            self.dia_inicio_q7.bind("<Return>", self.query_7_ans)
            self.dia_inicio_q7.pack()

            ttk.Label(self, text="Mês Inicio:").pack()
            self.mes_inicio_q7 = tk.Entry(self)
            self.mes_inicio_q7.bind("<Return>", self.query_7_ans)
            self.mes_inicio_q7.pack()

            ttk.Label(self, text="Ano Início:").pack()
            self.ano_inicio_q7 = tk.Entry(self)
            self.ano_inicio_q7.bind("<Return>", self.query_7_ans)
            self.ano_inicio_q7.pack()

            ttk.Label(self, text="Hora Início:").pack()
            self.hora_inicio_q7 = tk.Entry(self)
            self.hora_inicio_q7.bind("<Return>", self.query_7_ans)
            self.hora_inicio_q7.pack()

            # Data fim
            ttk.Label(self, text="Dia Fim:").pack()
            self.dia_fim_q7 = tk.Entry(self)
            self.dia_fim_q7.bind("<Return>", self.query_7_ans)
            self.dia_fim_q7.pack()

            ttk.Label(self, text="Mês Fim:").pack()
            self.mes_fim_q7 = tk.Entry(self)
            self.mes_fim_q7.bind("<Return>", self.query_7_ans)
            self.mes_fim_q7.pack()

            ttk.Label(self, text="Ano Fim:").pack()
            self.ano_fim_q7 = tk.Entry(self)
            self.ano_fim_q7.bind("<Return>", self.query_7_ans)
            self.ano_fim_q7.pack()

            ttk.Label(self, text="Hora Fim:").pack()
            self.hora_fim_q7 = tk.Entry(self)
            self.hora_fim_q7.bind("<Return>", self.query_7_ans)
            self.hora_fim_q7.pack()

            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'Os valores para bicicleta, mota e carro são respetivamente:'
            self.ok_buton()

        if op == "Query 8":
            self.res_q8 = tk.Label(self)
            self.res_q8.pack()

            # Data Inicio
            ttk.Label(self, text="Dia Inicio:").pack()
            self.dia_inicio_q8 = tk.Entry(self)
            self.dia_inicio_q8.bind("<Return>", self.query_8_ans)
            self.dia_inicio_q8.pack()

            ttk.Label(self, text="Mês Inicio:").pack()
            self.mes_inicio_q8 = tk.Entry(self)
            self.mes_inicio_q8.bind("<Return>", self.query_8_ans)
            self.mes_inicio_q8.pack()

            ttk.Label(self, text="Ano Início:").pack()
            self.ano_inicio_q8 = tk.Entry(self)
            self.ano_inicio_q8.bind("<Return>", self.query_8_ans)
            self.ano_inicio_q8.pack()

            ttk.Label(self, text="Hora Início:").pack()
            self.hora_inicio_q8 = tk.Entry(self)
            self.hora_inicio_q8.bind("<Return>", self.query_8_ans)
            self.hora_inicio_q8.pack()

            # Data fim
            ttk.Label(self, text="Dia Fim:").pack()
            self.dia_fim_q8 = tk.Entry(self)
            self.dia_fim_q8.bind("<Return>", self.query_8_ans)
            self.dia_fim_q8.pack()

            ttk.Label(self, text="Mês Fim:").pack()
            self.mes_fim_q8 = tk.Entry(self)
            self.mes_fim_q8.bind("<Return>", self.query_8_ans)
            self.mes_fim_q8.pack()

            ttk.Label(self, text="Ano Fim:").pack()
            self.ano_fim_q8 = tk.Entry(self)
            self.ano_fim_q8.bind("<Return>", self.query_8_ans)
            self.ano_fim_q8.pack()

            ttk.Label(self, text="Hora Fim:").pack()
            self.hora_fim_q8 = tk.Entry(self)
            self.hora_fim_q8.bind("<Return>", self.query_8_ans)
            self.hora_fim_q8.pack()



            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'Identifique o período de tempo que pretende observar'
            self.ok_buton()

        if op == "Query 9":
            self.res_q9_val = tk.Label(self)
            self.res_q9_val.pack()

            self.res_q9_inval = tk.Label(self)
            self.res_q9_inval.pack()

            #Data Inicio
            ttk.Label(self, text="Dia Inicio:").pack()
            self.dia_inicio_q9 = tk.Entry(self)
            self.dia_inicio_q9.bind("<Return>", self.query_9_ans)
            self.dia_inicio_q9.pack()

            ttk.Label(self, text="Mês Inicio:").pack()
            self.mes_inicio_q9 = tk.Entry(self)
            self.mes_inicio_q9.bind("<Return>", self.query_9_ans)
            self.mes_inicio_q9.pack()

            ttk.Label(self, text="Ano Início:").pack()
            self.ano_inicio_q9 = tk.Entry(self)
            self.ano_inicio_q9.bind("<Return>", self.query_9_ans)
            self.ano_inicio_q9.pack()

            ttk.Label(self, text="Hora Inicio:").pack()
            self.hora_inicio_q9 = tk.Entry(self)
            self.hora_inicio_q9.bind("<Return>", self.query_9_ans)
            self.hora_inicio_q9.pack()

            #Data fim
            ttk.Label(self, text="Dia Fim:").pack()
            self.dia_fim_q9 = tk.Entry(self)
            self.dia_fim_q9.bind("<Return>", self.query_9_ans)
            self.dia_fim_q9.pack()

            ttk.Label(self, text="Mês Fim:").pack()
            self.mes_fim_q9 = tk.Entry(self)
            self.mes_fim_q9.bind("<Return>", self.query_9_ans)
            self.mes_fim_q9.pack()

            ttk.Label(self, text="Ano Fim:").pack()
            self.ano_fim_q9 = tk.Entry(self)
            self.ano_fim_q9.bind("<Return>", self.query_9_ans)
            self.ano_fim_q9.pack()

            ttk.Label(self, text="Hora Fim:").pack()
            self.hora_fim_q9 = tk.Entry(self)
            self.hora_fim_q9.bind("<Return>", self.query_9_ans)
            self.hora_fim_q9.pack()



            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'As entregas válidas e inválidas são respetivamente:'
            self.ok_buton()

        if op == "Query 10":
            self.res_q10 = tk.Label(self)
            self.res_q10.pack()


            ttk.Label(self, text="Dia:").pack()
            self.dia = tk.Entry(self)
            self.dia.bind("<Return>", self.query_10_ans)
            self.dia.pack()

            ttk.Label(self, text="Mês:").pack()
            self.mes = tk.Entry(self)
            self.mes.bind("<Return>", self.query_10_ans)
            self.mes.pack()

            ttk.Label(self, text="Ano:").pack()
            self.ano = tk.Entry(self)
            self.ano.bind("<Return>", self.query_10_ans)
            self.ano.pack()


            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'Identifique o dia que pretende ver:'
            self.ok_buton()

        if op == "Query11 (extra)":
            self.res_q11 = tk.Label(self)
            self.res_q11.pack()

            # Data Inicio
            ttk.Label(self, text="Dia Inicio:").pack()
            self.dia_inicio_q11 = tk.Entry(self)
            self.dia_inicio_q11.bind("<Return>", self.query_11_ans)
            self.dia_inicio_q11.pack()

            ttk.Label(self, text="Mês Inicio:").pack()
            self.mes_inicio_q11 = tk.Entry(self)
            self.mes_inicio_q11.bind("<Return>", self.query_11_ans)
            self.mes_inicio_q11.pack()

            ttk.Label(self, text="Ano Início:").pack()
            self.ano_inicio_q11 = tk.Entry(self)
            self.ano_inicio_q11.bind("<Return>", self.query_11_ans)
            self.ano_inicio_q11.pack()

            ttk.Label(self, text="Hora Inicio:").pack()
            self.hora_inicio_q11 = tk.Entry(self)
            self.hora_inicio_q11.bind("<Return>", self.query_11_ans)
            self.hora_inicio_q11.pack()

            # Data fim
            ttk.Label(self, text="Dia Fim:").pack()
            self.dia_fim_q11 = tk.Entry(self)
            self.dia_fim_q11.bind("<Return>", self.query_11_ans)
            self.dia_fim_q11.pack()

            ttk.Label(self, text="Mês Fim:").pack()
            self.mes_fim_q11 = tk.Entry(self)
            self.mes_fim_q11.bind("<Return>", self.query_11_ans)
            self.mes_fim_q11.pack()

            ttk.Label(self, text="Ano Fim:").pack()
            self.ano_fim_q11 = tk.Entry(self)
            self.ano_fim_q11.bind("<Return>", self.query_11_ans)
            self.ano_fim_q11.pack()

            ttk.Label(self, text="Hora Fim:").pack()
            self.hora_fim_q11 = tk.Entry(self)
            self.hora_fim_q11.bind("<Return>", self.query_11_ans)
            self.hora_fim_q11.pack()

            # Este texto deve ser o q se quer escrever primeiro, visto que esta label foi criada antes
            self.output_label['text'] = f'Identifique o intervalo que pretende ver:'
            self.ok_buton()








if __name__ == "__main__":
    app = App()
    app.mainloop()