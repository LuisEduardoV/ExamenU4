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
    def __init__(self,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10):
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        self.P5 = P5
        self.P6 = P6
        self.P7 = P7
        self.P8 = P8
        self.P9 = P9
        self.P10 = P10
    def hacerEntrevista(self):
        print("Pregunta1: ", self.P1)
        print("Pregunta1: ", self.P2)
        print("Pregunta1: ", self.P3)
        print("Pregunta1: ", self.P4)
        print("Pregunta1: ", self.P5)
        print("Pregunta1: ", self.P6)
        print("Pregunta1: ", self.P7)
        print("Pregunta1: ", self.P8)
        print("Pregunta1: ", self.P9)
        print("Pregunta1: ", self.P10)

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
    print("---------------------------------------------------------------------------------")
    print("Ahora le haré algunas preguntas...")
    P1 = input("Pregunta 1.- ¿Cuál es su nombre?: ")
    P2 = input("Pregunta 2.- ¿Dónde vive?: ")
    P3 = input("Pregunta 3.- ¿Qúe grado de estudio tiene?: ")
    P4 = input("Pregunta 4.- ¿Por qué te interesa el puesto?: ")
    P5 = input("Pregunta 5.- ¿Qué sabes de nuestra empresa?: ")
    P6 = input("Pregunta 6: ¿Qué te gusta hacer en tu tiempo libre?: ")
    P7 = input("Pregunta 7.- ¿Cuál es tu meta en la vida?: ")
    P8 = input("Pregunta 8.- ¿Cómo manejas la presión?: ")
    P9 = input("Pregunta 9.- ¿Cuál es tu mayor debilidad o defecto?: ")
    P10 = input("Pregunta 10.- ¿Por qué deberíamos contratarte?: ")
    Entrevista1 = preguntas(P1,P2,P3,P4,P5)
    Entrevista1.hacerEntrevista()
    print("Se han guardado sus respuestas con exito")




else:
    print("Hasta luego, que tenga exelente día")











