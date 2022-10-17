#include <stdio.h>

int main() {
    
    int a = -1;
    int b = 50;
    
    //Se a < 0 então b == 50 não é avaliado.
    if(a > 0 && b == 50) {
        printf("Avaliação com curto circuito.");
    }
    
    //Força para que as duas condições sejam verificadas.
    if(a > 0 & b == 50) {
        printf("Avaliação sem curto circuito.");        
    }
    
    return 0;
}
