#include <stdio.h>

int main(){
    int tamanhoVetor;
    
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanhoVetor);
    
    int numeros[tamanhoVetor];
    int maior = 0, contador = 0;
    
    for(int i = 0; i < tamanhoVetor; i++) {
        printf("Digite o %d número:", i + 1);
        scanf("%d", &numeros[i]);
        
        if(i == 0) {
            maior = numeros[0];
        }
        
        else {
            if(numeros[i] > maior) {
                maior = numeros[i];
            }            
        }

    }
    
    printf("%d", maior);
    
    for(int i = 0; i < tamanhoVetor; i++) {
        if(numeros[i] == maior){
            contador++;
        }
    }
    
    printf("Existem %d números iguais ao maior valor do vetor!", contador);
    
    return 0;
}
