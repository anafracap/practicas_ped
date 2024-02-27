#include <stdio.h>

//assumes little endian
void printBits(size_t const size, void const * const ptr)
{
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    for (i=size-1;i>=0;i--)
    {
        for (j=7;j>=0;j--)
        {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
        printf(" ");
    }
    puts("");
}


void numeros(int valor)
{
    short s = valor;
    int i = valor;
    unsigned int u = valor;
    long l = valor;
    float r = valor;
    double d = valor;
    float *c = (float *)(&i);

    printf("short      (% 2d bytes) % 10d -> ", sizeof s, s);
    printBits(sizeof s, &s);
    printf("int        (% 2d bytes) % 10d -> ", sizeof i, i);
    printBits(sizeof i, &i);
    printf("unsigned   (% 2d bytes) % 10d -> ", sizeof u, u);
    printBits(sizeof u, &u);
    printf("float      (% 2d bytes) % 10f -> ", sizeof r, r);
    printBits(sizeof r, &r);
    printf("float CAST (% 2d bytes) % 10f -> ", sizeof r, *c);
    printBits(sizeof r, c);
    printf("long       (% 2d bytes) % 10d -> ", sizeof l, l);
    printBits(sizeof l, &l);
    printf("double     (% 2d bytes) % 10g -> ", sizeof d, d);
    printBits(sizeof d, &d);
    puts("");
}

int main()
{
    /*
    numeros(1);
    numeros(-1);
    numeros(0);
    */
    int i = 36;
    int b = 0;
    char *c = (char *)&i;
    char s[4];

    sprintf(s, "%d", i);

    printf("integer %d, cast %s, conversion %s.\n", i, c, s);

    return 0;
}

