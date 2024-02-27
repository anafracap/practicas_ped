! Copyright (C) 2016 rgg (Raul Garcia Garcia)).
! See http://factorcode.org/license.txt for BSD license.
USING: kernel interpolate classes accessors io formatting sequences sequences.generalizations strings math destructors ;
IN: oop

GENERIC: perro>string ( perro -- string )
GENERIC: clase ( perro -- string )
GENERIC: imprimirmsg ( msg perro -- )
GENERIC: imprimir ( perro -- )

TUPLE: perro { nombre string initial: "" } { edad integer initial: 0 } { disposed boolean } ;
! C: <perro> perro
: <perro> ( nombre edad -- perro )
  perro new
    swap >>edad
    swap >>nombre
  dup "inicializador" swap imprimirmsg ;
M: perro clase class-of name>> ;
M: perro perro>string [ clase ] [ nombre>> ] [ edad>> ] tri "%s(%s, %d)" sprintf ;
M: perro imprimirmsg perro>string "${1} ${0}" interpolate nl ;
M: perro imprimir "" swap imprimirmsg ;
M: perro dispose* "finalizador" swap imprimirmsg ;

"inicio" print

"pupi" 17 <perro>
"cuki" 7 <perro>
perro new

imprimir
imprimir
dup imprimir
"yupi" >>nombre imprimir

"lista" print

"pupi" 17 <perro>  "cuki" 7 <perro>  perro new 3 { } nsequence
[ imprimir ] each

"construccion y destruccion" print

"fufi" 2 <perro> [ imprimir ] with-disposal
! [ "interno" 3 <perro> ] [ call [ imprimir with-disposal ] ]

"fin" print
