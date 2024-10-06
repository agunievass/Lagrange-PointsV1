import matplotlib.pyplot as plt
import numpy as np


#Definicion de constantes
G = 6.67 * 10**(-11) #Constante de gravitacion universal
M_sol = 1.9891 * 10**30 #Masa del Sol, en kg
M_tierra = 5.972 * 10**24 #Masa de la Tierra, en kg
M_test = 0.00000000000000001 #Masa de la partícula de prueba

#Datos a tener a mano
#Radio del Sol = 694,340km
#Radio de la Tierra = 6371km

radio_sol = 150 #Radio del sol en pixeles/bloquecitos de la rejilla
radio_tierra = (6371*radio_sol)/694340

resolucion = 3000 #Tamaño del canvas, de la simulacion

x = 0 #Posicion en x inicial
y = 0 #Posicion en y inicial

pos_sol = (resolucion/2, resolucion/2)
pos_tierra = (pos_sol[0] + 0, pos_sol[1] + 5*radio_sol) #Posicion de la tierra, las distancias sumadas son radios solares.
print("La posicion de la tierra es:", pos_tierra)
canvas = np.zeros((resolucion,resolucion)) #Canvas o cuadro donde voy a graficar los puntos del mapa


def calcular_gravedad_solar(x,y): #Calcula/Devuelve el modulo de la fuerza ejercida entre el sol y la perticula de prueba
    d = distancia_al_sol(x,y)
    fuerza = (G * M_sol * M_test) / d**2
    if d <= radio_sol: #Elimino los valores de fuerza que sean menores que el radio del sol, la dimensión es el radio del sol.
        fuerza = 0
    return fuerza

def calcular_gravedad_terrestre(x,y):
    d = distancia_al_tierra(x,y)
    fuerza = (G * M_tierra * M_test) / d**2
    if d <= radio_tierra: #Elimino los valores de fuerza que sean menores que el radio de la tierra
        fuerza = 0
    return fuerza


def distancia_al_tierra(x,y): #Devuelve la distancia del punto (x,y) al centro de la tierra
    d_x_al_tierra = abs(x - pos_tierra[0])
    d_y_al_tierra = abs(y - pos_tierra[1])

    d = np.sqrt(d_x_al_tierra**2 + d_y_al_tierra**2)
    return d


def distancia_al_sol(x,y): #Devuelve la distancia del punto (x,y) al centro del sol
    d_x_al_sol = abs(x - pos_sol[0]) 
    d_y_al_sol = abs(y - pos_sol[1])

    d = np.sqrt(d_x_al_sol**2 + d_y_al_sol**2)
    return d


def heatmap2d(arr: np.ndarray):
    plt.imshow(arr, cmap='viridis')
    plt.colorbar()
    plt.show()

for i in range(0,resolucion*resolucion):
    #Chequeo los valores de x e y y empiezo a rasterizarlos/escanearlos
    if( x >= resolucion-1):
        x = 0
        y += 1
    elif( y >= resolucion-1):
        break
    else:
        x += 1
    #print("X value is:", x, "Y value is:", y)
    #valor_1 =  calcular_gravedad_solar(x,y)
    valor_2 = calcular_gravedad_terrestre(x,y)
    

    #print("Fuerza is:", valor)
    canvas[x,y] =  valor_2


heatmap2d(canvas)

print(pos_sol)
print(pos_tierra)
#test_array = np.arange(100 * 100).reshape(100, 100)
#heatmap2d(test_array)








