#ifndef TREE_H
#define TREE_H
#include <string>
#include <iostream>
#include "Node.h"

class Tree {
private:
    Node *root; // ponteiro para a raiz da arvore

public:
    // Construtor: cria arvore vazia
    Tree(); 

    // Construtor: cria uma arvore com chave key
    // e cujos filhos serao as raizes das arvores tl e tr.
    // tl e tr serao arvores vazias ao final dessa funcao
    Tree(int key, Tree& tl, Tree& tr); 

    Tree(std::string serial); // construtor que recebe um serial de uma arvore

    // funcoes que executam percursos especificos na arvore
    // imprimindo o valor das chaves na tela
    void preorder();
    void inorder();
    void posorder();

    // funcao que diz se a arvore esta vazia
    // retorna true se vazia; false caso contrario
    bool empty();

    // funcao que diz se a arvore contem a chave 'key'
    bool contain(int key);

    // essa funcao deixa a arvore vazia
    void clear();

    // retorna o numero de nos da arvore
    int size();

    ~Tree(); // Destrutor

    // retorna uma string contendo a serializacao da arvore
    std::string serializa();

    // -------------------------------------------------------------
    // Funcoes que foram removidas
    Tree(const Tree& t) = delete; // construtor de copia deletado
    Tree& operator=(const Tree& t) = delete; // operador de atribuicao deletado
};

#endif 
