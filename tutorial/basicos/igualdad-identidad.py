#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-


class A():
    pass

class B():
    def __eq__(self, other):
        return True

class C():
    def __eq__(self, other):
        return False


def ejemplo(cls):
    elem1 = construct('elem1', cls)
    elem2 = construct('elem2', cls)
    print("Hacemos elem3 = elem1")
    elem3 = elem1
    display("elem1 == elem2",  elem1 == elem2)
    display("elem1 == elem3",  elem1 == elem3)
    display("elem1 is elem2",  elem1 is elem2)
    display("elem1 is elem3",  elem1 is elem3)
    print("elem1: %r" % elem1)
    print("elem2: %r" % elem2)
    print("elem3: %r" % elem3)
    print("")


def construct(name, cls):
    print("Construimos %s = %s()" % (name, cls.__name__))
    return cls()

def display(cadena, valor):
    print("%-12s: ?    (pulsa ENTER para continuar) " % cadena, end='')
    input()
    print("  %4r" %  valor)

def main():
    ejemplo(A)
    ejemplo(B)
    ejemplo(C)

if __name__ == '__main__':
    main()
