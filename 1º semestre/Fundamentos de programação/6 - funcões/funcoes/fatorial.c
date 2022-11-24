#include <stdio.h>

int fatorial(int n) {
    int fatorial = 1;
    for(int i = n; i > 0; i--) {
        fatorial *= i;
    }
    
    return fatorial;
}
int main(){
    int numero;
    printf("Digite o número para saber seu fatorial");
    scanf("%d", &numero);
    
    int resultado = fatorial(numero);
    
    printf("O fatorial do número %d é: %d", numero, resultado);
    return 0;
}
