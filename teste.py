import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#retirar o Unnamed
df.drop(columns=['Unnamed: 0'], inplace = True)

#converter lat e long para numeros
list =['Lat_d', 'Long_d']
df[list] = df[list].apply(pd.to_numeric, errors = 'coerce')

#os estados não são repetidos
estados = df['NM_UF'].unique()
estadoSelecionado = st.selectbox('Qual estado selecionar?', estados)

dadosFiltrados = df[df['NM_UF'] == estadoSelecionado]

if st.checkbox('Mostrar tabela') == True:
  st.write(dadosFiltrados)

st.map(dadosFiltrados, latitude = 'Lat_d', longitude = 'Long_d')
st.bar_chart(df['NM_UF'].value_counts())
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])
