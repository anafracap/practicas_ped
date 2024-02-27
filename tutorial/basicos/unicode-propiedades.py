#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import unicodedata
import unicodedatos

def inform(header, data, adjust=32):
    print("%-*s: %s" % (adjust, header, data))

def getchar(name):
    return unicodedata.lookup(name)

def getprop(caracter, defecto='----'):
    inform("Code point en base 10", ord(caracter))
    res = unicodedata.name(caracter, defecto)
    inform("Nombre", res)
    res = unicodedata.decimal(caracter, defecto)
    inform("Valor decimal", res)
    res = unicodedata.digit(caracter, defecto)
    inform("Dígito", res)
    res = unicodedata.numeric(caracter, defecto)
    inform("Valor en punto flotante", res)
    res = unicodedata.category(caracter)
    inform("Categoría", "%s (%s)" % (res, unicodedatos.cat2[res]))
    inform("Bidireccional", unicodedata.bidirectional(caracter))
    inform("Clase de combinación", unicodedata.combining(caracter))
    inform("Anchura asiática", unicodedata.east_asian_width(caracter))
    inform("Espejado", unicodedata.mirrored(caracter))
    inform("Descomposición", unicodedata.decomposition(caracter))

def getnorm(caracter):
    for form in ('NFC', 'NFD', 'NFKC', 'NFKD'):
        normal = unicodedata.normalize(form, caracter)
        inform("Normalización %s" % form, normal.encode())

def uniencode(caracter):
    encodings = ['ascii', 'iso-8859-1', 'iso-8859-2', 'iso-8859-15', # occidental
                 'iso-8859-5', 'iso-8859-7', 'iso-8859-8', # cirílico / griego / hebreo
                 'cp950', 'big5', 'big5hkscs', 'gb2312', 'gbk', 'gb18030', # chino
                 'hz', 'iso2022_jp_2', # japonés
                 'utf_8', 'utf_8_sig',
                 'utf_16', 'utf_16_be', 'utf_16_le',
                 'utf_32', 'utf_32_be', 'utf_32_le']
    print ("Carácter %s (code point U+%04X) en varias codificaciones" % (caracter.encode(), ord(caracter)))
    print ("*"*70)
    for e in encodings:
        codificado = caracter.encode(e, errors='ignore')
        print('%12s:' % e, end='')
        for c in codificado:
            print(' %02X' % c, end='')
        print('')

def main():
    # caracter = input("Introduzca un carácter Unicode: ")
    ucp = input("Introduzca un code point Unicode: ")
    caracter = chr(int(ucp, 16))
    #caracter = '\u73ab'
    getprop(caracter)
    getnorm(caracter)
    print("Pulse ENTER para continuar... ", end='')
    input()
    uniencode(caracter)
    # mierdin: 1F4A9


if __name__ == '__main__':
    main()
