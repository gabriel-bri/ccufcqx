#include <stdio.h>

int main() {
    int n1, n2, n3, resultado;
    
    scanf("%d %d %d", &n1, &n2, &n3);
    
    resultado = (n1 + n2 + n3) / 3;
    
    printf("%d", resultado);
    
    return 0;
}