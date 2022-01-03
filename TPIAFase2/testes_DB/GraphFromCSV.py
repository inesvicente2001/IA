from enum import Enum
import igraph
from igraph import *

import pandas as pd


  
#lê apenas as colunas desejadas da Data Frame
df = pd.read_csv("/home/arkimedez/Desktop/IA/TPIAFase2/DublinRoadsandStreetsFinal.csv", usecols = ['street_name','Subarea','line_length','road_start','road_finish'])

#print(df)
graph = igraph.Graph.DataFrame(df)


##ainda tenho de ver se o grafo ficou com toda a informação

##plot(graph)