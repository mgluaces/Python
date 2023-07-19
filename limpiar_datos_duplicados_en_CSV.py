import csv

def limpiar_archivo_duplicados(archivo_entrada, archivo_salida):
    registros_unicos = set()
    with open(archivo_entrada, 'r') as archivo_in, open(archivo_salida, 'w', newline='') as archivo_out:
        lector_csv = csv.reader(archivo_in)
        escritor_csv = csv.writer(archivo_out)
        
        for fila in lector_csv:
            registro = tuple(fila)  # Convertir la fila en una tupla para que sea hashable
            if registro not in registros_unicos:
                escritor_csv.writerow(fila)
                registros_unicos.add(registro)

# Ejemplo de uso
archivo_entrada = r'c:/Users/Usuario/Desktop/PRUEBAS/PYTHON/informeCentros_TF.csv'
archivo_salida = r'c:/Users/Usuario/Desktop/PRUEBAS/PYTHON/datos_salida.csv'

limpiar_archivo_duplicados(archivo_entrada, archivo_salida)

'''
En este código, se define una función limpiar_archivo_duplicados que toma como entrada el nombre del archivo de entrada CSV 
y el nombre del archivo de salida CSV.

La función utiliza un conjunto (set) llamado registros_unicos para almacenar los registros únicos que se encuentren durante 
el proceso de lectura del archivo CSV.

Se utiliza un bucle para recorrer cada fila del archivo de entrada. Cada fila se convierte en una tupla para que pueda ser 
utilizada como una clave hashable en el conjunto registros_unicos. Si la tupla no está presente en el conjunto, se escribe 
en el archivo de salida y se agrega al conjunto registros_unicos. De esta manera, solo se escriben en el archivo de salida 
los registros que no están duplicados.

En el ejemplo de uso al final del código, se especifica el nombre del archivo de entrada y el nombre del archivo de salida. 
Puedes modificar estos valores según tus necesidades.
'''