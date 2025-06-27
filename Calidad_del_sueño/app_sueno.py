import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo previamente entrenado
modelo = joblib.load("modelo_sueno.pkl")

st.title("🌙 Predicción de Calidad del Sueño")
st.write("Introduce los datos para predecir tu calidad de sueño basada en tu estilo de vida.")

# Formulario interactivo
edad = st.slider("Edad", 18, 100, 35)
pasos = st.number_input("Pasos diarios", min_value=0, value=6000)
calorias = st.number_input("Calorías quemadas", min_value=0, value=2000)
horas_sueno = st.slider("Horas de sueño", 0.0, 12.0, 7.0)

genero = st.selectbox("Género", ["Femenino", "Masculino"])
actividad = st.selectbox("Nivel de actividad física", ["Bajo", "Medio", "Alto"])
habitos = st.selectbox("Hábitos alimentarios", ["Pobres", "Regulares", "Saludables"])
trastornos = st.selectbox("¿Tiene trastornos del sueño?", ["No", "Sí"])
medicacion = st.selectbox("¿Usa medicación para dormir?", ["No", "Sí"])

# Variables codificadas como en el modelo original
genero_m = 1 if genero == "Masculino" else 0
actividad_medium = 1 if actividad == "Medio" else 0
actividad_high = 1 if actividad == "Alto" else 0
habitos_regulares = 1 if habitos == "Regulares" else 0
habitos_saludables = 1 if habitos == "Saludables" else 0
trastornos_yes = 1 if trastornos == "Sí" else 0
medicacion_yes = 1 if medicacion == "Sí" else 0

# Crear DataFrame para la predicción
nuevos_datos = pd.DataFrame({
    "Age": [edad],
    "Daily_Steps": [pasos],
    "Calories_Burned": [calorias],
    "SleepDuration_Hours": [horas_sueno],
    "Gender_m": [genero_m],
    "Physical_Activity_Level_medium": [actividad_medium],
    "Physical_Activity_Level_high": [actividad_high],
    "Dietary_Habits_regular": [habitos_regulares],
    "Dietary_Habits_healthy": [habitos_saludables],
    "Sleep_Disorders_yes": [trastornos_yes],
    "Medication_Usage_yes": [medicacion_yes]
})
# Asegurar que el DataFrame tiene todas las columnas que el modelo espera
columnas_esperadas = [
    'Age',
    'Daily_Steps',
    'Calories_Burned',
    'SleepDuration_Hours',
    'Gender_m',
    'Physical_Activity_Level_low',
    'Physical_Activity_Level_medium',
    'Dietary_Habits_medium',
    'Dietary_Habits_unhealthy',
    'Sleep_Disorders_yes',
    'Medication_Usage_yes'
]

for col in columnas_esperadas:
    if col not in nuevos_datos.columns:
        nuevos_datos[col] = 0

# Reordenar columnas para que coincidan con el orden del entrenamiento
nuevos_datos = nuevos_datos[columnas_esperadas]

# Botón de predicción
if st.button("🧠 Predecir calidad del sueño"):
    resultado = modelo.predict(nuevos_datos)[0]
    if resultado == 1:
        st.success("🌙 Calidad del sueño estimada: BUENA 😴💤")
    else:
        st.warning("⚠️ Calidad del sueño estimada: MEJORABLE — podrías revisar tus hábitos.")
