# moving_average_forecasting.py
import streamlit as st
import pandas as pd
import numpy as np

# Cargar o generar datos de ejemplo
def load_data():
    data = pd.DataFrame({
        "fecha": pd.date_range(start="1/1/2023", periods=100, freq="D"),
        "ventas": np.random.randint(100, 200, size=100)
    })
    data.set_index("fecha", inplace=True)
    return data

# Función para calcular el pronóstico de promedio móvil
def moving_average_forecast(data, window_size=5):
    return data["ventas"].rolling(window=window_size).mean()

# Configuración de la interfaz con Streamlit
st.title("Pronóstico de Ventas - Promedio Móvil")
data = load_data()

st.write("Datos de ventas:")
st.line_chart(data["ventas"], width=600, height=300)

window_size = st.slider("Seleccione el tamaño de la ventana de promedio móvil:", 3, 10, 5)
forecast = moving_average_forecast(data, window_size=window_size)

st.write("Pronóstico de promedio móvil:")
st.line_chart(forecast, width=600, height=300)
