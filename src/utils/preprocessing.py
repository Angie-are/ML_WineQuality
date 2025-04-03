#!/usr/bin/env python
# coding: utf-8

# In[16]:

# src/utils/preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Función para cargar los datos
def load_data(file_path):
    return pd.read_csv(file_path, delimiter=';')

# Función para verificar los valores nulos en los datos
def check_missing_values(data):
    return data.isnull().sum()

# Función para dividir en características y etiquetas
def split_data(data):
    X = data.drop('quality', axis=1)
    y = data['quality']
    return X, y

# Función para crear un pipeline de preprocesamiento
def create_pipeline():
    return Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),  # Imputación de valores faltantes con la media
        ('scaler', StandardScaler())  # Normalización de las características
    ])

# Función para preprocesar los datos
def preprocess_data(X_train, X_test, pipeline):
    X_train = pipeline.fit_transform(X_train)
    X_test = pipeline.transform(X_test)
    return X_train, X_test

# Función para dividir los datos en conjuntos de entrenamiento y prueba
def train_test_split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
