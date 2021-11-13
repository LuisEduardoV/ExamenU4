"""

Estos son los cambios realizados desde pycharm

"""
class Gerente:
    def __init__(self, nombre, edad, sexo, estatura = ('1.80m')):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__estatura = estatura

    def getNombre(self):
        self.__nombre()
    def getEdad(self):
        self.__edad()
    def getSexo(self):
        self.__sexo()
    def getEstatura(self):
        self.__estatura()

    def info(self):
        print("El nombre del generte es: ", self.__nombre)
        print("La edad del gerente es: ", self.__edad)
        print("El sexo del gerente es: ", self.__sexo)
        print("La estatura del generte es: ",self.__estatura)

Nombre = input("Ingrese un nombre para el generte: ")
Edad= input("Ingrese la edad del generte: ")
Sexo= input(": ")


gerente1 = Gerente(Nombre,Edad,Sexo)
gerente1.info()



