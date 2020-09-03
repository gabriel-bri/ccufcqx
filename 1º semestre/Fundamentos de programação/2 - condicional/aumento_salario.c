#include <stdio.h>

int main() {
    //Variáveis
    float salario, resultado;

    //Leitura	
    scanf("%f", &salario);

	//Se salario <= 1000
    if(salario <= 1000) {
      resultado = (20.0 / 100 * salario);
      salario += resultado;
    }

    else if(salario > 1000 && salario <= 1500) {
      resultado = (15.0 / 100 * salario);
      salario += resultado;
    }

    else if(salario > 1500 && salario <= 2000 ) {
      resultado = (10.0 / 100 * salario);
      salario += resultado;
    }

    else {
      resultado = (5.0 / 100 * salario);
      salario += resultado;
    }

    printf("%.2f", salario);
    
    return 0;
}
