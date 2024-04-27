import numpy as np
import matplotlib.pyplot as plt

a = 0  # límite inferior del rango
b = 1  # límite superior del rango
n = 100  # número de variables aleatorias a generar

# Generar variables aleatorias uniformes
x = np.random.uniform(a, b, n)

# Calcular la función característica de cada variable
phi = np.exp(1j * x)

# Calcular el producto de las funciones características
phi_prod = np.exp(1j * np.sum(x))

# Graficar la parte real e imaginaria de la función característica
t_values = np.linspace(-10, 10, 1000)
phi_values = np.exp(1j * np.sum(x) * t_values)

plt.plot(t_values, np.real(phi_values), label='Parte Real')
plt.plot(t_values, np.imag(phi_values), label='Parte Imaginaria')
plt.xlabel('t')
plt.ylabel('phi(t)')
plt.title('Función Característica del Producto de Variables Aleatorias Uniformes')
plt.legend()
plt.grid(True)
plt.show()
