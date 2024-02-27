import sys

class Perro(object):
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad
        print("constructor de %s(%s, %d)" % (self.clase(), self.nombre, self.edad))

    def __del__(self):
        print("finalizador (no se usa)")

    def __str__(self):
        return "% 12s: %s(%s)" % (self.clase(), self.nombre, self.edad)

    def clase(self):
        return self.__class__.__name__

    def imprimir(self, output=sys.stdout):
        mensaje = "Imprimimos %s\n" % self
        output.write(mensaje)


def main():
    print("Inicio")

    p1 = Perro()
    p2 = Perro("cuki")
    p3 = Perro(edad=7)
    p4 = Perro("pupi", 17)

    p1.imprimir()
    p2.imprimir()
    p3.imprimir()
    p3.nombre = "yupi";
    p3.imprimir()
    p4.imprimir()

    print("Lista")
    lista_bichos = [p1, p2, p3, p4]
    for bicho in lista_bichos:
        print(bicho)

    print("Construccion y destruccion")
    p = Perro("fufi", 2)
    interno = Perro(3)
    p.imprimir()
    del p
    interno.imprimir()
    #ojo: p.imprimir()
    p.imprimir()

    print("Fin")


if __name__ == '__main__':
    main()
