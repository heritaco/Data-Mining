import os
import matplotlib.pyplot as plt
import umap
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid", context="notebook", palette="tab10")

def visualizar_umap(X, y, fine_label_names, epochs_to_test, neighbors_to_test, resultados_path):
    """
    Visualiza UMAP con diferentes configuraciones de n_epochs y n_neighbors.
    Args:
        X (numpy.ndarray): Datos a visualizar.
        y (numpy.ndarray): Etiquetas de los datos.
        fine_label_names (list): Nombres de las clases.
        epochs_to_test (list): Lista de valores de n_epochs a probar.
        neighbors_to_test (list): Lista de valores de n_neighbors a probar.
        resultados_path (str): Ruta para guardar los resultados.
    """

    fig, axes = plt.subplots(len(epochs_to_test), len(neighbors_to_test), figsize=(15, 15))
    fig.suptitle('Visualización UMAP con diferentes n_epochs y n_neighbors', fontsize=20, weight='bold')

    for i, n_epochs in enumerate(epochs_to_test):
        for j, n_neighbors in enumerate(neighbors_to_test):

            # Crear un pipeline con UMAP
            umap_model = umap.UMAP(
                n_components=2,
                n_neighbors=n_neighbors,
                min_dist=0.05,
                metric="euclidean",
                n_epochs=n_epochs,
                spread=1.0,
                learning_rate=1.5,
                random_state=8
            )

            # Ajustar el modelo UMAP a los datos
            X_umap_2 = umap_model.fit_transform(X)

            # Crear un DataFrame para la visualización
            df_umap = pd.DataFrame({
                'x_1': X_umap_2[:, 0],
                'x_2': X_umap_2[:, 1],
                'Clase': [fine_label_names[k] for k in y]
            })

            # Crear un gráfico de dispersión
            ax = axes[i, j]
            sns.scatterplot(
                data=df_umap,
                x='x_1',
                y='x_2',
                hue='Clase',
                alpha=0.4,
                ax=ax
            )

            # Configurar el gráfico
            ax.set_xlabel('')
            ax.set_ylabel('')
            ax.legend().set_visible(False)
            ax.grid(True)
            ax.set_xlim(-6, 10)
            ax.set_ylim(-4, 12)

    # Añadir etiquetas en los bordes para mejor claridad
    for ax, neighbors in zip(axes[0, :], neighbors_to_test):
        ax.set_title(f'n_neighbors={neighbors}', fontsize=15, weight='bold')
    for ax, epochs in zip(axes[:, 0], epochs_to_test):
        ax.set_ylabel(f'n_epochs={epochs}', fontsize=15, weight='bold')

    # Añadir una leyenda común al final
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=len(fine_label_names), fontsize=12, bbox_to_anchor=(0.5, -0.001), bbox_transform=fig.transFigure, title="Clases")


    plt.tight_layout(rect=[0, 0.05, 1, 0.95]) # Ajustar para que no se superpongan los títulos y la leyenda

    # Guardar la figura
    plt.savefig(os.path.join(resultados_path, "svg", 'comparacion_epochs_neighbors.svg'), format='svg')

    plt.show()