#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from decimal import Decimal, getcontext

def display(cadena, valor):
    print("%-12s: ?    (pulsa ENTER para continuar) " % cadena, end='')
    input()
    print("  %4r\n" %  valor)

def ieee754():
    cerouno  = 0.1
    cerodos  = 0.2
    cerotres = 0.3
    calculo("IEEE 754", cerouno, cerodos, cerotres)

def decimal_mal():
    cerouno  = Decimal(0.1)
    cerodos  = Decimal(0.2)
    cerotres = Decimal(0.3)
    calculo("Decimal", cerouno, cerodos, cerotres)

def decimal_bien():
    cerouno  = Decimal('0.1')
    cerodos  = Decimal('0.2')
    cerotres = Decimal('0.3')
    calculo("Decimal OK", cerouno, cerodos, cerotres)

def decimal_precision():
    print(getcontext())
    getcontext().prec = 4
    cerouno  = Decimal(0.1)
    cerodos  = Decimal(0.2)
    cerotres = Decimal(0.3)
    calculo("Decimal con precision", cerouno, cerodos, cerotres)

def calculo(titulo, cerouno, cerodos, cerotres):
    print("\nCálculo con %s:" % titulo)
    display("0.1+0.1",            cerouno+cerouno)
    display("0.1+0.2",            cerouno+cerodos)
    display("0.3-0.2",            cerotres-cerodos)
    display("0.1+0.2-0.1-0.2",    cerouno+cerodos-cerouno-cerodos)


def main():
    ieee754()
    decimal_mal()
    decimal_bien()
    decimal_precision()


if __name__ == '__main__':
    main()
