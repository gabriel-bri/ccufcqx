#include <stdio.h>

int main() {
  int preco_fabrica, PercentualLucroDistribuidor;
  int PercentualImposto, impostos, lucro, total;
  double outra_variavel, outra_variavel_lucro;

  scanf("%d", &preco_fabrica);

  scanf("%d", &PercentualLucroDistribuidor);

  scanf("%d", &PercentualImposto);

  outra_variavel_lucro = PercentualLucroDistribuidor;
  lucro = (outra_variavel_lucro / 100 * preco_fabrica);
  printf("%d ", lucro);
  
  outra_variavel = PercentualImposto;
  impostos =  (outra_variavel / 100 * preco_fabrica) ;
  printf("%d ", impostos);

  total = preco_fabrica - (impostos + lucro);
  printf("%d ", total);
  
  //com gambiarra se resolve tudo :)
}