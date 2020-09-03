#include <stdio.h>

int main(void) {
  char opcao, resultado;

  int n1, n2;

  scanf("%c \n %d \n %d", &opcao, &n1, &n2);

  if(opcao == 'p') {
    resultado = n1 + n2;

    if(resultado % 2 == 0) {
      printf("Venceu");
    }

    else {
      printf("Perdeu");
    }
  }

  else {
    resultado = n1 + n2;
    
    if(resultado % 2 == 1) {
      printf("Venceu");
    }

    else {
      printf("Perdeu");
    }

  }

  return 0;
}