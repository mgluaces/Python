# Medir tiempo de ejecución
import time
inicio = time.time()

time.sleep(1)

# Simulación de lanzamientos de Baseball
import random

def lanzamiento_baseball():
    strikes = 0
    bolas = 0

    while strikes < 3 and bolas < 4:
        # Generar un número aleatorio entre 0 y 1 para determinar si es bola o strike
        resultado = random.random()

        if resultado < 0.6:  # 60% de probabilidad de ser strike
            strikes += 1
            print("¡Strike!")
        else:
            bolas += 1
            print("¡Bola!")

        print("Strikes: {}, Bolas: {}".format(strikes, bolas))
        print()

    # Verificar el resultado del lanzamiento
    if strikes == 3:
        print("¡El bateador fue eliminado por strikes!")
    elif bolas == 4:
        print("¡El bateador avanzó a la primera base por bolas!")

# Ejecutar el simulador de lanzamiento
lanzamiento_baseball()

# Verificar el tiempo de ejecución
fin = time.time()
print("Tiempo de ejecución:" , fin-inicio)

'''
En este código, se utiliza un bucle while para simular los lanzamientos hasta que el número de strikes llegue a 3 o el número de bolas llegue a 4. 
En cada iteración del bucle, se genera un número aleatorio entre 0 y 1 para determinar si es un strike (60% de probabilidad) o una bola (40% de 
probabilidad). Luego, se actualizan los contadores de strikes y bolas, y se muestra el resultado actual.

Después de finalizar el bucle, se verifica el resultado del lanzamiento y se imprime un mensaje indicando si el bateador fue eliminado por 
strikes o si avanzó a la primera base por bolas.
'''
