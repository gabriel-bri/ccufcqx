#include <stdio.h>

int main(void) {
  int num = 0, impar[10], par[10];
  int parNum = 0, imparNum = 0;

  for(int i = 0; i < 10; i++) {
    printf("Digite o numero da posicao %d> ", i);
    scanf("%d", &num);

    if(num % 2 == 0) {
      par[parNum] = num;
      parNum++;
    } else {
      impar[imparNum] = num;
      imparNum++;
    }
  }

  printf("Imprimindo números pares \r\n");
  for(int i = 0; i < parNum; i++) {
    i == 0 ? : printf("-");
    printf("%d", par[i]);
  }

  printf("\r\n");

  printf("Imprimindo números ímpares \r\n");
  for(int i = 0; i < imparNum; i++) {
    i == 0 ? : printf("-");
    printf("%d", impar[i]);
  }
}
