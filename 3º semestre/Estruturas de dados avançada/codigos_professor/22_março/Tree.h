#ifndef TREE_H
#define TREE_H
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

    // funcoes que executam percursos especificos na arvore
    // imprimindo o valor das chaves na tela
    void preorder();
    void inorder();
    void posorder();
};

#endif 
