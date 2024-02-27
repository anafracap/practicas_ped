#include <stdio.h>

void display(char str[], int* valor)
{
    fprintf(stdout, "%-12s: ?    (pulsa ENTER para continuar) ", str);
    char c[2];
    fgets(c, 2, stdin);
    fprintf(stdout, "  %4d <0x%010x>\n\n", *valor, valor);
}

void punteros()
{
    int tabla[3] = {32, 23, 33};
    int valor = 30;

    fprintf(stdout, "int tabla[3] = {32, 23, 33};\n");
    fprintf(stdout, "int valor = 30;\n");
    display("tabla[0]",     & tabla[0]);
    display("tabla[1]",     & tabla[1]);
    display("tabla[2]",     & tabla[2]);
    display("tabla[3]",     & tabla[3]);
    display("*(tabla+2)",   & *(tabla+2));
    display("*(2+tabla)",   & *(2+tabla));
    display("2[tabla]",     & 2[tabla]);

    tabla[2] = 10;
    display("tabla[2] = 10;   tabla[2]",     & tabla[2]);
    *(tabla+2) = 14;
    display("*(tabla+2) = 14; tabla[2]",     & tabla[2]);
}

int main(int argc, char* argv[])
{
    punteros();
    return 0;
}
