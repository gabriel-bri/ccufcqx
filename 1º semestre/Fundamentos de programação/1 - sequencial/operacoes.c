#include <stdio.h>

 int main () {
  
int soma, divisao, subtracao, multiplicacao, n1, n2;
  
 
scanf ("%d %d", &n1, &n2);
  
 
soma = n1 + n2;
  
 
subtracao = n1 - n2;
  
 
divisao = n1 / n2;
  
 
multiplicacao = n1 * n2;
  
 
printf ("%d", soma);
printf (" %d", subtracao);
printf (" %d", multiplicacao);
printf (" %d", divisao);

// printf(" %d %d %d %d ", soma, subtracao, divisao, multiplicacao);
  
return 0;

}