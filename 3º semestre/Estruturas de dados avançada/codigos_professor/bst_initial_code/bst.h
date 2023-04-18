#ifndef BST_H
#define BST_H
#include <iostream>
#include "node.h"

class BST { 
public:
    BST() = default;                        // Construtor default
    BST(const BST& t) = delete;             // Construtor de copia removido
    BST& operator=(const BST& t) = delete;  // Operador de atribuicao removido
    ~BST();                                 // Destrutor
    void add(int key);                      // Adicionar chave 
    void remove(int key);                   // Remover chave
    bool contains(int key);                 // A arvore contem esta chave?
    int minimum();                          // Devolve chave minima
    int maximum();                          // Devolve chave maxima
    int successor(int k);                   // Devolve chave sucessora de k
    int predecessor(int k);                 // Devolve chave antecessora de k
    void inorder();                         // Imprime as chaves em ordem simetrica

private:
    // Atributo privado
    Node *root {nullptr};

    // Funcoes-membro privadas
    Node *add(Node *node, int key);
    Node *search(Node *node, int key);
    Node *clear(Node *node);
    Node *minimum(Node *node);
    Node *maximum(Node *node);
    Node *ancestral_sucessor(Node *x, Node *raiz);
    Node *ancestral_predecessor(Node *x, Node* raiz);
    Node *sucessor(Node *x, Node *raiz);
    Node *predecessor(Node *x, Node* raiz);
    Node *remove(int k, Node *node);
    Node *removeRoot(Node *node);
    void inorder(Node *node);
};

#endif
