import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.title("Dashboard de Anuncios de Coches")
st.write("""
Bienvenido al dashboard interactivo. Aquí puedes explorar los datos de anuncios de coches
filtrando por año, tipo y condición, y visualizar histogramas y gráficos de dispersión.
""")

# -----------------------
# Filtros interactivos
# -----------------------
st.sidebar.header("Filtros")

selected_year = st.sidebar.multiselect(
    "Selecciona el año del coche",
    options=sorted(car_data['model_year'].dropna().unique()),
    default=sorted(car_data['model_year'].dropna().unique())
)

selected_type = st.sidebar.multiselect(
    "Selecciona el tipo de carro",
    options=car_data['type'].dropna().unique(),
    default=car_data['type'].dropna().unique()
)

selected_condition = st.sidebar.multiselect(
    "Selecciona la condición",
    options=car_data['condition'].dropna().unique(),
    default=car_data['condition'].dropna().unique()
)

# Filtrar datos según selección
filtered_data = car_data[
    (car_data['model_year'].isin(selected_year)) &
    (car_data['type'].isin(selected_type)) &
    (car_data['condition'].isin(selected_condition))
]

st.write(f"Mostrando {len(filtered_data)} registros filtrados.")

# -----------------------
# Gráficos con checkboxes
# -----------------------
st.subheader("Visualizaciones")

if st.checkbox('Mostrar Histograma del odómetro'):
    st.write('Histograma del odómetro de los coches filtrados')
    fig_hist = px.histogram(
        filtered_data,
        x="odometer",
        nbins=30,
        title="Histograma del Odómetro",
        labels={"odometer": "Kilometraje"}
    )
    st.plotly_chart(fig_hist, use_container_width=True)

if st.checkbox('Mostrar Gráfico de Dispersión (Precio vs Odómetro)'):
    st.write('Gráfico de dispersión del precio vs odómetro')
    fig_scatter = px.scatter(
        filtered_data,
        x="odometer",
        y="price",
        color="type",
        hover_data=["model", "model_year"],
        title="Precio vs Odómetro",
        labels={"odometer": "Kilometraje", "price": "Precio"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)