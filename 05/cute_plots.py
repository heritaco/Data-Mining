# practica 3

import matplotlib.pyplot as plt
import seaborn as sns


def box_plot(column, mergefull, dictcat, palette):
    sns.set_style('whitegrid')  # estilo de la grafica
    plt.figure(figsize=(3, 6))
    ax = sns.boxplot(y=mergefull[column], color=palette[0], width=0.6, linewidth=1.5)
    plt.title(dictcat[column] + '\n', fontsize=16, fontweight='bold')
    plt.xlabel(column.capitalize(), fontsize=12)
    plt.ylabel('Valores', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # cuadricula en el eje y
    plt.grid(axis='x', linestyle='--', alpha=0)    # cuadricula en el eje x
    
    sns.despine(left=True)  # quitar el borde izquierdo
    plt.savefig(f'boxplot_{column}.svg', bbox_inches='tight')  # guardar la grafica
    plt.show()

def histograma(column, mergefull, dictcat, palette, numerito=False):
    sns.set_style('whitegrid')  # estilo de la grafica
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(mergefull[column], color=palette[0], alpha=0.7, binwidth=1)
    plt.title(dictcat[column] + '\n', fontsize=16, fontweight='bold')
    plt.xlabel("")
    plt.ylabel('Frecuencia', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # cuadricula en el eje y
    plt.grid(axis='x', linestyle='--', alpha=0)    # cuadricula en el eje x
    
    if numerito: 
        # agregar etiquetas con el valor de cada barra
        for p in ax.patches:
            ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', fontsize=6, color='black', xytext=(0, 5), 
                        textcoords='offset points')
        
    sns.despine(left=True)  # quitar el borde izquierdo
    plt.tight_layout()
    plt.savefig(f'histograma_{column}.svg', bbox_inches='tight')  # guardar la grafica
    plt.show()

def grafico_de_barras(column, mergefull, dictcat, diccionario_etiquetas, palette, plotdesconocido=False, numerito=True):
    sns.set_style('whitegrid')  # estilo de la grafica
    plt.figure(figsize=(6, 6))
    
    vc = mergefull[column].value_counts()  # cuenta los valores de la columna
    etiquetas = [diccionario_etiquetas[column].get(str(tag), 'Desconocido') for tag in vc.index]
    
    if not plotdesconocido:
        # filtrar valores desconocidos, esos son los que no tenian que contastar esa pregunta
        vc = vc[[etiqueta != 'Desconocido' for etiqueta in etiquetas]]
        etiquetas = [etiqueta for etiqueta in etiquetas if etiqueta != 'Desconocido']
    
    ax = vc.plot(kind='bar', color=palette, alpha=0.8, width=1)  # crea el grafico de barras
    plt.title(dictcat[column] + '\n', fontsize=16, fontweight='bold')
    plt.xlabel('')
    plt.xticks(rotation=0, fontsize=10)  # rotacion de las etiquetas del eje x
    ax.set_xticklabels(etiquetas, rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # cuadricula en el eje y
    plt.grid(axis='x', linestyle='--', alpha=0)  # cuadricula en el eje x
    
    # agregar etiquetas con el valor de cada barra
    if numerito:
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', fontsize=8, color='black', xytext=(0, 5), 
                        textcoords='offset points')
    
    sns.despine(left=True)  # quita el borde izquierdo
    plt.savefig(f'grafico_de_barras_{column}.svg', bbox_inches='tight')  # guardar la grafica
    plt.show()

def heatmap(x, y, mergefull, dictcat, diccionario_etiquetas, categorico=True): # se supone que es para categoricos
    plt.figure(figsize=(10, 6))

    vcx = mergefull[x].value_counts()  # cuenta los valores de la columna
    vcy = mergefull[y].value_counts()  # cuenta los valores de la columna

    cmap = sns.dark_palette('#69d', reverse=False, as_cmap=True)  # matplotli
    ax = sns.heatmap(mergefull.groupby([x, y]).size().unstack(), cmap=cmap, annot=True, fmt='.1f', linewidths=0.5, linecolor='white')
    plt.title(f'Correlación entre {dictcat[x].title()} y {dictcat[y].title()} \n', fontsize=16, fontweight='bold')  # titulo
    plt.xlabel(dictcat[y].title())  # etiqueta eje x
    plt.ylabel(dictcat[x].title())  # etiqueta eje y

    plt.grid(axis='y', linestyle='--', alpha=0.1)
    plt.grid(axis='x', linestyle='--', alpha=0.1)

    plt.xticks(fontsize=8, rotation=90)
    plt.yticks(fontsize=8, rotation=0)
    
    if categorico: 
        ax.set_xticklabels([diccionario_etiquetas.get(y, {}).get(str(tag), 'Desconocido') for tag in vcy.index], rotation=90)
        ax.set_yticklabels([diccionario_etiquetas.get(x, {}).get(str(tag), 'Desconocido') for tag in vcx.index], rotation=0)

    plt.tight_layout()
    plt.savefig(f'heatmap_{x}_{y}.svg', bbox_inches='tight')  # guardar la grafica
        
    plt.show()

def matriz_correlacion(columns, mergefull, dictcat):
    plt.figure(figsize=(12, 10))
    
    corr_matrix = mergefull[columns].corr() # Calcular la matriz de correlación
    
    cmap = sns.diverging_palette(240, 12, as_cmap=True)
    ax = sns.heatmap(corr_matrix, cmap=cmap, annot=True, fmt='.2f', linewidths=0.5, linecolor='white')
    
    plt.title('Matriz de Correlación \n', fontsize=16, fontweight='bold')

    yticklabels = [dictcat.get(col, col).title() for col in columns] # diccionario de etiquetas   
    ax.set_xticklabels('')  # que en el eje x no haya etiquetas
    ax.set_yticklabels(yticklabels, fontsize=10, rotation=0) # etiquetas en el eje y

    plt.savefig('matriz_correlacion.svg', bbox_inches='tight')  # bbox para no cortar la grafica

    plt.show()

def scatter_plot(x, y, mergefull, dictcat, diccionario_etiquetas, palette):
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 6))
    ax = sns.scatterplot(data=mergefull, x=x, y=y, color=palette[0], alpha=0.15, linewidth=0.1)
    plt.title(f'{dictcat[x].title()} vs {dictcat[y].title()} \n', fontsize=16, fontweight='bold')
    plt.xlabel(dictcat[x].title(), fontsize=12)
    plt.ylabel(dictcat[y].title(), fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.5)   # cuadricula
    plt.tight_layout()
    sns.despine(left=True)  # quitae l borde izquierdo
    plt.savefig(f'scatter_plot_{x}_{y}.svg', bbox_inches='tight')  # guardar la grafica
    plt.show()

class CutePlots:
    def __init__(self, mergefull, dictcat, diccionario_etiquetas, colorpalette):
        self.mergefull = mergefull
        self.dictcat = dictcat
        self.diccionario_etiquetas = diccionario_etiquetas
        self.palette = sns.color_palette(colorpalette)

    def box_plot(self, column):
        return box_plot(column, self.mergefull, self.dictcat, self.palette)

    def histograma(self, column, numerito=False):
        return histograma(column, self.mergefull, self.dictcat, self.palette, numerito)
    
    def grafico_de_barras(self, column, plotdesconocido=False, numerito=True):
        return grafico_de_barras(column, self.mergefull, self.dictcat, self.diccionario_etiquetas, self.palette, plotdesconocido, numerito)
    
    def heatmap(self, x, y, categorico=True):
        return heatmap(x, y, self.mergefull, self.dictcat, self.diccionario_etiquetas, categorico)
    
    def matriz_correlacion(self, columns):
        return matriz_correlacion(columns, self.mergefull, self.dictcat)
    
    def scatter_plot(self, x, y):
        return scatter_plot(x, y, self.mergefull, self.dictcat, self.diccionario_etiquetas, self.palette)