#include <stdio.h>

int main() {
    int jogador1, jogador2, jogador3;
    
    scanf("%d%d%d", &jogador1, &jogador2, &jogador3);
    
    if(jogador1 != jogador2 && jogador1 != jogador3 ) {
        printf("jog1");
    }

    else if (jogador2 != jogador1 && jogador2 != jogador3) {
      printf("jog2");
    }
    
    else if (jogador3 != jogador2 && jogador3 != jogador1) {
      printf("jog3");
    }

    else {
      printf("empate");
    }

    return 0;
}