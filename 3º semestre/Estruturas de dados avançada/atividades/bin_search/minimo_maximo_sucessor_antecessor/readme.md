# Atividade
![Caminho](img/arvore.jpg)

No exercício anterior, você implementou as operações de inserção de chaves e de busca em uma árvore binária de busca cujos nós possuem ponteiro para o pai. Estas funções devem ser copiadas neste exercício para que ele funcione também.

Além disso, agora, você terá que implementar outras funções que devem obrigatoriamente serem iterativas (não é permitido usar recursividade para solucionar esse exercício)

Parte das funções já está programada. Você deve implementar apenas as seguintes funções adicionais:

### int BST::minimum();
Esta função pública devolve o menor valor de chave da árvore.
Esta função deve obrigatoriamente ser iterativa. Também não é permitido usar estruturas de dados adicionais nessa função, apenas a árvore e sua estrutura já é suficiente.

### Node *BST::minimum(Node *node);
Função privada que recebe como argumento o ponteiro para a raiz de uma árvore e devolve o ponteiro para o nó com a menor chave na árvore. Se a árvore for vazia, devolve nullptr.
Esta função deve obrigatoriamente ser iterativa. Também não é permitido usar estruturas de dados adicionais nessa função, apenas a árvore e sua estrutura já é suficiente.

### int BST::maximum();
Função pública que devolve o maior valor de chave da árvore.
Esta função deve obrigatoriamente ser iterativa. Também não é permitido usar estruturas de dados adicionais nessa função, apenas a árvore e sua estrutura já é suficiente.

### Node *BST::maximum(Node *node);
Função privada que recebe como argumento o ponteiro para a raiz de uma árvore e devolve o ponteiro para o nó com a maior chave na árvore. Se a árvore for vazia, devolve nullptr.
Esta função deve obrigatoriamente ser iterativa. Também não é permitido usar estruturas de dados adicionais nessa função, apenas a árvore e sua estrutura já é suficiente.

### int BST::successor(int k);
Função pública que recebe um inteiro k como argumento e: (1) devolve INT_MAX se a chave k não estiver presente na árvore ou se k estiver presente na árvore mas não tem sucessor; ou (2) caso contrário, devolve o valor da chave sucessora de k quando esta existe.
Esta função deve obrigatoriamente ser iterativa. Também não é permitido usar estruturas de dados adicionais nessa função, apenas a árvore e sua estrutura já é suficiente.

### Node *BST::successor(Node *node);
Função privada que Recebe um ponteiro para um Node e: (1) devolve nullptr quando node não tem sucessor; ou (2) caso contrário, devolve o ponteiro para o no sucessor de node. 
Esta função deve obrigatoriamente ser iterativa. Também não é permitido usar estruturas de dados adicionais nessa função, apenas a árvore e sua estrutura já é suficiente.
 

### int BST::predecessor(int k);
Função pública que recebe um inteiro k como argumento e: (1) devolve INT_MIN se a chave k não estiver presente na árvore ou se k estiver presente na árvore mas não tem antecessor; ou (2) caso contrario, devolve o valor inteiro da chave antecessora de k quando esta existir. Esta função deve obrigatoriamente ser iterativa. Também não é permitido usar estruturas de dados adicionais nessa função, apenas a árvore e sua estrutura já é suficiente.

### Node *BST::predecessor(Node *node);
Função privada que recebe um ponteiro para um Node e: (1) devolve nullptr quando node não tem antecessor; ou (2) caso contrário, devolve o ponteiro para o nó antecessor de node. Esta função deve obrigatoriamente ser iterativa. Também não é permitido usar estruturas de dados adicionais nessa função, apenas a árvore e sua estrutura já é suficiente.
 

# Ajuda

A atividade já vem com um código implementado para você seguir como ponto de partida.

O método bshow da árvore imprime a árvore em um formato amigável. Você pode utilizá-lo para conferir se seu código está funcionando corretamente.

Os locais onde você deve colocar seu código estão marcados com //TODO. 

### Exemplo de Entrada:

<pre>
<code>
34 56 9 3 99 123 6 18 34 32 77 55 66 90 81 22 47 68 83
66
</code>
</pre>

### Exemplo de Saída:

<pre>
<code>
minimo: 3
maximo: 123
antecessor(66) = 56
sucessor(66) = 68
Node removed: 6
Node removed: 3
Node removed: 22
Node removed: 32
Node removed: 18
Node removed: 9
Node removed: 47
Node removed: 55
Node removed: 68
Node removed: 66
Node removed: 83
Node removed: 81
Node removed: 90
Node removed: 77
Node removed: 123
Node removed: 99
Node removed: 56
Node removed: 34
</code>
</pre>



## Arquivos requeridos

#### main.cpp
<pre>
<code>
#include <iostream>
#include <string>
#include <climits>
#include <sstream>
#include "bst.h"
using namespace std;

int main()
{
    BST arv;
    string skeys;
    
    getline(cin, skeys); // read a string containing all keys separated by spaces

    stringstream ss { skeys };
    int value;

    while(ss >> value) {
        arv.add(value);
    }

    int v;
    cin >> v;

    cout << "minimo: " << arv.minimum() << endl;
    cout << "maximo: " << arv.maximum() << endl;

    int pred = arv.predecessor(v);
    if(pred == INT_MIN)
        cout << v << " nao tem antecessor ou nao esta na arvore" << endl;
    else 
        cout << "antecessor(" << v << ") = " << pred << endl;

    int succ = arv.successor(v);
    if(succ == INT_MAX)
        cout << v << " nao tem sucessor ou nao esta na arvore" << endl;
    else 
        cout << "sucessor(" << v << ") = " << succ << endl;

    return 0;
}
</code>
</pre>

