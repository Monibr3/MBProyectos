# 💤 Predicción de la Calidad del Sueño

**Predicción del sueño** es una aplicación desarrollada en Python que permite estimar la **calidad del sueño** de una persona a partir de variables relacionadas con su estilo de vida, salud y hábitos diarios. Utiliza técnicas de inteligencia artificial para predecir si el descanso ha sido **bueno** o **malo**.

---

## 🎯 Objetivo

El objetivo principal de esta aplicación es proporcionar una herramienta intuitiva que ayude a los usuarios a:

- Identificar patrones que afectan a su sueño
- Prever la calidad de su descanso
- Reflexionar sobre sus hábitos diarios

---

## 🧾 Variables utilizadas

La predicción se basa en variables como:

- 🕒 **Horas de sueño**
- ❤️ **Frecuencia cardíaca**
- ☕ **Consumo de cafeína**
- 🏃 **Nivel de actividad física**
- 😰 **Nivel de estrés**
- 🎂 **Edad**
- ⚧ **Género**

---

## 🧠 Tecnología utilizada

- `Python 3`
- `pandas`, `numpy` – para manejo de datos
- `scikit-learn` – para el entrenamiento del modelo
- `pickle` – para guardar y cargar el modelo
- `matplotlib`, `seaborn` – para visualización (en el notebook)
- `Streamlit`(despliegue final) 

---

## ⚙️ Funcionamiento

1. El usuario introduce datos personales en una interfaz sencilla.
2. El modelo entrenado (`modelo_sueno.pkl`) procesa estos datos.
3. Se devuelve una predicción:  
   ✅ **Sueño de buena calidad**  
   ❌ **Sueño de mala calidad**

---

## 📁 Estructura del proyecto

📦 Calidad_del_sueno/
│
├── Calidad_del_sueno.ipynb # Notebook de análisis y entrenamiento
├── app_sueno.py # Código principal de la app
├── modelo_sueno.pkl # Modelo guardado (no subido a GitHub)
├── app_sueno.spec # Archivo de configuración para empaquetado
├── /Health and Sleep stadistics # Carpeta con el dataset CSV
├── /build, /dist # Carpetas generadas por PyInstaller


yaml
Copiar
Editar

---

## 🚫 Nota sobre el modelo

El archivo del modelo `modelo_sueno.pkl` **no se encuentra en este repositorio** porque supera el límite de tamaño de GitHub.  
Puedes descargarlo desde este enlace externo:  
🔗 [Enlace al modelo en Google Drive (pendiente)](#)
El proyecto está pensado como una herramienta educativa y no sustituye a una evaluación médica.

🙋‍♀️ Autora
Este proyecto ha sido desarrollado por Monibr3, como parte de su formación en inteligencia artificial aplicada con Python.

