#include <stdio.h>

int main() {
  int n1, n2;
  char op;

  scanf("%d \n", &n1);

  scanf("%d \n", &n2);

  scanf("%c", &op);

  switch(op) {
    case '+':
      printf("%d", n1 + n2);
      break;

    case '-':
      printf("%d", n1 - n2);
      break;

    case '*':
      printf("%d", n1 * n2);
      break;

    case '/':
      if(n2 != 0) {
        printf("%d", n1 / n2);
      }

      else {
        printf("invalida");
      }
      break;
    default:
      printf("invalida");
  }

  return 0;
}