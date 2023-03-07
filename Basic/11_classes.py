# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición

class MyEmptyPerson: # por buenas prácticas, los nombres de las clases se escriben sin espacios y sin guiones, y en mayúsculas la primera letra de cada palabra
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson()) # Funciona igual con o sin paréntesis, los parentesis serán necesarios, cuando hace falta algo para poder ejecutarse

# Clase con constructor, funciones y propiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"): # con "self" se está creando un constructor
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública (al poner los paréntesis, le decimos que el valor lo presente entre paréntesis, pero puede ser cualquier caracter)
        self.__name = name  # Propiedad privada (no modificable al ser privada)

    def get_name(self): # De esta manera puedo acceder a "name"
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)
