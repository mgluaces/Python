import math
import random

def lanzamiento_baseball():
    # Generar velocidad y ángulo aleatorios
    velocidad = random.uniform(40, 120)  # en mph
    angulo = random.uniform(20, 70)  # en grados

    # Convertir ángulo de grados a radianes
    angulo_rad = math.radians(angulo)

    # Convertir velocidad de mph a m/s
    velocidad_ms = velocidad * 0.447  # factor de conversión de mph a m/s

    # Calcular las componentes horizontal y vertical de la velocidad inicial
    velocidad_x = velocidad_ms * math.cos(angulo_rad)
    velocidad_y = velocidad_ms * math.sin(angulo_rad)

    # Calcular el tiempo de vuelo
    tiempo_vuelo = (2 * velocidad_y) / 9.8

    # Calcular la distancia alcanzada
    distancia = velocidad_x * tiempo_vuelo

    # Imprimir los resultados
    print("Simulación de lanzamiento de béisbol:")
    print("Velocidad: {:.2f} mph".format(velocidad))
    print("Ángulo: {:.2f} grados".format(angulo))
    print("Distancia alcanzada: {:.2f} metros".format(distancia))

# Ejecutar la simulación
lanzamiento_baseball()

'''
Este código generará una velocidad aleatoria en el rango de 40 a 120 mph y un ángulo aleatorio en el rango de 20 a 70 grados. 
Luego, calculará la distancia alcanzada por la pelota utilizando las fórmulas de la física del movimiento de proyectiles. 
Por último, imprimirá los resultados en la consola.
'''
