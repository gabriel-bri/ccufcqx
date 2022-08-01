#ifndef PROJETO_H
#define PROJETO_H
#include <iostream>

struct Node {
    Node *direita;
    Node *abaixo;
    int linha;
    int coluna;
    double valor;

    Node(int l, int c, int value, Node *right, Node *dwn) {
        direita = right;
        abaixo = dwn;
        linha = l;
        coluna = c;
        valor = value;
    }
};

class Matriz {
private:
    Node *head;
    int Ltam;
    int Ctam;
public:
    //Inicializa uma matriz esparsa vazia com capacidade para m linhas e n colunas.
    Matriz(int m,int n);
    //Destrutor que libera toda a memória que foi alocada dinamicamente para esta estrutura de dados.
    ~Matriz();
    //Checa se as posições passada estão dentro da matriz
    bool naMatriz(int i, int j);
    //Insere um valor na célula (i, j) da matriz, onde i é alinha e j é a coluna.
    void insert(int i,int j,double valor);
    //Devolve o valor na célula (i, j) da matriz, onde i é a linha e j é a coluna.
    double getValue(int i,int j);
    //Devolve a quantidade de linhas da matriz
    int getTamLinhas();
    //Devolve a quantidade de colunas da matriz
    int getTamCols();
    //Devolve um ponteiro para o head da matriz
    Node* getHead();
    //Esse método imprime a matriz A, inclusive os elementos iguais a zero.
    void print();
};
//Se possível somar, retorna uma terceira matriz com o resultado da soma de duas matrizes
Matriz *soma (Matriz* A, Matriz* B);
//Se possível multiplicar, retorna uma terceira matriz com o resultado da multiplicação de duas matrizes
Matriz *multiplica(Matriz*, Matriz*);
//Dado o nome de um arquivo, lê uma matriz desse arquivo
Matriz *lerMatrizDeArquivo(std::string);

#endif
