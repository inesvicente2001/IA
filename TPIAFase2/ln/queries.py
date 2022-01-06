from datetime import time
import db as db
from dl.db import db

#No transporte in estafetas, só em servicos
def query1(estafetas):
    

def query2(cliente,estafetas):
    list_estafetas = []
    for x in estafetas:
        for y in x.encomendas:
            if (y.cliente.nome == cliente.nome):
                list_estafetas.append(x)
                break
            continue
        continue
    return list_estafetas

def query3(estafeta):
    list_clientes = []
    for x in estafeta.encomendas:
        if (x.cliente in list_clientes):
            continue
        list_clientes.append(x.client)
        continue
    return list_clientes

#Needs a money value
def query4(estafetas):

#Zonas? Múltiplas?
def query5(estafetas):


def query6(estafeta):
    return estafeta.classificacao


#Needs Servico, porque preciso de transporte.
def query7(time_start, time_end):


#Needs Servico. Need to understand how to switch it up.
def query8(time_start, time_end):


#Doing it with 0 reviews as non delivered.
#Delivery, depends on service done. Might need some help here.
def query9(time_start, time_end, estafetas):
    nEncomendasEntregues = 0
    nNãoEncomendasEntregues = 0
    for x in estafetas:
        

#Missing day idea. Might wanna check this later.
def query10(estafetas):
    time_start = time(0,0)
    time_end = time(23,59)
    peso_por_estafeta = []
    peso = 0
    for x in estafetas:
        for y in x.encomendas:
            peso = peso + y.peso
            continue
        peso_por_estafeta.append((x,peso))
        continue
    return peso_por_estafeta