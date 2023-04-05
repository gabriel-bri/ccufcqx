# Descrição

Durante as aulas, estudamos a estrutura de dados árvore binária generalizada (uma árvore em que as chaves dos nós não tem nenhuma relação de ordem entre si) e

vimos a implementação das funções mais básicas que podem ser realizadas nesta estrutura de dados.

As árvores binárias podem ser representadas como uma string por meio da serialização dos valores de suas chaves.

A  **serialização**  é um processo pelo qual percorremos a árvore em pré-ordem e adicionamos o valor de cada chave encontrada ao

final de uma string que inicialmente começa vazia, sendo que, para cada filho nulo encontrado, seu valor é representado pelo caractere '#'.

Por exemplo, logo abaixo mostramos o desenho de uma árvore e depois a string obtida pela serialização de suas chaves:

A serialização da árvore acima consiste na string:

**8 3 1 # # 6 4 # # 7 # # 10 # 14 13 # # #**

Para entender melhor o conceito de serialização de uma árvore binária e ver outros exemplos

de árvores e sua serialização, você pode acessar esse link: [https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/](https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/)

Nesta atividade, a árvore é construída através de uma string de serialização.

**Isso já está codificado. Você não precisa implementar.**

# Atividade

Para esta atividade, é pedido que você incremente a implementação desta estrutura, implementando as seguintes funções adicionais:

**1. Escreva uma função que calcule a altura uma árvore binária.**

A sua função deve ser recursiva e deve ter o seguinte protótipo:

int _height(Node *node);

**2. Escreva uma função que calcule o número de nós de uma árvore binária.**

A sua função deve ser recursiva e deve ter o seguinte protótipo:

int _size(Node *node);

**Observação:**  Suas funções privadas devem ser recursivas e não é permitido usar variáveis globais nestas atividades.

Exercícios resolvidos com variáveis globais receberão nota ZERO.

## Ajuda

A atividade já vem com um código implementado para você seguir como ponto de partida.

O método `bshow` da árvore imprime a árvore em um formato amigável. Você pode utilizá-lo para conferir se seu código está funcionando corretamente.

Para o caso da árvore abaixo, temos essa saída.

```
//serial
1 8 7 # # 4 # 6 # # 5 0 # # 9 # 3 2 # # #

//bshow()
```
Para simplificar o código, estou utilizando a convenção `_` para expressar quais são os métodos privados.

Os locais onde você deve colocar seu código estão marcados com //TODO. Como estamos lidando com árvores,

você deverá criar também os métodos recursivos privados e os métodos públicos.

## Testes

```
>>>>>>>> um
4 # # 
========
1 1
<<<<<<<<

>>>>>>>> dois
1 # 0 # # 
========
2 2
<<<<<<<<

>>>>>>>> tres
4 # 8 2 # # 3 # # 
========
3 4
<<<<<<<<

>>>>>>>> quatro
0 9 4 # # # 5 # # 
========
3 4
<<<<<<<<

>>>>>>>> cinco
0 4 # # 2 0 # # 3 # # 
========
3 5
<<<<<<<<

>>>>>>>> seis
2 0 0 # # # 3 # 7 # 9 # # 
========
4 6
<<<<<<<<

>>>>>>>> dez
1 8 7 # # 4 # 6 # # 5 0 # # 9 # 3 2 # # # 
========
5 10
<<<<<<<<
```

```
>>>>>>>> zero
# # 
========
0 0
<<<<<<<<
```
## Arquivos requeridos

#### main.cpp

<pre>
<code>
#include <iostream>
#include <string>
#include "Tree.h"
using namespace std;

int main(){
	string line;
    getline(cin, line);
    Tree bt(line);
    cout << bt.height() << " " << bt.size() << endl;
    return 0;
}
</code>
</pre>

####  Tree.h

<pre>
<code>
#ifndef TREE_H
#define TREE_H
#include <string>
#include <sstream>

struct Node;

class Tree {
public:
    Tree(std::string serial);
    void inorder();   // percurso em ordem simetrica
    void bshow();     // exibe a arvore de forma amigavel
    int size();
    int height();
    ~Tree();
private:
    Node *_root;
    Node *_clear(Node *root);
    void _inorder(Node *node);
    void _bshow(Node *node, std::string heranca);
    void _serializeTree(std::stringstream& ss, Node **node);
    int _size(Node *node);
    int _height(Node *node);
};

#endif
</code>
</pre>

####  Tree.cpp

<pre>
<code>
#include <iostream>
#include <sstream>
#include <string>
#include "Tree.h"

// Definicao do struct Node
// Em C++ os structs podem ter funcoes-membro, como 
// construtores, destrutores, etc.
struct Node {
    int key;
    Node *left;
    Node *right;

    Node(int k, Node *l = nullptr, Node *r = nullptr) {
        this->key = k;
        this->left = l;
        this->right = r;
    }
};

// Construtor
Tree::Tree(std::string serial) {
    _root = nullptr;
    std::stringstream ss(serial);
    _serializeTree(ss, &_root);
}

// Essa funcao recursiva recebe como entrada uma string contendo 
// uma versao serializada da arvore e recebe um ponteiro para ponteiro para o no raiz.
// A funcao ler os dados e constroi a arvore seguindo um percurso em pre-ordem.
void Tree::_serializeTree(std::stringstream& ss, Node **node) {
    std::string value;
    ss >> value;
    if(value == "#") // filho == nullptr
        return;
    int key = std::stoi(value);
    *node = new Node(key);
    _serializeTree(ss, &((*node)->left));
    _serializeTree(ss, &((*node)->right));
}

// Destrutor
Tree::~Tree() {
    _root = _clear(_root);
}

// Essa funcao recebe uma raiz chamada node e
// ela libera todos os nos decendentes de node e o proprio node.
Node *Tree::_clear(Node *node) {
    if(node != nullptr) { // caso geral: vamos liberar essa arvore
        node->left = _clear(node->left);
        node->right = _clear(node->right);
        delete node;
    }
    return nullptr;
}

void Tree::inorder() {
    _inorder(_root);
    std::cout << std::endl;
}

void Tree::_inorder(Node *node) {
    if(node != nullptr) { // Caso Geral
        _inorder(node->left);
        std::cout << node->key << " ";
        _inorder(node->right);  
    }
}

void Tree::bshow(){
    _bshow(_root, "");
}

void Tree::_bshow(Node *node, std::string heranca) {
    if(node != nullptr && (node->left != nullptr || node->right != nullptr))
        _bshow(node->right , heranca + "r");
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
        _bshow(node->left, heranca + "l");
}

int Tree::size() { //TODO
    
}

int Tree::_size(Node *node) { // TODO
    
}

int Tree::height() { // TODO

}

int Tree::_height(Node *node) { // TODO
    
}
</code>
</pre>