"""
Examen unidad 4
En este programa se verá la interacción de un
generente al entrevistar a una persona que sera nuevo empleado
"""
class Empresa:
    def __init__(self,NombreEmbresa):
        self.__NombreEmpresa = NombreEmbresa
        pass

class Empleado(Empresa):
    def __init__(self, puesto):
        self.__puesto = puesto

    def getPuesto(self):
        self.__puesto()

class Gerente(Empleado):
    def __init__(self, nombre,puesto=None, sexo='hombre',edad ='25', estatura = '1.80m'):
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
        print("Hola mi nombre es", self.__nombre,"tengo", self.__edad,"años")
        print("ocupo el puesto de gerente","soy", self.__sexo,"y mido",self.__estatura)
class preguntas:
    def __init__(self,Pregunta1,Pregunta2,Pregunta3,Pregunta4,Pregunta5):
        self.__Pregunta1 = Pregunta1
        self.__Pregunta2 = Pregunta2
        self.__Pregunta3 = Pregunta3
        self.__Pregunta4 = Pregunta4
        self.__Pregunta5 = Pregunta5

    def hacerEntrevista(self):
        print("Ahora le voy hacer una entrevista....")


class saco:
    def __init__(self,medida,color,botones):
        self.__medida=medida
        self.__color=color
        self.__botones=botones

print("Hola vienvenido a la empresa TRES HERMANOS ")
print("Si usted desea trabajar en la empresa presione la tecla 1")
condicion = input("sino presione cualquier tecla: ")
print("---------------------------------------------------------------------------------")
if (condicion == '1'):
    print("Hola usted a decidido ingresar a nuestra empresa,")
    print("ahora vendra un personal para atenderlo")
    Nombre = input("Porfavor ingrese el nombre de la persona que lo atendera: ")
    print("---------------------------------------------------------------------------------")
    gerente1 = Gerente(Nombre)
    gerente1.info()

else:
    print("Hasta luego, que tenga exelente día")











