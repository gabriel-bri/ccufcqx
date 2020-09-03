#include <stdio.h>
#include <math.h>
#include <stdlib.h>


int main() {
    int valor_produto, chute1, chute2, diferenca1, diferenca2;
    
    scanf("%d", &valor_produto);
    scanf("%d", &chute1);
    scanf("%d", &chute2);
    
    diferenca1 = abs(valor_produto - chute1);
    diferenca2 = abs(valor_produto - chute2);

    
    if (diferenca1 < diferenca2) {
        printf("primeiro");
    }
    
    else if(diferenca1 == diferenca2) {
        printf("empate");
    }
    
    else {
        printf("segundo");
    }
	
  return 0;
}