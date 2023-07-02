import random

def generar_apuestas(num_apuestas):
    apuestas = []
    for _ in range(num_apuestas):
        apuesta = random.sample(range(1, 50), 6)
        apuestas.append(sorted(apuesta))
    return apuestas

def imprimir_apuestas(apuestas):
    for i, apuesta in enumerate(apuestas, 1):
        print(f"Apuesta {i}: {apuesta}")

# Pedir al usuario la cantidad de apuestas a generar
num_apuestas = int(input("Ingrese la cantidad de apuestas que desea generar: "))

# Generar las apuestas
apuestas = generar_apuestas(num_apuestas)

# Imprimir las apuestas generadas
imprimir_apuestas(apuestas)

'''
Código en Python que te permitirá calcular "x" apuestas para la lotería primitiva. En este código, asumiré que los números de la lotería 
primitiva van del 1 al 49 y que cada apuesta consta de 6 números.

Explicación del código:

La función generar_apuestas recibe como parámetro el número de apuestas que se desean generar. Utiliza la función random.sample para obtener 
6 números únicos aleatorios del rango del 1 al 49. Los números de cada apuesta se almacenan en una lista y se ordenan de menor a mayor. 
Esta lista se agrega a la lista de apuestas.
La función imprimir_apuestas recibe la lista de apuestas y las imprime en el formato deseado.
En el código principal, se solicita al usuario la cantidad de apuestas que desea generar.
Se llama a la función generar_apuestas con el número ingresado por el usuario y se almacenan las apuestas generadas en la variable apuestas.
Finalmente, se llama a la función imprimir_apuestas para mostrar las apuestas generadas en la consola.
'''
