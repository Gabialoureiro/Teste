#include <stdio.h>
#include <string.h>
#define DIM 50

int main()
{
    char frase[DIM], aux;
    char *p = frase;
    int tam, i;
    gets(frase);
    tam = strlen(frase);
    for(i=strlen(frase)-1;i>=0;i--)
    {
        aux = *(p+i);
        printf("%c", aux );
    }
	return 0;
}
