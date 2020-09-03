#include <stdio.h>
int main(){
    int mat[6][4];
    int maiornumero;

    printf("Informe os numeros da matriz: \n");
    for(int i=0;i<6;i++){
        for(int j = 0; j < 4; j++){
           printf("Digit o número da posição: [%d][%d]", i, j);
           scanf("%i", &mat[i][j]);
           if(i==0)
                maiornumero = mat[i][j];
           else if(mat[i][j]>maiornumero)
                maiornumero = mat[i][j];
        }
        
        for(int j = 0; j < 6; j++){
            mat[i][j]*=maiornumero;
        }
    }


    printf("A matriz resultante da multiplicacao do maior elemento da linha:\n " ) ; 

    for ( int i = 0; i < 6; i++){
        for( int j = 0; j < 4; j++){
            printf("%i ",mat[i][j]);
        }
        printf("\n");
    }
    return 0;
}