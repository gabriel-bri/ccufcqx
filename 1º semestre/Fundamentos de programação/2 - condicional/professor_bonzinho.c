#include <stdio.h>

int main(void) {
  
  float nota1, nota2, nota3, nota_trabalho, media;
  scanf("%f \n %f \n %f \n %f", &nota1, &nota2, &nota3, &nota_trabalho);

  if(nota1 <= nota2 && nota2 <= nota3) {
    media = (nota2 + nota3 + nota_trabalho) / 3;
  }

  else if (nota2 <= nota1 && nota1 <= nota3){
    media = (nota1 + nota3 + nota_trabalho) / 3;
  }

  else if (nota3 <= nota2 && nota3 <= nota1){
    media = (nota2 + nota1 + nota_trabalho) / 3;
  }

  if (media >= 7) {
    printf("Aprovado com %.1f", media);
  }

  else {
    printf("Final com %.1f", media);
  }
  
  return 0;
}