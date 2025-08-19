import pandas as pd
import plotly_express as px
import streamlit as st


# El proyecto consite en desplegar los datos de la tabla vehicles.cvs en una página de internet, experimentar con los datos e implementar
# gráficos


car_data = pd.read_csv(
    r'C:\Users\jhernandezp\Documents\CURSO_DA_TRIPLETEN\CURSO_TRIPLETEN\SPRINT7\vehicles_env\vehicles_us.csv')

# El título se pone en negritas, aprovechar el espacio de la página
st.header('**Anuncios para ventas de coches**')


st.write(
    """
Creación de gráficos para el módelo de datos *vehicles_usa*, el cual muestra la cantidad de anuncios disponibles para la venta de
coches, para una compañia determinada 
"""

)  # como se implemetaron columnas, se cambió la descripción de la página para que quedara debajo del header y no en cada columna

col1, col2 = st.columns(2)

with col1:

    # valores en falso para que no aparezcan default
    ver_hist = st.checkbox('Construir **histograma**', value=False)

    if ver_hist:

        fig_hist = px.histogram(car_data, x="odometer")

        st.plotly_chart(fig_hist, use_container_width=True)

with col2:

    # valores en falso para que no aparezcan default
    ver_sctr = st.checkbox('Construir **gráfico de dispersión**', value=False)

    if ver_sctr:

        fig_sctr = px.scatter(car_data, x="odometer", y="price")

        st.plotly_chart(fig_sctr, use_container_width=True)
