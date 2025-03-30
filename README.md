# ML_WineQuality

Este proyecto tiene como objetivo predecir la calidad de los vinos (tinto y blanco) a partir de características físico-químicas. Para ello, utilizamos técnicas de Machine Learning para abordar el problema como **regresión** o **clasificación**, dependiendo de cómo definamos las clases de calidad del vino.

## Dataset

El dataset utilizado es el **Wine Quality Dataset**. Contiene información sobre características físico-químicas de los vinos y la calidad evaluada por expertos. Este dataset está disponible públicamente en el [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality).

### Descripción del dataset:
- El dataset incluye dos versiones: vino tinto y vino blanco.
- Las características incluyen datos como la acidez, el pH, el alcohol, el azúcar residual, entre otros.
- La calidad del vino es una variable numérica entre 0 y 10.

## Solución Adoptada

Se abordará el problema utilizando un enfoque de **Machine Learning supervisado**. Se probarán varios modelos de regresión y clasificación para predecir la calidad del vino y se evaluarán según su precisión y rendimiento.

## Estructura de Directorios

```plaintext
ML_WineQuality/
├── data/                  # Directorio para almacenar el dataset (archivos CSV).
├── notebooks/             # Jupyter notebooks para el análisis y modelado.
├── src/                   # Código fuente para preprocesamiento, modelos, etc.
├── README.md              # Este archivo con la descripción del proyecto.
