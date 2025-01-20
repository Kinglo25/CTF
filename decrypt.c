#include <stdio.h>
#include <string.h>
#include <crypt.h>

int main()
{
    printf("%s\n", crypt("Loic", "$3$$"));
}