#include <stdio.h>

int main()
{
    float jogador1_chute, valor_real;
    char opcao_jogador2, resposta;
    
    scanf("%f \n %c \n %f", &jogador1_chute, &opcao_jogador2, &valor_real);
    
    if(valor_real > jogador1_chute) {
        resposta = 'M';
    }
    
    else {
        resposta = 'm';
    }
    
    if(jogador1_chute == valor_real || opcao_jogador2 != resposta) {
        printf("primeiro");
    }
    
    else {
        printf("segundo");
    }

    return 0;
}
