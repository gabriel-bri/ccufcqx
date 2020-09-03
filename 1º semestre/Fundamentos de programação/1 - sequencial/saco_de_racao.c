#include <stdio.h>

int main() {
  int gramas_gato, total;
  float peso_saco;

  scanf("%f", &peso_saco);
  scanf("%d", &gramas_gato);

  gramas_gato *= 2;
  gramas_gato *= 5;

  peso_saco *= 1000;

  total = peso_saco - gramas_gato;

  printf("%d", total);
   return 0;
}