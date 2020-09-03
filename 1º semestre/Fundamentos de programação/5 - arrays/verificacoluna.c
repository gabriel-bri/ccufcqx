#include <stdio.h>

int main(){
    int mat[4][3];
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 3; j++) {
            printf("Digite o valor da posição [%d][%d]:", i, j);
            scanf("%d", &mat[i][j]);
        }
    }
    
    int eql = 1;
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 3; j++) {
            if(i != 3 && j != 2) {
                if(mat[i][j] == mat[i + 1][j]) {
                    continue;
                }
            
                else{
                    eql = 0;
                    break;
                }
            }
        }
    }
    
    if(eql == 1) {
        printf("Sim");
    }
    
    else {
        printf("Não");
    }
    return 0;
}
