class Alumno:
    def dimetunombre(self):
        return self.nombre

    def imprimetunombre(self):
        print(self.dimetunombre())

    def __init__(self, nombr="no se"):
        self.nombre = nombr


class Erasmus(Alumno):
    def dimetunombre(self):
        return "yo ser Errasmus estiuden"


def imprimir(alumno):
    alumno.imprimetunombre()


a1 = Alumno("Fulano")
a2 = Erasmus("Mengano")
imprimir(a1)
imprimir(a2)
# a2.imprimetunombre()
