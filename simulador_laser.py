import numpy as np
import matplotlib.pyplot as plt

def double_slit_interference(d, wavelength, distance, screen_width, screen_distance, num_slits=2):
    """
    Simula el patrón de interferencia de la doble rendija.
    
    Parámetros:
        - d: Separación entre las rendijas (en metros).
        - wavelength: Longitud de onda de la luz (en metros).
        - distance: Distancia entre las rendijas y la pantalla (en metros).
        - screen_width: Ancho de la pantalla (en metros).
        - screen_distance: Distancia entre el punto de observación y la pantalla (en metros).
        - num_slits: Número de rendijas (por defecto 2).
        
    Retorna:
        - x_values: Valores de posición en el eje x.
        - intensity: Intensidad de la luz en cada posición.
    """
    x_values = np.linspace(-screen_width / 2, screen_width / 2, 1000)
    intensity = np.zeros_like(x_values)

    for i in range(num_slits):
        path_difference = d * i
        intensity += np.cos(2 * np.pi * path_difference / wavelength) ** 2

    intensity /= num_slits

    # Corrección por distancia
    intensity *= (wavelength * distance / (screen_distance * np.pi)) ** 2

    return x_values, intensity

# Parámetros del experimento
d = 0.1  # Separación entre las rendijas (en metros)
wavelength = 0.0000005  # Longitud de onda de la luz (en metros)
distance = 1  # Distancia entre las rendijas y la pantalla (en metros)
screen_width = 0.1  # Ancho de la pantalla (en metros)
screen_distance = 2  # Distancia entre el punto de observación y la pantalla (en metros)

# Simulación del experimento
x_values, intensity = double_slit_interference(d, wavelength, distance, screen_width, screen_distance)

# Gráfico del patrón de interferencia
plt.plot(x_values, intensity)
plt.title("Patrón de Interferencia de Doble Rendija")
plt.xlabel("Posición en la pantalla (metros)")
plt.ylabel("Intensidad de la luz")
plt.show()
