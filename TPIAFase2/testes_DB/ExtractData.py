# importing the module
import pandas as pd
  
#lê apenas as colunas desejadas da Data Frame
df = pd.read_csv("/home/arkimedez/Desktop/IA/TPIAFase2/DCC_DublincityRoadsandStreets.csv", usecols = ['street_name','Subarea','line_length','road_start','road_finish'])
#retira qualquer linha que não tenha informação
df = df.dropna()
#retira qualquer linha totalmente repetida
df = df.drop_duplicates()
#retira qualquer linha com nome da rua repetido
df.drop_duplicates(subset=['street_name'])
#retira qualquer linha que tenha a distância igual a 0
df.drop(df.index[df['line_length'] == 0], inplace = True)
#rearranjar a ordem para se poder criar o grafo mais facilmente
cols = ['road_start','road_finish','line_length','street_name','Subarea']
df = df[cols]
print(cols)



print(df)

df.to_csv(r'/home/arkimedez/Desktop/IA/TPIAFase2/DublinRoadsandStreetsFinal.csv')


