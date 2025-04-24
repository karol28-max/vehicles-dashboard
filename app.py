import pandas as pd
import plotly.express as px
import streamlit as st

# Carga de datos
car_data = pd.read_csv('vehicles_us.csv')

# Título
st.header('📊 Análisis de anuncios de autos en EE.UU.')

# Histograma
if st.button('Mostrar histograma de odómetro'):
    st.subheader('Histograma de lecturas del odómetro')
    fig1 = px.histogram(car_data, x='odometer', nbins=30, title='Distribución de odómetro')
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico de dispersión
if st.button('Mostrar gráfico de dispersión precio vs odómetro'):
    st.subheader('Gráfico de dispersión entre precio y odómetro')
    fig2 = px.scatter(car_data, x='odometer', y='price', title='Precio vs Odómetro')
    st.plotly_chart(fig2, use_container_width=True)

import subprocess
import sys

# Verificar las dependencias instaladas
subprocess.check_call([sys.executable, "-m", "pip", "list"])

import pandas as pd
import plotly.express as px
import streamlit as st
