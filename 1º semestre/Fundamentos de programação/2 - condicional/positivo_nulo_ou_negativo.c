#include <stdio.h>

int main(void) {
  
  int numero;
  scanf("%d", &numero);

  if(numero < 0) {
    printf("negativo");
  }

  else if(numero > 0) {
    printf("positivo");
  }

  else {
    printf("nulo");
  }
  return 0;
}