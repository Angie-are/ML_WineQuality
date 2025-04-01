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

# ML_WineQuality - Wine Quality Prediction

## Project Overview

This project aims to predict the quality of wine based on various chemical properties like acidity, alcohol content, etc. The dataset used for this project is the **Wine Quality** dataset, which consists of both red and white wine data.

## Dataset

The dataset contains 12 features (e.g., alcohol, acidity, residual sugar) and a quality rating between 0 and 10. The datasets can be accessed from [UCI Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality).

## Solution

We are building a **Random Forest Regressor** model to predict wine quality for both red and white wines.

## Project Structure

- `/src/data_sample`: Contains a small sample of the wine dataset (to ensure reproducibility).
- `/src/notebooks`: Contains exploratory data analysis (EDA) and preprocessing steps.
- `/src/results_notebook`: Contains the final notebook with the step-by-step process.
- `/src/models`: Contains the saved trained models (`model_white_wine.pkl`, `model_red_wine.pkl`).
- `/src/utils`: Contains utility functions or custom classes (if any).

## Steps Followed

1. **Exploratory Data Analysis (EDA)** - Analyzing the dataset's characteristics and distributions.
2. **Data Preprocessing** - Splitting the data into train-test sets and normalizing the features.
3. **Model Training** - Using a Random Forest Regressor to train models for both red and white wine.
4. **Model Evaluation** - Evaluating the models using MSE and R² scores.
5. **Model Saving** - Saving the trained models using joblib.
