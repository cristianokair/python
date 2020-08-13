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


# código da atividade em grupo
df_completo = pd.read_csv("covid19_casos_brasil.csv")
df_completo.head()

colsConfirmados = ['city', 'date', 'last_available_confirmed', 'new_confirmed']
colsMortes = ['city', 'date', 'last_available_deaths', 'new_deaths']
cidades = ['Joinville', 'Francisco Beltrão', 'Dois Vizinhos', 'Pato Branco', 'Florianópolis']
frames = list()
for c in cidades:
    frames.append(df_completo[df_completo['city'] == c])
df = pd.concat(frames)
df[colsConfirmados]

df_confirmados = df[colsConfirmados]
df_mortes = df[colsMortes]

df_confirmados.head()

df_mortes.head()

filtro_cidades = (df_completo['city'] == 'Joinville') | (df_completo['city'] == 'Francisco Beltrão') | (df_completo['city'] == 'Dois Vizinhos') | (df_completo['city'] == 'Pato Branco') | (df_completo['city'] == 'Florianópolis')
df_DV = df_completo[filtro_cidades]
df_DV.tail()[colsConfirmados]

filtro_J = (df_completo['city'] == 'Dois Vizinhos') & (df_completo['date'] == '2020-07-10')
df_J = df_completo[filtro_J]
df_J[colsConfirmados]

for i in cidades:
    df_J = df_confirmados[df_completo['city'] == i]
    plt.plot(df_J.date, df_J.last_available_confirmed)

plt.show()

for i in cidades:
    filtro = df_completo['city'] == i
    df_J = df_confirmados[filtro]
    plt.plot(df_J.date, df_J.new_confirmed)

plt.show()