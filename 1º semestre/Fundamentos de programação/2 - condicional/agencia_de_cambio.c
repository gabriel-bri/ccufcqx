#include <stdio.h>
#include <ctype.h>
int main()
{
    int opcao, valor, resultado;
    // utilizei os seguintes valores de cotação: 5.02, 3.56, 5.54, 6.09

    scanf("%d %d", &opcao, &valor);
    
    switch(opcao) {
        case 1:
            resultado =  valor / 5.02;
            printf("%d", resultado);
        break;
        
        case 2:
            resultado = valor / 3.56;
            printf("%d", resultado);
        break;

        case 3:
            resultado = valor / 5.54;
            printf("%d", resultado);
        break;

        case 4:
            resultado = valor / 6.09;
            printf("%d", resultado);
        break;
    }
    return 0;
}
