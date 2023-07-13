# Atividade
![Caminho](img/arvore.jpg)

Nos exercícios anteriores, você implementou as operações de inserção de chaves, de busca, mínimo, máximo, antecessor e sucessor  em uma árvore binária de busca cujos nós possuem ponteiro para o pai. 

Além disso, agora, você terá que implementar outras funções que devem obrigatoriamente serem iterativas (não é permitido usar recursividade para solucionar esse exercício)

Parte das funções já está programada. Você deve implementar apenas as seguintes funções adicionais:


### void BST::preorder();
Função pública. Percorre os nós da árvore em pre-ordem imprimindo os valores das chaves. Dica: use a estrutura de dados pilha (stack).

### void BST::inorder();
Função pública. Percorre os nós da árvore em ordem simétrica imprimindo os valores das chaves. Dica: use a estrutura de dados pilha (stack).

### void BST::clear();
Função pública que libera todos os nós da árvore deixando ela vazia. Dica: use a estrutura de dados pilha (stack).

# Ajuda

A atividade já vem com um código implementado para você seguir como ponto de partida.

O método bshow da árvore imprime a árvore em um formato amigável. Você pode utilizá-lo para conferir se seu código está funcionando corretamente.

Os locais onde você deve colocar seu código estão marcados com //TODO. 

### Exemplo de Entrada:

<pre>
<code>
1 2 3 4 5 6 7
23 45 67 21 34 89 77 45
</code>
</pre>

### Exemplo de Saída:

<pre>
<code>
inorder: 1 2 3 4 5 6 7
preorder: 1 2 3 4 5 6 7
Node removed: 1
Node removed: 2
Node removed: 3
Node removed: 4
Node removed: 5
Node removed: 6
Node removed: 7
inorder: 21 23 34 45 67 77 89
preorder: 23 21 45 34 67 89 77
Node removed: 21
Node removed: 23
Node removed: 34
Node removed: 45
Node removed: 67
Node removed: 77
Node removed: 89
</code>
</pre>



## Arquivos requeridos

#### main.cpp
<pre>
<code>
#include <iostream>
#include <string>
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

    cout << "inorder: ";
    arv.inorder();
    cout << endl;
    cout << "preorder: ";
    arv.preorder();
    cout << endl;

    arv.clear();

    skeys.clear();
    getline(cin, skeys);
    stringstream sss { skeys };

    while(sss >> value) {
        arv.add(value);
    }

    cout << "inorder: ";
    arv.inorder();
    cout << endl;
    cout << "preorder: ";
    arv.preorder();
    cout << endl;

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
using namespace std;

/******************************
 * Definicao do struct Node
 ******************************/
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

/***********************************
 * Declaracao da classe
 ***********************************/
class BST {
public:
    BST();
    BST(int k);
    void bshow();
    bool add(int k);
    void preorder();  // --> Implementar
    void inorder();   // --> Implementar
    void clear();     // --> Implementar
    ~BST();
private:
    Node *root;
    void bshow(Node *node, std::string heranca);
};

/***********************************
 * Implementacao da classe
 ***********************************/
BST::BST() {
    root = nullptr;
}
 
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

BST::~BST() {
    clear();
}

// Funcao publica 'add'
// Esta funcao deve obrigatoriamente ser iterativa.
// Esta funcao adiciona um no com chave k na arvore e: 
// (1) devolve true em caso de sucesso;
// (2) devolve false caso contrario.
// Lembre-se que nao podem haver chaves repetidas na nossa arvore.
bool BST::add(int k) {
    //TODO: adicione aqui o codigo feito no primeiro exercicio
}

// Funcao publica 'preorder'
// Percorre os nos da arvore em pre-ordem imprimindo os 
// valores das chaves. Dica: use a estrutura de dados pilha (stack)
void BST::preorder() {
    // TODO
}

// Funcao publica 'inorder'
// Percorre os nos da arvore em ordem simetrica imprimindo os 
// valores das chaves. Dica: use a estrutura de dados pilha (stack)
void BST::inorder() {
    // TODO
}

// Funcao publica 'clear'
// Libera todos os nos da arvore deixando ela vazia.
// Dica: use a estrutura de dados pilha (stack)
void BST::clear() {
    // TODO
}

#endif 
</code>
</pre>