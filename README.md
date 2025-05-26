# Predicción de Calidad de Vinos con Machine Learning / Wine Quality Prediction with Machine Learning

## Descripción del proyecto / Project Description

Este proyecto utiliza técnicas de Machine Learning para predecir la calidad de vinos basada en variables físico-químicas.  
El objetivo es facilitar un método rápido y económico para estimar la calidad, evitando los métodos tradicionales costosos y lentos.  

This project uses Machine Learning techniques to predict wine quality based on physicochemical variables.  
The goal is to provide a fast and cost-effective method to estimate quality, avoiding traditional expensive and slow methods.

---

## Problema de negocio / Business Problem

La calidad del vino es clave para la satisfacción del cliente y la reputación de la bodega.  
Medir la calidad en laboratorio es costoso y requiere tiempo.  
Un modelo predictivo automático puede ayudar a predecir la calidad a partir de características químicas, agilizando el control de calidad.  

Wine quality is crucial for customer satisfaction and winery reputation.  
Measuring quality in the lab is costly and time-consuming.  
An automatic predictive model can help forecast quality based on chemical features, speeding up quality control.

---

## Problema técnico / Technical Problem

El problema se aborda como una clasificación multiclase, donde la variable objetivo es la calidad del vino, que varía entre 3 y 9.  
Se emplean modelos supervisados para clasificar cada muestra en la categoría correspondiente.  

The problem is tackled as a multiclass classification, where the target variable is wine quality, ranging from 3 to 9.  
Supervised models are used to classify each sample into the corresponding category.

---

## Dataset

- Nombre: Wine Quality / Name: Wine Quality  
- Origen: UCI Machine Learning Repository  
- Tamaño: 1599 muestras (vinos tintos) / Size: 1599 samples (red wines)  
- Variables: 11 predictoras (propiedades físico-químicas) + 1 objetivo (calidad) / Variables: 11 predictors (physicochemical properties) + 1 target (quality)

---

## Metodología / Methodology

1. **Exploración de datos (EDA):** análisis univariante, bivariante y multivariante para entender la distribución y relación de variables.  
   **Exploratory Data Analysis (EDA):** univariate, bivariate, and multivariate analysis to understand variable distributions and relationships.  

2. **Modelado:**  
   - Baseline con modelo simple (ej. Regresión Logística).  
   - Comparación de varios modelos: Random Forest, SVM, XGBoost.  

   **Modeling:**  
   - Baseline with simple model (e.g., Logistic Regression).  
   - Comparison of several models: Random Forest, SVM, XGBoost.  

3. **Validación cruzada:** para obtener métricas robustas (accuracy, F1-score macro).  
   **Cross-validation:** to obtain robust metrics (accuracy, macro F1-score).  

4. **Optimización de hiperparámetros:** búsqueda con GridSearch o RandomSearch.  
   **Hyperparameter optimization:** using GridSearch or RandomSearch.  

5. **Evaluación final:** sobre conjunto de test independiente y análisis de errores.  
   **Final evaluation:** on independent test set and error analysis.

---

## Resultados / Results

- Mejor modelo: Random Forest optimizado.  
- Métrica principal: F1-score macro ~0.60.  
- Predicciones correctas principalmente en clases medias; errores comunes entre clases adyacentes.  

- Best model: Optimized Random Forest.  
- Main metric: Macro F1-score ~0.60.  
- Correct predictions mainly in middle classes; common errors between adjacent classes.

---


## Estructura de carpetas / Folder structure
├── data/ # Datos originales / Original data
├── src/ # Código fuente y notebooks / Source code and notebooks
│ ├── results_notebook/ # Notebooks con EDA y modelado / Notebooks with EDA and modeling
│ └── ...
├── README.md # Este archivo / This file
├── requirements.txt # Dependencias / Dependencies
└── presentation/ # Soporte de presentación (PPTX y PDF) / Presentation files (PPTX and PDF) / MP4.


