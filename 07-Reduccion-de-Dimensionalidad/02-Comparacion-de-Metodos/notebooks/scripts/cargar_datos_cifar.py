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

    return X, y, fine_label_names, data_dict, meta_dict


import random
from pathlib import Path
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')  # Importante: encoding='bytes' para Python 3
    return dict

def i_want_to_see_a_(img, data_dict, meta_dict):

    # Definimos la ruta de los datos y resultados
    path_resultados = Path("../resultados")
    
    # Extraer las labels
    label_names = [label.decode('utf-8') for label in meta_dict[b'label_names']]
    
    # Encuentra todos los índices con la etiqueta deseada
    label_idx = label_names.index(img)
    indices = [i for i, l in enumerate(data_dict[b'labels']) if l == label_idx]

    # Selecciona uno al azar
    img_index = random.choice(indices)

    # Consigue la imagen y su etiqueta
    img_flat = data_dict[b'data'][img_index]
    label = data_dict[b'labels'][img_index]

    # Convertir a imagen 32x32x3
    img_R = img_flat[0:1024].reshape(32, 32)
    img_G = img_flat[1024:2048].reshape(32, 32)
    img_B = img_flat[2048:].reshape(32, 32)
    img = np.stack([img_R, img_G, img_B], axis=2)

    # Mostrar la imagen
    plt.imshow(img.astype(np.uint8))
    plt.title(f"{label_names[label]}")
    plt.axis('off')
    
    # Define tu nombre de archivo (usa por ejemplo: label_names[label] = 'grafico_1')
    nombre_archivo = f"{label_names[label]}_{img_index}.svg"
    plt.savefig(path_resultados / nombre_archivo, bbox_inches='tight')
    plt.show()