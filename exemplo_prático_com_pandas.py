#10-Exemplo Prático com Pandas

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df_completo = pd.read_csv("covid19_casos_brasil.csv")
cols = ['city', 'date', 'last_available_confirmed', 'last_available_deaths']
# print(df_completo.head()[cols])

filtro_cidade_DV = df_completo['city'] == 'Dois Vizinhos'
df_DV = df_completo[filtro_cidade_DV]
print(df_DV.tail()[cols])

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# df_DV.plot('date', ['last_available_confirmed', 'last_available_deaths'])