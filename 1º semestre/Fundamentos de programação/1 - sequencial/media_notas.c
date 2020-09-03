#include <stdio.h>

int main() {
    double nota1, nota2, nota3, peso1, peso2, peso3, r1, r2, r3;
    double resultado;
    
    scanf("%lf", &nota1);
    scanf("%lf", &nota2);
    scanf("%lf", &nota3);
    
    scanf("%lf", &peso1);
    scanf("%lf", &peso2);
    scanf("%lf", &peso3);
    
    r1 = nota1 * peso1;
    r2 = nota2 * peso2;
    r3 = nota3 * peso3;
    
    resultado = (r1 + r2 + r3) / (peso1 + peso2 + peso3);
    
    printf("%lf", resultado);
    return 0;
}