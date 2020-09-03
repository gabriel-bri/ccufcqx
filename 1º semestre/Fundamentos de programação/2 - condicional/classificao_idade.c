#include <stdio.h>
#include <ctype.h>
int main()
{
    int opcao;
    scanf("%d", &opcao);
    
    opcao = opcao / 10;
    
    switch(opcao) {
        case 0:
            printf("Criança");
        break;

        case 1:
            printf("Adolescente");
        break;

        case 2:
            printf("Adulto jovem");
        break;
        
        case 3:
            printf("Adulto jovem");
        break;
        
        case 4:
            printf("Adulto");
        break;
        
        case 5:
            printf("Adulto");
        break;
        
        default: 
            printf("Melhor idade");
    }
    return 0;
}
