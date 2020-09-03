#include <stdio.h>

int main(void) {
  int n1, n2, n3, qtd = 0;
  
  scanf("%d %d %d", &n1, &n2, &n3);
  
  if (n1 == n2 && n2 == n3 && n3 == n1 ) {
     qtd = 3;
  }

  else if (n1 != n2 && n2 == n3) {
    qtd = 2;
  }

  else if (n1 == n2 && n2 == n3 && n3 != n1 ){
    qtd = 1;
  }

  else if (n1 != n2 && n3 == n1) {
    qtd = 2;
  }

  else if (n1 == n2 && n3 != n1) {
    qtd = 2;
  }

  else {
    qtd = 0;
  }

  printf("%d", qtd);
  
  return 0;
}