"""
Examen unidad 4
En este programa se verá la interacción de un
generente al entrevistar a una persona que sera nuevo empleado
"""
import csv
class Empresa:
    def __init__(self,NombreEmbresa):
        self.__NombreEmpresa = NombreEmbresa

    def setNombreEmpresa(self, nuevoNombre):
        self.__NombreEmpresa = nuevoNombre

    def NombreEmpresa(self):
        print("Hola vienvenido a la empresa",self.__NombreEmpresa,"donde fabricamos todo tipo de prenda")
NombreEmpresa1=Empresa('TRES HERMANOS')
NombreEmpresa1.NombreEmpresa()

class Empleado(Empresa):
    def __init__(self, puesto):
        self.__puesto = puesto

    def getPuesto(self):
        self.__puesto()
    def setPuesto(self, nuevoPuesto):
        self.__puesto = nuevoPuesto

class Puesto(Empleado):
    def __init__(self, nombre,puesto, sexo,edad, estatura):
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
    def setEdad(self,nuevaEdad):
        self.__edad = nuevaEdad
    def setEstatura(self, nuevaEstatura):
        self.__estatura = nuevaEstatura

    def info(self):
        print("Hola mi nombre es", self.__nombre,"tengo", self.__edad,"años")
        print("ocupo el puesto de gerente, soy", self.__sexo,"y mido",self.__estatura)
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
        print("Pregunta 1.- ¿Cuál es su nombre?: ", self.P1)
        print("Pregunta 2.- ¿Dónde vive?: ", self.P2)
        print("Pregunta 3.- ¿Qúe grado de estudio tiene?: ", self.P3)
        print("Pregunta 4.- ¿Por qué te interesa el puesto?: ", self.P4)
        print("Pregunta 5.- ¿Qué sabes de nuestra empresa?: ", self.P5)
        print("Pregunta 6: ¿Qué te gusta hacer en tu tiempo libre?: ", self.P6)
        print("Pregunta 7.- ¿Cuál es tu meta en la vida?: ", self.P7)
        print("Pregunta 8.- ¿Cómo manejas la presión?: ", self.P8)
        print("Pregunta 9.- ¿Cuál es tu mayor debilidad o defecto?: ", self.P9)
        print("Pregunta 10.- ¿Por qué deberíamos contratarte?: ", self.P10)

class saco:
    def __init__(self,medida,color,botones):
        self.__medida=medida
        self.__color=color
        self.__botones=botones

    def vestir(self):
        print("Hoy visto de un saco talla",self.__medida,"de color",self.__color,"con",self.__botones,"botones")
saco1=saco('chica','azul','tres')


print("Si usted desea trabajar en la empresa escriba [Si]")
condicion = input("sino presione cualquier tecla: ")
print("---------------------------------------------------------------------------------")
if (condicion == 'Si') or (condicion == 'si') or (condicion == 'SI'):
    print("Hola usted a decidido ingresar a nuestra empresa,")
    print("ahora vendra un personal para atenderlo")
    Nombre = input("Porfavor ingrese el nombre de la persona que lo atendera: ")
    print("---------------------------------------------------------------------------------")
    gerente1 = Puesto(Nombre,'gerente','hombre','25','1.80m')
    gerente1.info()
    saco1.vestir()
    print("---------------------------------------------------------------------------------")
    print("Ahora le haré algunas preguntas...")
    P1 = input("Pregunta 1.- ¿Cuál es su nombre?: ")
    P2 = input("Pregunta 2.- ¿Dónde vive?: ")
    P3 = input("Pregunta 3.- ¿Qué grado de estudio tiene?: ")
    P4 = input("Pregunta 4.- ¿Por qué te interesa el puesto?: ")
    P5 = input("Pregunta 5.- ¿Qué sabes de nuestra empresa?: ")
    P6 = input("Pregunta 6: ¿Qué te gusta hacer en tu tiempo libre?: ")
    P7 = input("Pregunta 7.- ¿Cuál es tu meta en la vida?: ")
    P8 = input("Pregunta 8.- ¿Cómo manejas la presión?: ")
    P9 = input("Pregunta 9.- ¿Cuál es tu mayor debilidad o defecto?: ")
    P10 = input("Pregunta 10.- ¿Por qué deberíamos contratarte?: ")

    Entrevista1 = preguntas(P1,P2,P3,P4,P5,P6,P7,P8,P9,P10)
    Entrevista1.hacerEntrevista()
    with open('Registro.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow([f'Pregunta 1.- ¿Cual es su nombre?: {P1}'])
        spamwriter.writerow([f'Pregunta 2.- ¿Donde vive?: {P2}'])
        spamwriter.writerow([f'Pregunta 3.- ¿Que grado de estudio tiene?: {P3}'])
        spamwriter.writerow([f'Pregunta 4.- ¿Por qué te interesa el puesto?: {P4}'])
        spamwriter.writerow([f'Pregunta 5.- ¿Que sabes de nuestra empresa?:  {P5}'])
        spamwriter.writerow([f'Pregunta 6.- ¿Que te gusta hacer en tu tiempo libre?: {P6}'])
        spamwriter.writerow([f'Pregunta 7.- ¿Cual es tu meta en la vida?: {P7}'])
        spamwriter.writerow([f'Pregunta 8.- ¿Como manejas la presión?: {P8}'])
        spamwriter.writerow([f'Pregunta 9.- ¿Cual es tu mayor debilidad o defecto?: {P9}'])
        spamwriter.writerow([f'Pregunta 10.- ¿Por que deberíamos contratarte?: {P10}'])

    print("---------------------------------------------------------------------------------")
    print("Se han guardado sus respuestas con exito")
    print("---------------------------------------------------------------------------------")
    print(f"Hola {P1} usted ya es integrante de nuestra empresa")
    print()


else:
    print("Hasta luego, que tenga exelente día")