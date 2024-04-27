#Hipo: x,y no estan correlacionadas

#Permutas x e y, para cada permu calculo ro, es decir la correlacion

#Podemos decir que p= 0,58 (p < 0,001)

import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de puntos
puntos = np.arange(5, 25, 0.1)

# Definir la función
def f(x):
    return np.e**-x

for i in range(1000):
    n= 20
    uniforme = np.random.uniform(5,100,n)
    uniforme2 = np.random.uniform(0, np.exp(-5),n)
    l1,r1,l2,r2 = 5, 10000000,0,np.e**-5
    cant_y_abajo_funcion = 0
    for u,v in zip(uniforme,uniforme2):
        if v <= f(u):
            cant_y_abajo_funcion += 1
    proba = cant_y_abajo_funcion/ n *(r1 + l1) * (r2 + l2)
# Calcular los valores de la función para cada punto
valores = f(puntos)

# Graficar la función
plt.plot(puntos, valores, label='f(x) = e^(-x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la función f(x) = e^(-x)')
plt.legend()
plt.grid(True)
plt.show()
