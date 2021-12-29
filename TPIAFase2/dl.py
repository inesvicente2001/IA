from enum import Enum

class Cliente:
    def __init__(self, nome): 
        self.nome = nome

class Transporte(Enum):
    Carro = 0
    Mota = 1
    Bicicleta = 2

class Localizacao:
    def __init__(self, rua, freguesia): 
        self.rua = rua 
        self.freguesia = freguesia

    
#N sei se vamos ter uma encomenda a ter um id para não haver repetidos
class Encomenda:
    def __init__(self, nome, peso, volume, transporte, prazo, cliente, ponto_chegada, classificacao): 
        self.nome = nome 
        self.peso = peso
        self.volume = volume
        self.Transporte = transporte
        self.prazo = prazo
        self.Cliente = cliente
        self.Localizacao = ponto_chegada
        self.classificacao = classificacao  #n sei se isto fica aqui
    
class Estafeta:
    nome: str 
    classificacao: float #media das classificações dada pelos clientes
    encomendas: list[Encomenda]
 
#Exemplo para criar uma encomenda   
c = Cliente("joao")
l = Localizacao("Barros", "Gualtar")
e = Encomenda("ola", 21, 21, Transporte.Carro, 21, c, l, 3)
#print(e)
    
    
    