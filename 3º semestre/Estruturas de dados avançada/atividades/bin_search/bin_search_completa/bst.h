#ifndef BST_H
#define BST_H
#include <iostream>
#include <string>
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
    Node(int k, Node* l = nullptr, Node* r = nullptr) {
        this->key = k;
        this->left = l;
        this->right = r;
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
    bool add(int k);  //  ---> Completar
    int height();
    ~BST();
private:
    Node *root;
    Node *_add(Node *node, int key); // ---> Descomente se voce precisar implementar essa funcao recursiva
    void bshow(Node *node, std::string heranca);
    Node *clear(Node *node);
    int height(Node *node);
};

/*****************************
 * Implementacao da classe
 *****************************/
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

int BST::height() {
    return height(root);
}

int BST::height(Node *node) {
    if(node == nullptr) return 0;
    else return 1 + std::max(height(node->left), height(node->right));
}

// Funcao publica 'add'
// Esta funcao pode ser implementada sem usar recursividade e sem usar nenhuma estrutura
// de dados adicional. Porem, deixarei aberta a forma como voce decidir implementa-la.
// Voce pode implementa-la como quiser, contanto que ela funcione e, de fato, crie uma
// arvore binaria de busca (BST).
// Esta funcao adiciona um no com chave k na arvore e: 
// (1) devolve true em caso de sucesso;
// (2) devolve false caso contrario.
// Lembre-se que nao podem haver chaves repetidas na nossa arvore.
bool BST::add(int k) {
    if(root == nullptr) {
        root = new Node(k);
        return true;
    } else {
        Node* currentNode = root;
        Node* parentNode = nullptr;

        while(currentNode != nullptr) {
            parentNode = currentNode;

            if(k < currentNode->key) {
                currentNode = currentNode->left;
            } else if(k > currentNode->key) {
                currentNode = currentNode->right;
            } else {
                return false;
            }
        }

        if(k < parentNode->key) {
            parentNode->left = new Node(k);
            parentNode->left->parent = parentNode;
        } else {
            parentNode->right = new Node(k);
            parentNode->right->parent = parentNode;
        }

        return true;
    }
}


// Descomente esta funcao caso voce precise implementar uma versao auxiliar
// recursiva para a funcao de adicionar nodes na arvore

    


#endif