#include <stdio.h>

int main(){
    
    int numLinhas, numColunas;
    
    printf("Digite o números de linhas: ");
    scanf("%d", &numLinhas);
    
    printf("Digite o números de colunas: ");
    scanf("%d", &numColunas);
    
    int n[numLinhas][numColunas], soma = 0, cont = 0;
    
    for(int i = 0; i < numLinhas; i++) {
        for(int j = 0; j < numColunas; j++) {
            printf("Digite os números da posição [%d][%d]", i, j);
            scanf("%d", &n[i][j]);
            soma += n[i][j];
            cont++;
        }
    }
    
    int media = soma / cont;
    int contaIgual = 0;
    for(int i = 0; i < numLinhas; i++) {
        for(int j = 0; j < numColunas; j++) {
            if(n[i][j] == media) {
                contaIgual++;
            }
        }
    }
    
    printf("Existem %d iguais a média de %d", contaIgual, media);
    
    
    return 0;
}
