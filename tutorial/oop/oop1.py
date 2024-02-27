
class Animal:
    def hazruido(self):            return "ruido animal"
    def __add__(self, otro):       return self.hazruido() + " " + type(otro).__name__
    def dametamano(self):          return 0

class Perro(Animal):
    def hazruido(self):            return "guau"
    def dametamano(self):          return 10

class Gato(Animal):
    def hazruido(self):            return "miau"
    def dametamano(self):          return 4

class Doberman(Perro):
    def hazruido(self):            return "grrrrr"
    def dametamano(self, cad=""):  return 17 if cad else 20

def clase(bicho):            return bicho.__class__.__name__


def ver_bicho(bicho):
    cls, ruido, tam = clase(bicho), bicho.hazruido(), bicho.dametamano()
    print("% 12s: %s(%s)" % (cls, ruido, tam))


def main():
    print("Inicio")

    a = Animal()
    p = Perro()
    g = Gato()
    d = Doberman()

    ver_bicho(a)
    ver_bicho(p)
    ver_bicho(g)
    ver_bicho(d)

    print("Lista")
    lista_bichos = [a, p, g, d]
    for bicho in lista_bichos:
        ver_bicho(bicho)

    print("Sobrecarga")
    print("% 12s: %s y %s" % (clase(a), a + 34, a + 4.2))
    print("% 12s: %s y %s" % (clase(d), d + 34, d + 4.2))
    print("% 12s: %s" % (clase(d), d.dametamano("raro")))

    print("Fin")


if __name__ == '__main__':
    main()
