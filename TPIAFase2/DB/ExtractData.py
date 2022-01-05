# importing the module
import pandas as pd
import random
import numpy as np
from operator import itemgetter


freguesias = ["Agrela","Água Longa","Monte Córdova","Rebordões","Reguenga","Roriz","S.Tomé Negrelos","Areias","Sequeirô","Lama","Palmeira",
"Lamelas","Guimarei","S. Tiago da Carreira","Refojos","Riba de Ave",
"Santo Tirso", "Couto (S. Cristina e S. Miguel)","Burgães",
"Vila das Aves","Vila Nova do Campo","Vilarinho"]

ruas = pd.read_csv("DB/SantoTirsoStreets.csv")

greenDistribution = {'rua': 'Green Distribution'}

ruas = ruas.append(greenDistribution, ignore_index = True)

print(ruas)

freguesia = []

for x in range(len(ruas)):
   freguesia.append(freguesias[random.randint(0,len(freguesias)-1)])
  

ruas = ruas.drop_duplicates()
ruas['freguesia'] = freguesia
#ruas = ruas.sort_values('freguesia')


ruas_lst = ruas['rua'].tolist()

coordenadas_lst = []
arestas = []
distancias = []

for a in range(len(ruas_lst)):
   coord_x = 20
   coord_y = 20

   while (coord_x,coord_y) in coordenadas_lst:
      coord_x = random.randint(1,200)
      coord_y = random.randint(1,200)


   coordenadas_lst.append((coord_x,coord_y))
   conects = random.randint(1,4)
   for y in range(conects):
      num = a
      while (num == a):
         num = random.randint(0,len(ruas_lst)-1)
      if not((a, num) in arestas) and not((num, a) in arestas) :
         arestas.append(tuple([a, num]))
         #distancia = random.randint(30,120)
         #distancias.append(distancia)


ruas['coordenadas'] = coordenadas_lst


from_lst = list(map(itemgetter(0), arestas))
to_lst = list(map(itemgetter(1), arestas))

for b in range(len(arestas)):
   #para todos os pares, calcular a distância euclidiana

   from_ = from_lst[b]
   to_ = to_lst[b]

   point_a = np.array(coordenadas_lst[from_lst[b]])
   point_b = np.array(coordenadas_lst[to_lst[b]])
   
   # calculating Euclidean distance
   dist = np.linalg.norm(point_a - point_b)
   distancias.append(dist)



#print(arestas)





data = {'Arestas': arestas, 'Distancias': distancias}
#data = {'Arestas': arestas}  

#print(data)
  
conexoes = pd.DataFrame(data)  

#print(ruas)
#print(conexoes)


ruas.to_csv(r'DB/SantoTirsoStreets.csv')
conexoes.to_csv(r'DB/ConexoesRuas.csv')


