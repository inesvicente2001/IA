# importing the module
import pandas as pd
import random


freguesias = ["Agrela","Água Longa","Monte Córdova","Rebordões","Reguenga","Roriz","S.Tomé Negrelos","Areias","Sequeirô","Lama","Palmeira",
"Lamelas","Guimarei","S. Tiago da Carreira","Refojos","Riba de Ave",
"Santo Tirso", "Couto (S. Cristina e S. Miguel)","Burgães",
"Vila das Aves","Vila Nova do Campo","Vilarinho"]

ruas = pd.read_csv("/home/arkimedez/Desktop/IA/TPIAFase2/DB/SantoTirsoStreets.csv")

greenDistribution = {'rua': 'Green Distribution'}

ruas = ruas.append(greenDistribution, ignore_index = True)

print(ruas)

freguesia = []

for x in range(len(ruas)):
   freguesia.append(freguesias[random.randint(0,len(freguesias)-1)])
  

ruas = ruas.drop_duplicates()
ruas['freguesia'] = freguesia
ruas = ruas.sort_values('freguesia')


ruas_lst = ruas['rua'].tolist()


arestas = []
distancias = []

for a in range(len(ruas_lst)):
   conects = random.randint(1,4)
   for y in range(conects):
      num = a
      while (num == a):
         num = random.randint(0,len(ruas_lst))
      if not((a, num) in arestas) and not((num, a) in arestas) :
         arestas.append(tuple([a, num]))
         distancia = random.randint(30,120)
         distancias.append(distancia)



#print(arestas)


data = {'Arestas': arestas, 'Distancias': distancias}  

#print(data)
  
conexoes = pd.DataFrame(data)  

#print(ruas)
#print(conexoes)


ruas.to_csv(r'/home/arkimedez/Desktop/IA/TPIAFase2/DB/SantoTirsoStreetsFinal.csv')
conexoes.to_csv(r'/home/arkimedez/Desktop/IA/TPIAFase2/DB/ConexoesRuas.csv')


