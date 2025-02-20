import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis de Anuncios de Venta de Coches")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para mostrar un histograma
if st.button('Mostrar Histograma'):
    st.write("Histograma del Odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para mostrar un gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión'):
    st.write("Relación entre el precio y el odómetro")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)