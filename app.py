import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv(
    r'C:\Users\jhernandezp\Documents\CURSO_DA_TRIPLETEN\CURSO_TRIPLETEN\SPRINT7\vehicles_env\vehicles_us.csv')

st.header('Anuncios para ventas de coches')

st.write(
    'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

hist_button = st.button('Construir histograma')

if hist_button:

    fig_hist = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig_hist, use_container_width=True)

st.write(
    'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

scatter_button = st.button('Construir un gráfico de dispersión')

if scatter_button:

    fig_sctr = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig_sctr, use_container_width=True)
