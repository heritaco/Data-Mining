import pickle
import os
import numpy as np


def unpickle(file_path):
    """Carga un archivo pickle de Python y devuelve el diccionario."""
    with open(file_path, 'rb') as fo:
        return pickle.load(fo, encoding='bytes')



def clases_cifar(cifar100_path, clases):
    """
    Carga los datos de CIFAR-100 y filtra por las clases seleccionadas.
    Args:
        cifar100_path (str): Ruta al directorio de CIFAR-100.
        clases (list): Lista de nombres de clases a filtrar.
    Returns:
        X (numpy.ndarray): Datos de las clases seleccionadas.
        y (numpy.ndarray): Etiquetas de las clases seleccionadas.
        fine_label_names (list): Nombres de todas las clases.
    """
    # Carga de los datos de entrenamiento y metadatos
    data_dict = unpickle(os.path.join(cifar100_path, 'data_batch_1'))   # Diccionario de datos
    meta_dict  = unpickle(os.path.join(cifar100_path, 'batches.meta'))  # Diccionario de metadatos

    # Decodificar nombres de clases
    fine_label_names = [name.decode('utf-8') for name in meta_dict[b'label_names']]

    # Obtener índices de las clases seleccionadas
    idx_clases = [fine_label_names.index(clase) for clase in clases]

    # Convertir datos y etiquetas a numpy
    data = data_dict[b'data']
    labels = np.array(data_dict[b'labels']) 

    # Filtrar datos y etiquetas para las clases seleccionadas
    mask = np.isin(labels, idx_clases)     # conseguir una mascara booleana
    X = data[mask]                         # datos de las clases seleccionadas (n_samples, n_features)
    y = labels[mask]                       # etiquetas de las clases seleccionadas (n_samples, )

    return X, y, fine_label_names, idx_clases