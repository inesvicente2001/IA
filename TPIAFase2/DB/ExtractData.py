# importing the module
import pandas as pd
import random


freguesias = ["Agrela","Água Longa","Monte Córdova","Rebordões","Reguenga","Roriz","S.Tomé Negrelos","Areias","Sequeirô","Lama","Palmeira",
"Lamelas","Guimarei","S. Tiago da Carreira","Refojos","Riba de Ave",
"Santo Tirso", "Couto (S. Cristina e S. Miguel)","Burgães",
"Vila das Aves","Vila Nova do Campo","Vilarinho"]

ruas = pd.read_csv("/home/arkimedez/Desktop/IA/TPIAFase2/testes_DB/SantoTirsoStreets.csv")

print(ruas)
freguesia = []

for x in range(len(ruas)):
   freguesia.append(freguesias[random.randint(0,len(freguesias)-1)])
  

ruas = ruas.drop_duplicates()

ruas['freguesia'] = freguesia

ruas = ruas.sort_values('freguesia')



print(ruas)



ruas.to_csv(r'/home/arkimedez/Desktop/IA/TPIAFase2/testes_DB/SantoTirsoStreetsFinal.csv')


