import numpy as np
import matplotlib.pyplot as plt

def graficar_vectores( vecs, cols, alpha=1):    
    plt.axvline(x=0, color='grey', zorder = 0)
    plt.axhline(y=0, color='grey', zorder = 0)
    
    for i in range(len(vecs)):
        x = np.concatenate(([0,0], vecs[i]))
        
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy', scale_units='xy', scale=1,
                   color=cols[i],
                   alpha = alpha)


def graficarMatriz(matriz, vectorCol=['red', 'blue']):
    
    #círculo unitario
    x = np.linspace(-1, 1, 100000)
    y = np.sqrt(1 - (x**2))
    
    #Transformamos x e y en una matriz de vectores x, y
    vector_x_y = np.array([x, y])
    
    # círculo unitario transformado (curva del espacio)
    prod_punto = matriz.dot(vector_x_y)
    
    #vectores
    u1 = [matriz[0, 0], matriz[1, 0]]
    v1 = [matriz[0, 1], matriz[1, 1]]
    
    graficar_vectores([u1, v1], cols=[vectorCol[0], vectorCol[1]])
    
    plt.plot(prod_punto[0], prod_punto[1], 'purple', alpha = 0.7)
    plt.plot(-prod_punto[0], -prod_punto[1], 'green', alpha = 0.7)