import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title = "Previsao de renda",
     page_icon = "💵",
     layout = "wide",
)

st.write('# Análise exploratória da previsão de renda')

renda = pd.read_csv('./input/previsao_de_renda.csv')

max_renda = int(renda.renda.max())+1
min_renda = int(renda.renda.min())-1
faixa_renda= st.sidebar.slider(label='Filtrar pela faixa de renda', 
                                        min_value = min_renda,
                                        max_value = max_renda, 
                                        value = (min_renda, max_renda),
                                        step = 1000)
st.sidebar.write('Renda Mínima: ', faixa_renda[0]) 
st.sidebar.write('Renda Máxima: ', faixa_renda[1]) 
renda = renda.query("renda >= @faixa_renda[0] and renda <= @faixa_renda[1]")


#plots
fig, ax = plt.subplots(8,1,figsize=(10,70))
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])
st.write('## Gráficos ao longo do tempo')
sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel',data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='posse_de_veiculo',data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='qtd_filhos',data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_renda',data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='educacao',data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='estado_civil',data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)
sns.lineplot(x='data_ref',y='renda', hue='tipo_residencia',data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)
sns.despine()
st.pyplot(plt)

st.write('## Gráficos bivariada')
fig, ax = plt.subplots(7,1,figsize=(10,50))
sns.barplot(x='sexo',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_imovel',y='renda',data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo',y='renda',data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos',y='renda',data=renda, ax=ax[2])
sns.barplot(x='tipo_renda',y='renda',data=renda, ax=ax[3])
sns.barplot(x='educacao',y='renda',data=renda, ax=ax[4])
sns.barplot(x='estado_civil',y='renda',data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia',y='renda',data=renda, ax=ax[6])
sns.despine()
st.pyplot(plt)





