"""
Examen unidad 4
En este programa se verá la interacción de un
generente al entrevistar a una persona que sera nuevo empleado
"""
class Empresa:
    def __init__(self,NombreEmbresa):
        self.__NombreEmpresa = NombreEmbresa

class Empleado(Empresa):
    def __init__(self, puesto):
        self.__puesto = puesto


class Gerente(Empleado):
    def __init__(self, nombre, sexo,puesto,edad =('25'), estatura = ('1.80m')):
        super().__init__(puesto)
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
        print("Hola mi nombre es: ", self.__nombre)
        print("Tengo", self.__edad,"años")
        print("Mi genero es: ", self.__sexo)
        print("Y mi estatura es: ",self.__estatura)

print("Hola vienvenido a la empresa TRES HERMANOS ")
condicion = input("Hola qué tal, si usted desea ingresar a nuestra empresa presione la tecla 1,"
                " sino presiones cualquier tecla")
if (condicion == '1'):
    print("Hola usted a decidido ingresar a nuestra empresa,")
    print("ahora vendra un personal para atenderlo")
    Nombre = input("Porfavor ingrese el nombre de la persona que lo atendera: ")
    Sexo = input("Porfavor ingrese el genero de la persona que desee que lo atienda: ")
    Puesto = input("El puesto es: ")

    gerente1 = Gerente(Nombre, Sexo,Puesto)
    gerente1.info()
else:
    print("Hasta luego, que tenga exelente día")











