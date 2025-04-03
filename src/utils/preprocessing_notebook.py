#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Importar librerías necesarias
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import pandas as pd


# In[17]:


red_wine = pd.read_csv(r'C:\Users\angel\OneDrive\Documentos\DATA_SCIENCE\Bootcamp\ML_WineQuality\data\winequality-red.csv', delimiter=';')
white_wine = pd.read_csv(r'C:\Users\angel\OneDrive\Documentos\DATA_SCIENCE\Bootcamp\ML_WineQuality\data\winequality-white.csv', delimiter=';')


# In[18]:


# Revisar si hay valores nulos en los datasets
print("\nValores nulos en el dataset de vino tinto:")
print(red_wine.isnull().sum())

print("\nValores nulos en el dataset de vino blanco:")
print(white_wine.isnull().sum())

# Si hubiera valores nulos, podemos optar por eliminar o imputar esos valores
# red_wine = red_wine.dropna()  # O bien, imputar con red_wine.fillna(0) o un valor medio/mediano
# white_wine = white_wine.dropna()  # Lo mismo para vino blanco


# In[19]:


# Verificar tipos de datos en ambos datasets
print("\nTipos de datos en el dataset de vino tinto:")
print(red_wine.dtypes)

print("\nTipos de datos en el dataset de vino blanco:")
print(white_wine.dtypes)


# In[20]:


# Dividir el dataset en características (X) y etiquetas (y) para vino tinto
X_red = red_wine.drop('quality', axis=1)  # Características (features)
y_red = red_wine['quality']  # Etiquetas (target)

# Dividir el dataset en características (X) y etiquetas (y) para vino blanco
X_white = white_wine.drop('quality', axis=1)  # Características (features)
y_white = white_wine['quality']  # Etiquetas (target)

# Dividir en conjunto de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train_red, X_test_red, y_train_red, y_test_red = train_test_split(X_red, y_red, test_size=0.2, random_state=42)
X_train_white, X_test_white, y_train_white, y_test_white = train_test_split(X_white, y_white, test_size=0.2, random_state=42)

# Crear un pipeline para preprocesar los datos (imputar y escalar)
pipeline_red = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),  # Imputación de valores faltantes con la media
    ('scaler', StandardScaler())  # Normalización de las características
])

pipeline_white = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),  # Imputación de valores faltantes con la media
    ('scaler', StandardScaler())  # Normalización de las características
])

# Ajustar y transformar los datos de entrenamiento, luego transformar los de prueba
X_train_red = pipeline_red.fit_transform(X_train_red)
X_test_red = pipeline_red.transform(X_test_red)

X_train_white = pipeline_white.fit_transform(X_train_white)
X_test_white = pipeline_white.transform(X_test_white)

# Mostrar el tamaño de los conjuntos de entrenamiento y prueba
print("\nTamaño del dataset de vino tinto (entrenamiento y prueba):")
print(f"Train size: {X_train_red.shape}, Test size: {X_test_red.shape}")

print("\nTamaño del dataset de vino blanco (entrenamiento y prueba):")
print(f"Train size: {X_train_white.shape}, Test size: {X_test_white.shape}")

