# Lotería primitiva sorteo

import random 

# Números del 1 al 49
numeros = list(range(1,50))

# Mezclar números  
random.shuffle(numeros)

# Seleccionar 6 números ganadores  
ganadores = numeros[:6]

# Ordenar los números ganadores    
ganadores.sort()

# Mostrar los números ganadores
print(ganadores)

'''
Este código en Python genera un sorteo de lotería primitiva. Se importa la librería random para usar shuffle() y generar números aleatorios. 
Se crea una lista con los números del 1 al 49, se mezclan esos números y luego se seleccionan los 6 primeros para crear los números ganadores. 
Finalmente se ordenan los números ganadores de menor a mayor y se imprimen.
'''
