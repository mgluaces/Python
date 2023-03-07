# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list() # Creas la lista
my_other_list = [] # Así también creamos una lista

print(len(my_list)) # Calcula la longitud de la lista

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list)) # Nos dice que clase es 
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) # Devuelve el número de ocurrencias de un valor
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Brais"))

age, height, name, surname = my_other_list # asigna variables a los valores de la lista
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev") # añadir un elemento
print(my_other_list)

my_other_list.insert(1, "Rojo") # inserta en la posición "1" el valor "Rojo"
print(my_other_list)

my_other_list[1] = "Azul" # Modifica el valor del índice en la lista
print(my_other_list)

my_other_list.remove("Azul") # elimina un valor de la lista
print(my_other_list)

my_list.remove(30) # elimina el primer elemento de dicho valor
print(my_list)

print(my_list.pop()) # elimina el último valor de la lista
print(my_list)

my_pop_element = my_list.pop(2) # elimina el valor del índice dado, guardando el valor en la variable
print(my_pop_element)
print(my_list)

del my_list[2] # elimina el valor de la lista que se encuenta en la posición del índice dada
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy() # copia una lista en otra lista

my_list.clear() # vacía la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # se le da la vuelta a la lista
print(my_new_list)

my_new_list.sort() # ordena la lista
print(my_new_list)

# Sublistas

print(my_new_list[1:3]) # no entrega el o los valores entre los índices dados

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))
