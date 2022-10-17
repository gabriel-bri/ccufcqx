#include <stdio.h>


// Funções conseguem retornar apenas um valor, mas nesse caso precisamos 
// retornar 2, como proceder?

// Definimos o cabeçalho da função que recebe dois inteiros e um ponteiro de inteiro. 
int soma(int a, int b, int *mul);

int main() {
    //Definição da variável mul que receberá o resultado da Multiplicacão
    int mul;
    //Chamada da função soma que armaze o resultado na variável res.
    int res = soma(3, 3, &mul); 
    //Passagem de dois inteiros e o endereço de mul 
    //para receber a operação de multiplicação
    
    //Imprime a multiplicação e a soma.
    printf("Multiplicacao: %d\n", mul);
    printf("Soma: %d\n", res);
    
    return 0;
}

//Definição da função.
int soma(int a, int b, int *mul) {
    //Ponteiro mul recebe a multiplicação dos dois parâmetros.
    *mul = a * b;
    //Armazena a soma dos dois parâmetros
    int soma = a + b;
    //Retorna o valor
    return soma;
}

