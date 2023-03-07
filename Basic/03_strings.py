# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3] # Da como resultado "yt"
print(language_slice)

language_slice = language[1:] # Da como resultado "ython"
print(language_slice)

language_slice = language[-2] # Da como resultado "o"
print(language_slice)

language_slice = language[0:6:2] # Da como resultado "pto"
print(language_slice)

# Reverse

reversed_language = language[::-1] # Da como resultado "nohtyP"
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize()) # Pone la primera letra en mayúscula
print(language.upper()) # Pone todo en mayúscula
print(language.count("t")) # Cuenta cuantas "t" tiene
print(language.isnumeric()) # Nos dice si es un número
print("1".isnumeric()) # Nos dice si la cadena si es un número
print(language.lower()) # Pone todo en minúsculas
print(language.lower().isupper()) # Devuelve True si todos los caracteres están en mayúsculas, de lo contrario, False. Solo los caracteres alfabéticos

print(language.startswith("Py")) # Si detecta la cadena devuelve Verdadero, de lo contrario False
print("Py" == "py")  # No es lo mismo
