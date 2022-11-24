#include <stdio.h>

void tipoTriangulo(int forma, int a, int b, int c);
void verificaPossibilidade(int a, int b, int c);

int main(){
    int a, b, c;
    
    do{
        printf("Digite os três lados em sequência: ");
        scanf("%d", &a);
        scanf("%d", &b);
        scanf("%d", &c);
    } while(a <= 0 || b <= 0 || c <=0);
    
    verificaPossibilidade(a, b, c);
    return 0;
}

void tipoTriangulo(int forma, int a, int b, int c) {
    if(forma) {
        if(a == b && b == c && a == c) {
            printf("Triângulo equilátero");
        }
        
        else if(a != b && b != c && c != a) {
            printf("Triângulo escaleno");
        }
        
        else {
            printf("Triângulo isósceles");
        }
    }
    
    else {
        printf("Não pode formar um triângulo");
    }
}

void verificaPossibilidade(int a, int b, int c) {
    int forma;
    if(a + b > c && b + c > a && c + b > a) {
        //Retorna true
        forma = 1;
        tipoTriangulo(forma, a, b, c);
    }
    
    else {
        //Retorna false
        forma = 0;
        tipoTriangulo(forma, a, b, c);
    }
}
