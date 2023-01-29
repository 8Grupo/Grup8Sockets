import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Grup8Sockets")
st.header('Infraestructura II - Grupo 8')
st.subheader('Objetivo 8:')
st.subheader('Generar nuevas oportunidades y bienestar para las zonas rurales, con énfasis en pueblos y nacionalidades.')
st.subheader('Meta 8.2.2:')
st.subheader('Incrementar la tasa bruta de matrícula de bachillerato en el área rural de 48,65% al 54,91%.')

###cargar los datos en sitio web####
excel_file = ('C:\\Users\\jonas\\OneDrive\\Documentos\\DatosExtraidos\\resumen.xlsx')


df = pd.read_excel(excel_file,
                   usecols='A:D',
                   header=0,
                   )

st.dataframe(df)

#grafico Pastel
pie_chart = px.pie(df,
                    title='',
                    values='TOTAL ESTUDIANTES BACHILLERATO',
                    names='PERIODO')

st.plotly_chart(pie_chart)
