import matplotlib.pyplot as plt
import numpy as np


#Definicion de constantes
G = 6.67 * 10**(-11) #Constante de gravitacion universal
M_sol = 1.9891 * 10**30 #Masa del Sol, en kg
M_tierra = 5.972 * 10**24 #Masa de la Tierra, en kg
M_test = 0.00000000000000000001 #Masa de la partícula de prueba


resolucion = 100 #Tamaño del canvas, de la simulacion

x = 0 #Posicion en x inicial
y = 0 #Posicion en y inicial

pos_sol = (resolucion/2, resolucion/2)


canvas = np.zeros((resolucion,resolucion)) #Canvas o cuadro donde voy a graficar los puntos del mapa


def calcular_gravedad(x,y):
    d = distancia(x,y)
    fuerza = (G * M_sol * M_test) / d**2
    if d <= 6:
        fuerza = 0
    return fuerza

def distancia(x,y):
    d_x_al_sol = abs(x - pos_sol[0]) 
    d_y_al_sol = abs(y - pos_sol[1])

    d = np.sqrt(d_x_al_sol**2 + d_y_al_sol**2)
    return d


def heatmap2d(arr: np.ndarray):
    plt.imshow(arr, cmap='viridis')
    plt.colorbar()
    plt.show()

for i in range(0,100*100):
    #Chequeo los valores de x e y y empiezo a rasterizarlos/escanearlos
    if( x >= 99):
        x = 0
        y += 1
    elif( y >= 99):
        break
    else:
        x += 1
    print("X value is:", x, "Y value is:", y)
    valor = calcular_gravedad(x,y)
    print("Fuerza is:", valor)
    canvas[x,y] = valor  


heatmap2d(canvas)
#test_array = np.arange(100 * 100).reshape(100, 100)
#heatmap2d(test_array)








