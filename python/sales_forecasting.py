# sales_forecasting.py
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import load_model

# Cargar o generar datos de ejemplo
def load_data():
    data = pd.DataFrame({
        "fecha": pd.date_range(start="1/1/2020", periods=100, freq="D"),
        "ventas": np.random.randint(100, 200, size=100)
    })
    data.set_index("fecha", inplace=True)
    return data

# Preprocesar datos para el modelo
def preprocess_data(data, look_back=3):
    X, Y = [], []
    dataset = data["ventas"].values
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back)]
        X.append(a)
        Y.append(dataset[i + look_back])
    return np.array(X), np.array(Y)

# Crear modelo LSTM
def create_model():
    model = Sequential()
    model.add(LSTM(50, input_shape=(3, 1)))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error", optimizer="adam")
    return model

# Configuración de la interfaz con Streamlit
st.title("Pronóstico de Ventas")
data = load_data()
st.line_chart(data["ventas"], width=600, height=300)

look_back = 3
X, Y = preprocess_data(data, look_back)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Entrenar el modelo
model = create_model()
model.fit(X, Y, epochs=10, batch_size=1, verbose=2)

# Predicciones
predictions = model.predict(X)
st.line_chart(predictions.flatten(), width=600, height=300)