### bst.h
<pre>
<code>
#ifndef BST_H
#define BST_H
#include <iostream>
#include <string>
#include <stack>
#include <climits>
using namespace std;

/*****************************
 * Definicao do struct Node
 *****************************/
struct Node {
    int key;
    Node *left;
    Node *right;
    Node *parent;

    // Construtor
    Node(int k, Node* l = nullptr, Node* r = nullptr, Node* p = nullptr) {
        this->key = k;
        this->left = l;
        this->right = r;
        this->parent = p;
    }
    // Destrutor
    ~Node() {
        cout << "Node removed: " << this->key << endl;
    }
};

/************************
 * Declaracao da classe
 ************************/
class BST {
public:
    BST();
    BST(int k);
    void bshow();
    bool add(int k);
    int minimum();           // ---> Implementar
    int maximum();           // ---> Implementar
    int predecessor(int k);  // ---> Implementar
    int successor(int k);    // ---> Implementar
    ~BST();
private:
    Node *root;
    void bshow(Node *node, std::string heranca);
    Node *minimum(Node *node);       // ---> Implementar
    Node *maximum(Node *node);       // ---> Implementar
    Node *successor(Node *node);     // ---> Implementar
    Node *predecessor(Node *node);     // ---> Implementar
    Node *clear(Node *node);
    Node *search(int k);
};

/*****************************
 * Implementacao da classe
 *****************************/
// Construtor 
BST::BST() {
    root = nullptr;
}

// Construtor 
BST::BST(int k) {
    root = new Node(k);
}

void BST::bshow(){
    bshow(root, "");
}

void BST::bshow(Node *node, std::string heranca) {
    if(node != nullptr && (node->left != nullptr || node->right != nullptr))
        bshow(node->right , heranca + "r");
    for(int i = 0; i < (int) heranca.size() - 1; i++)
        std::cout << (heranca[i] != heranca[i + 1] ? "│   " : "    ");
    if(heranca != "")
        std::cout << (heranca.back() == 'r' ? "┌───" : "└───");
    if(node == nullptr){
        std::cout << "#" << std::endl;
        return;
    }
    std::cout << node->key << std::endl;
    if(node != nullptr && (node->left != nullptr || node->right != nullptr))
        bshow(node->left, heranca + "l");
}

Node *BST::clear(Node *node) {
    if(node != nullptr) {
        node->left = clear(node->left);
        node->right = clear(node->right);
        delete node;
    }
    return nullptr;
}

BST::~BST() {
    root = clear(root);
}

// Funcao publica 'add'
// Esta funcao deve obrigatoriamente ser iterativa.
// Esta funcao adiciona um no com chave k na arvore e: 
// (1) devolve true em caso de sucesso;
// (2) devolve false caso contrario.
// Lembre-se que nao podem haver chaves repetidas na nossa arvore.
bool BST::add(int k) {
    //TODO: adicione aqui o codigo feito no exercicio anterior
}

// Funcao privada 'search'
// Esta funcao devolve o ponteiro para o no que 
// contem a chave k se ela existir na arvore;
// caso contrario, devolve nullptr;
Node *BST::search(int k) {
    //TODO: adicione aqui o codigo feito no exercicio anterior
}

// Funcao publica (obrigatoriamente iterativa)
// Devolve o menor valor de chave da arvore.
int BST::minimum() {
    // TODO
}

// Funcao privada (obrigatoriamente iterativa)
// Recebe como argumento o ponteiro para a raiz de uma arvore
// e devolve o ponteiro para o no com a menor chave na arvore.
// Se a arvore for vazia, devolve nullptr
Node *BST::minimum(Node *node) {
    // TODO
}

// Funcao publica (obrigatoriamente iterativa)
// Devolve o maior valor de chave da arvore
int BST::maximum() {
    // TODO
}

// Funcao privada (obrigatoriamente iterativa)
// Recebe como argumento o ponteiro para a raiz de uma arvore
// e devolve o ponteiro para o no com a maior chave na arvore.
// Se a arvore for vazia, devolve nullptr
Node *BST::maximum(Node *node) {
    // TODO
}

// Funcao publica (obrigatoriamente iterativa)
// Recebe um inteiro k como argumento e:
// (1) devolve INT_MAX se a chave k nao esta presente na arvore ou 
// se k esta presente na arvore mas nao tem sucessor
// (2) caso contrario, devolve o valor inteiro da 
// chave sucessora de k quando esta existe
int BST::successor(int k) {
    // TODO
}

// Funcao privada (obrigatoriamente iterativa)
// Recebe um ponteiro para um Node e:
// (1) devolve nullptr quando node nao tem sucessor; ou
// (2) caso contrario, devolve o ponteiro para o no sucessor de node.
Node *BST::successor(Node *node) {
    // TODO
}

// Funcao publica (obrigatoriamente iterativa)
// Recebe um inteiro k como argumento e:
// (1) devolve INT_MIN se a chave k nao esta presente na arvore ou 
// se k esta presente na arvore mas nao tem antecessor;
// (2) caso contrario, devolve o valor inteiro da chave 
// antecessora de k quando esta existe.
int BST::predecessor(int k) {
    // TODO
}

// Funcao privada (obrigatoriamente iterativa)
// Recebe um ponteiro para um Node e:
// (1) devolve nullptr quando node nao tem antecessor; ou
// (2) caso contrario, devolve o ponteiro para o no antecessor de node.
Node *BST::predecessor(Node *node) {
    // TODO
}

#endif  
</code>
</pre>