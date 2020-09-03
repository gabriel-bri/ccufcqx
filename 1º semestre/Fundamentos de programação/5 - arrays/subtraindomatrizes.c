#include <stdio.h>
#include <unistd.h>

int main(){
    int totLinhas, totColunas;
    printf("Digite o mesmo número de linhas e colunas\n");
    sleep(3);
    
    do {
        printf("Digite o número de linhas: ");
        scanf("%d", &totLinhas);
        
        printf("Digite o número de colunas: ");
        scanf("%d", &totColunas);
    } while(totLinhas != totColunas);
    
    int n[totLinhas][totColunas];
    int n1[totLinhas][totColunas];
    int sub[totLinhas][totColunas];
    
    for(int i = 0; i < totLinhas; i++) {
        for(int j = 0; j < totColunas; j++) {
            printf("Digite o número da posição [%d] [%d] do primeiro conjunto", i, j);
            scanf("%d", &n[i][j]);
        }   
    }
    
    for(int i = 0; i < totLinhas; i++) {
        for(int j = 0; j < totColunas; j++) {
            printf("Digite o número da posição [%d] [%d] do segundo conjunto", i, j);
            scanf("%d", &n1[i][j]);
        }   
    }
    
    for(int i = 0; i < totLinhas; i++) {
        for(int j = 0; j < totColunas; j++) {
           sub[i][j] = n[i][j] - n1[i][j];
           
           printf("%d - %d = %d\n", n[i][j], n1[i][j], sub[i][j]);
        }
    }
    return 0;
}
