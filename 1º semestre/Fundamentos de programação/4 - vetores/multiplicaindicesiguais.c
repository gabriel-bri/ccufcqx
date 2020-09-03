#include <stdio.h>

int main()
{
    int vetor1[10], vetor2[10], mult[10];
    
    for(int i = 0; i < 10; i++) {
        printf("Digite o %d valor da primeira faixa de vetor: ", i);
        scanf("%d", &vetor1[i]);
    }
    
    printf("\n");
    
    for(int i = 0; i < 10; i++) {
        printf("Digite o %d valor da segunda faixa de vetor: ", i);
        scanf("%d", &vetor2[i]);
    }
    printf("\n");
    
    for(int i = 0; i < 10; i++) {
        mult[i] = vetor1[i] * vetor2[i];
        printf("%d\n", mult[i]);
    }
    return 0;
}
