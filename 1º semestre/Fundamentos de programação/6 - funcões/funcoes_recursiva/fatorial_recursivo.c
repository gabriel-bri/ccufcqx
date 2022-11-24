
#include <stdio.h>

int fatorial(int x){
    int resultado;

    if( x == 0){
       resultado = 1;
    } 
    
    else{
        resultado = x * fatorial (x - 1);  
    }
    
    return resultado;
}

int main(){
    int q;
    do{
        
        printf("Digite um número inteiro: ");
        scanf("%d", &q);
        
    }while(q < 0);
    
    int resultado = fatorial(q);
    printf("\nO fatorial de %d é igual a %d", q, resultado);
    return 0;
}
