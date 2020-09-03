#include <stdio.h>
int main() {
    
    int numero;
    int qtdPares = 0;
    int totPrimos = 0;
    int soma = 0;
    
    for(int i = 1; i <= 10; i++) {
        printf("Digite o %d número:", i);
        scanf("%d", &numero);
        
        if(numero % 2 == 0) {
            qtdPares++;
        }
        
        int c = 1;
        
		while(c <= numero) {
            if(numero % c == 0) {
                soma++;
            }
            
            c++;
        }
        
        if(soma == 2) {
            totPrimos++;
        }
        
        soma = 0;
    }
    
    printf("Tivemos um total de %d números pares \n", qtdPares);
    printf("E tivemos um total de %d números primos", totPrimos);
    return 0;
}
