! Copyright (C) 2016 rgg (Raul Garcia Garcia)).
! See http://factorcode.org/license.txt for BSD license.
USING: kernel interpolate classes accessors io formatting sequences sequences.generalizations ;
IN: oop

: clase ( obj -- string ) class-of name>> ;

GENERIC: hazruido ( animal -- ruido )
GENERIC: dametamano ( animal -- tamano )
GENERIC: + ( animal animal -- suma )

TUPLE: animal ;
C: <animal> animal
M: animal hazruido drop "ruido animal" ;
M: animal dametamano drop 0 ;
! M: animal + [ hazruido ] bi@ "yo:${0} otro:${1}" interpolate>string ;
M: animal + [ clase ] [ hazruido ] bi* "yo:${0} otro:${1}" interpolate>string ;

TUPLE: perro < animal ;
: <perro> ( -- perro ) perro new ;
M: perro hazruido drop "guau" ;
M: perro dametamano drop 10 ;

TUPLE: gato < animal ;
M: gato hazruido drop "miau" ;
M: gato dametamano drop 4 ;

TUPLE: doberman < perro ;
M: doberman hazruido drop "grrrrr" ;
M: doberman dametamano drop 20 ;

: ver-bicho ( animal -- ) [ clase ] [ hazruido ] [ dametamano ] tri "%12s: %s(%s)" printf nl ;

"inicio" print

<animal> ver-bicho
perro new ver-bicho
gato new ver-bicho
doberman new ver-bicho

"lista" print

<animal>  perro new  gato new  doberman new  4 { } nsequence
[ ver-bicho ] each

"sobrecarga" print

<animal> [ clase ] [ 34 swap + ] [ 4.2 swap + ] tri "%12s: %s y %s" printf nl
doberman new [ clase ] [ 34 swap + ] [ 4.2 swap + ] tri "%12s: %s y %s" printf nl

"fin" print
