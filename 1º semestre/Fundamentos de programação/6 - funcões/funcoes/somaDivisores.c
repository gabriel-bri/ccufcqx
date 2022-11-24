#include <stdio.h>
int somaDivisores(int n);
int main(){
    int n;
    do{
        printf("Digite um número inteiro positivo");
        scanf("%d", &n);
    } while(n < 0);
    
    int result = somaDivisores(n);
    printf("A soma dos divisores do número %d é igual a: %d", n, result);
    
    
    return 0;
}

int somaDivisores(int n){
    int soma = 0;
    
    for(int i = n; i > 0; i--) {
        if(n % i == 0) {
            soma += i;
        }
    }
    
    return soma;
}
