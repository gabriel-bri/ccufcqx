#include <stdio.h>

int main(int argc, char** argv) {
  int vetor[4], aux;

  for (int x = 0; x < 4; x++) {
    scanf("%d", &vetor[x]);   
  }
  
  for (int i = 0; i < 4; i++) {

    for(int x = i + 1; x < 4; x++ ){

      if(vetor[i] > vetor[x]) {
        aux = vetor[i];
        vetor[i] = vetor[x];
        vetor[x] = aux;
      }
    
    }
  
  }
  
  printf("%d", vetor[3]);
  
}