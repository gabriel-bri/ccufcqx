#include <stdio.h>
int main() {
    
    int numero;
    int fatorial = 1;

    printf("Digite o número para o fatorial:");
    scanf("%d", &numero);    
    for(int i = numero; i >= 1; i--) {
        fatorial *= i;
    }
    
    printf("%d", fatorial);
    
    return 0;
}
