# Proyecto: **Predicción de la Calidad del Vino con Machine Learning**

## Descripción del Proyecto
Este proyecto tiene como objetivo predecir la calidad de los vinos (tintos y blancos) utilizando modelos de Machine Learning. El dataset utilizado contiene características químicas de los vinos, como acidez, azúcar residual, pH y alcohol, entre otros, y la tarea es predecir la calidad del vino (en una escala de 0 a 10) a partir de esas características.

## Dataset
Se ha utilizado el conjunto de datos **Wine Quality Dataset**, disponible públicamente en [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality). El dataset consta de dos partes: vinos tintos y vinos blancos, con 11 características y una etiqueta de calidad.

## Solución Adoptada
El proyecto empleó modelos de Machine Learning supervisado para la predicción de la calidad del vino. Se probaron varios algoritmos de clasificación, entre los que destacan:
- **Árboles de decisión** (XGBoost)
- **Máquinas de soporte vectorial** (SVM)
- **Perceptrón multicapa** (MLP)

Los pasos realizados en el proyecto fueron:
1. **Preprocesamiento de los datos**: Se realizó la limpieza de datos y normalización de las características.
2. **Entrenamiento de modelos**: Se entrenaron modelos de clasificación usando los conjuntos de entrenamiento.
3. **Evaluación de los modelos**: Se evaluaron los modelos con métricas como la precisión y el recall.
4. **Guardado del modelo entrenado**: El modelo final fue guardado en formato `.pkl` para su reutilización.

## Estructura de Directorios

## Notebooks
El proyecto incluye varios notebooks:
- **EDA_notebook.ipynb**: Análisis exploratorio de los datos.
- **Model_training_notebook.ipynb**: Entrenamiento de un modelo básico.
- **Model_training2xgb.ipynb**: Entrenamiento de un modelo usando XGBoost.
- **Model_training3.SVM.ipynb**: Entrenamiento de un modelo usando SVM.
- **Model_training4.MLP.ipynb**: Entrenamiento de un modelo usando un perceptrón multicapa.
- **Preprocessing_notebook.ipynb**: Preprocesamiento de los datos (limpieza y normalización).

## Modelos
- El modelo entrenado final está guardado en formato **.pkl** dentro de la carpeta `src/models`.

# Project: **Wine Quality Prediction with Machine Learning**

## Project Description
The goal of this project is to predict the quality of wines (red and white) using Machine Learning models. The dataset contains chemical characteristics of wines, such as acidity, residual sugar, pH, and alcohol, among others. The task is to predict the wine quality (on a scale from 0 to 10) from these features.

## Dataset
The **Wine Quality Dataset** was used, which is publicly available at the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality). The dataset consists of two parts: red wines and white wines, with 11 features and a quality label.

## Adopted Solution
The project used supervised Machine Learning models for wine quality prediction. Several classification algorithms were tested, including:
- **Decision Trees** (XGBoost)
- **Support Vector Machines** (SVM)
- **Multilayer Perceptron** (MLP)

The steps taken in the project were:
1. **Data Preprocessing**: Data cleaning and feature normalization.
2. **Model Training**: Classification models were trained using training sets.
3. **Model Evaluation**: Models were evaluated with metrics such as accuracy and recall.
4. **Model Saving**: The final trained model was saved in `.pkl` format for reuse.

## Directory Structure

## Notebooks
The project includes several notebooks:
- **EDA_notebook.ipynb**: Exploratory Data Analysis.
- **Model_training_notebook.ipynb**: Basic model training.
- **Model_training2xgb.ipynb**: Training a model using XGBoost.
- **Model_training3.SVM.ipynb**: Training a model using SVM.
- **Model_training4.MLP.ipynb**: Training a model using a multilayer perceptron.
- **Preprocessing_notebook.ipynb**: Data preprocessing (cleaning and normalization).

## Models
- The final trained model is saved in **.pkl** format in the `src/models` folder.
