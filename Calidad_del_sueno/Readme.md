💤 Predicción de la Calidad del Sueño
Este proyecto es una aplicación desarrollada en Python que permite predecir la calidad del sueño de una persona en función de distintos factores relacionados con su estilo de vida y salud. Utiliza modelos de inteligencia artificial entrenados con datos reales para generar una predicción automática e intuitiva.

🎯 Objetivo
El objetivo principal es ofrecer una herramienta sencilla que ayude a los usuarios a conocer si su calidad de sueño es adecuada o deficiente, basándose en variables como:

Horas de sueño

Nivel de actividad física

Consumo de cafeína

Nivel de estrés

Frecuencia cardíaca

Edad y género, entre otros

🧠 Tecnología utilizada
Python

Pandas / Numpy (tratamiento de datos)

Scikit-learn (entrenamiento del modelo)

Pickle (para guardar y cargar el modelo)

Streamlit o Flask (para interfaz web, si corresponde)

Jupyter Notebook (para exploración y análisis)

⚙️ Funcionamiento
Se carga un modelo previamente entrenado (modelo_sueno.pkl).

El usuario introduce datos sobre su día a día a través de una interfaz simple.

La aplicación procesa los datos y devuelve una predicción de calidad de sueño: "Buena" o "Mala".

📁 Estructura del proyecto
bash
Copiar
Editar
📁 Calidad_del_sueno/
│
├── Calidad_del_sueno.ipynb       # Análisis y entrenamiento del modelo
├── app_sueno.py                  # Aplicación en Python (interfaz)
├── modelo_sueno.pkl              # Modelo entrenado (ignorado en GitHub)
├── .gitignore                    # Archivos que no se suben al repositorio
├── /Health and Sleep stadistics # Dataset usado
🚫 Notas
El archivo del modelo (modelo_sueno.pkl) no está subido a GitHub por superar el límite de tamaño. Puedes descargarlo desde aquí (añade el enlace si lo subes a Drive u otro sitio).

El proyecto está pensado como una herramienta educativa y no sustituye a una evaluación médica.

🙋‍♀️ Autora
Este proyecto ha sido desarrollado por Monibr3, como parte de su formación en inteligencia artificial aplicada con Python.

¿Quieres que te lo prepare ya en archivo .md para que lo subas directamente? También te puedo añadir una sección con instrucciones para ejecutarlo si usas Streamlit o Flask.

**https://drive.google.com/drive/folders/1TheXFLxmMAEX2EYKFfS9nM_hlYud5OTt?usp=drive_link**
