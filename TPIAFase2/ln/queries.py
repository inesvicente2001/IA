import sys
sys.path.insert(1, 'dl')
from datetime import datetime, timedelta, time
from tkinter.constants import N, NE
from db import Estafeta, Transporte
#from dl.db import Estafeta, Transporte, db
from collections import Counter

def query1(estafetas):
    estafeta_mais_ecologico = None
    fator_ecologico = 0
    maior_fator_ecologico = 0
    for x in estafetas:
        fator_ecologico = 0
        for y in x.servicos:
            fator_ecologico = fator_ecologico + y.transporte
            continue
        if (fator_ecologico > maior_fator_ecologico):
            maior_fator_ecologico = fator_ecologico
            estafeta_mais_ecologico = x
        continue
    return estafeta_mais_ecologico

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

def query4(estafetas,day):
    rendimento = 0
    time_start = datetime.combine(day,time.min)
    time_end = datetime.combine(day,time.max)
    for x in estafetas:
        for y in x.servicos:
            if (time_start <= y.hora_de_entrega <= time_end):
                rendimento = rendimento + y.dinheiro
            continue
        continue
    return rendimento

def query5(estafetas):
    lista_de_ruas = []
    for x in estafetas:
        for y in x.servicos:
            lista_de_ruas.append(y.rua)
            continue
        continue
    return most_frequent(lista_de_ruas)
    

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


def query6(estafeta):
    return estafeta.classificacao

def query7(time_start, time_end, estafetas):
    entregas_por_veículo = []
    carros = 0
    motas = 0
    bicicletas = 0
    for x in estafetas:
        for y in x.servicos:
            if (time_start <= y.hora_de_entrega <= time_end):
                if (y.transporte == "carro" ): 
                    carros = carros + 1
                elif (y.transporte == "mota"):
                    motas = motas + 1
                else:
                    bicicletas = bicicletas + 1
            continue
        continue
    entregas_por_veículo.append(("carro",carros))
    entregas_por_veículo.append(("mota",motas))
    entregas_por_veículo.append(("bicicleta",bicicletas))
    return entregas_por_veículo

def query8(time_start, time_end, estafetas):
    estafeta_e_encomendas = []
    nEntregas = 0
    for x in estafetas:
        for y in x.servicos:
            if (time_start <= y.hora_de_entrega <= time_end):
                nEntregas = nEntregas + 1
            continue
        estafeta_e_encomendas.append((x.nome,nEntregas))
        continue
    return estafeta_e_encomendas

def query9(time_start, time_end, estafetas):
    nEncomendasEntregues = 0
    nNãoEncomendasEntregues = 0
    entregues_e_nao = (0,0)
    for x in estafetas:
        for y in x.servicos:
            if (time_start <= y.hora_de_entrega <= time_end):
                if (y.classificacao > 0):
                    nEncomendasEntregues = nEncomendasEntregues + 1
                else:
                    nNãoEncomendasEntregues = nNãoEncomendasEntregues + 1
            continue
        continue
    entregues_e_nao = (nEncomendasEntregues,nNãoEncomendasEntregues)
    return entregues_e_nao
        
def query10(estafetas,day):
    time_start = datetime.combine(day,time.min)
    time_end = datetime.combine(day,time.max)
    peso_por_estafeta = []
    peso = 0
    for x in estafetas:
        for y in x.encomendas:
            if (time_start <= y.hora_de_entrega <= time_end):
                peso = peso + y.peso
            continue
        peso_por_estafeta.append((x,peso))
        continue
    return peso_por_estafeta