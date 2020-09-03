#include <stdio.h>

int main()
{
    int contador = 0;
    int idade;
    int somaIdades = 0;
    float mediaIdades;
    for(; ;) {
        printf("Digite uma idade (0 para parar): ");
        scanf("%d", &idade);
        somaIdades += idade;
        
        if(idade == 0) {
            break;
        }
        
        contador++;
    }
    
    printf("Foram inseridas %d idades e a soma de idades foi de igual a %d \n", contador, somaIdades);
    mediaIdades = somaIdades / contador;
    printf("A média de idades foi de: %.2f", mediaIdades);

    return 0;
}
