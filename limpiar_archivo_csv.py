import csv

def limpiar_archivo(archivo_entrada, archivo_salida, caracteres_prohibidos):
    with open(archivo_entrada, 'r') as archivo_in, open(archivo_salida, 'w', newline='') as archivo_out:
        lector_csv = csv.reader(archivo_in)
        escritor_csv = csv.writer(archivo_out)
        
        for fila in lector_csv:
            fila_limpia = [limpiar_celda(celda, caracteres_prohibidos) for celda in fila]
            escritor_csv.writerow(fila_limpia)

def limpiar_celda(celda, caracteres_prohibidos):
    for caracter in caracteres_prohibidos:
        celda = celda.replace(caracter, '')
    return celda

# Ejemplo de uso
archivo_entrada = 'archivo.csv'
archivo_salida = 'archivo_salida.csv'
caracteres_prohibidos = [';', '#', '$', '%', ',', '/']

limpiar_archivo(archivo_entrada, archivo_salida, caracteres_prohibidos)



'''
En este código, se define una función limpiar_archivo que toma como entrada el nombre del archivo de entrada CSV, el nombre del archivo de 
salida CSV y una lista de caracteres prohibidos que deseas eliminar de las celdas del archivo.

La función utiliza los módulos csv para leer el archivo de entrada y escribir el archivo de salida. Lee cada fila del archivo de entrada y, 
para cada celda, llama a la función limpiar_celda para eliminar los caracteres prohibidos. Luego, escribe la fila limpia en el archivo de salida.

La función limpiar_celda recorre cada caracter prohibido en la lista caracteres_prohibidos y reemplaza esos caracteres en la celda por una 
cadena vacía.

En el ejemplo de uso al final del código, se especifica el nombre del archivo de entrada, el nombre del archivo de salida y la lista 
de caracteres prohibidos. Puedes modificar estos valores según tus necesidades.
'''
