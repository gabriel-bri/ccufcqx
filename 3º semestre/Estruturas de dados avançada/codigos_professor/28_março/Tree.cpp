#include "Tree.h"
#include <string>
#include <sstream>

using namespace std;

/********************************************************
 * Funcoes recursivas auxiliares
*/
void preorder_rec(Node* node) {
    if(node != nullptr) { // Caso geral: arvore nao vazia
        std::cout << node->key << " ";
        preorder_rec(node->left);
        preorder_rec(node->right);
    }
}

void posorder_rec(Node* node) {
    if(node != nullptr) { // Caso geral: arvore nao vazia
        posorder_rec(node->left);
        posorder_rec(node->right);
        std::cout << node->key << " ";
    }
}

void inorder_rec(Node* node) {
    if(node != nullptr) { // Caso geral: arvore nao vazia
        inorder_rec(node->left);
        std::cout << node->key << " ";
        inorder_rec(node->right);
    }
}

// recebe uma raiz de arvore e retorna 'true' se e somente se
// a arvore em questao contem a 'key'
bool contain_rec(Node *node, int key) {
    if(node == nullptr) { // Caso base
        return false;
    }
    else {
        if(node->key == key) {
            return true;
        }
        else {
            return contain_rec(node->left, key) || contain_rec(node->right, key);
        }

        return node->key == key || 
               contain_rec(node->left, key) || 
               contain_rec(node->right, key);
    }
}

// Essa funcao recursiva recebe a raiz de uma arvore e 
// libera todos os nos dessa arvore deixando ela vazia novamente
Node *clear_rec(Node *node) {
    if(node == nullptr) { // Caso base: arvore vazia
        return nullptr;
    }
    else { // Caso geral
        node->left = clear_rec(node->left);
        node->right = clear_rec(node->right);
        delete node;
        return nullptr;
    }
}

// Essa funcao recursiva recebe uma raiz de arvore e 
// retorna o numero de nos da arvore em questao 
int size_rec(Node *node) {
    //return (node == nullptr) ? 0 : 1 + size_rec(node->left) + size_rec(node->right);
    if(node == nullptr) 
        return 0;
    else 
        return 1 + size_rec(node->left) + size_rec(node->right);
}

void serialize_rec(Node *node, stringstream& ss) {
    if(node == nullptr) {
        ss << "# ";
    }
    else {
        ss << node->key << " ";
        serialize_rec(node->left, ss);
        serialize_rec(node->right, ss);
    }
}

// funcao recursiva que retorna a raiz de uma arvore criada
// a partir de uma serializacao 
Node *deserializa(stringstream& ss) {
    string valor;
    ss >> valor;
    if(valor == "#") {
        return nullptr;
    }
    else {
        int key = stoi(valor);
        Node *p = new Node(key, deserializa(ss),deserializa(ss));
        return p;
    }
}

/*********************************************************
 * Implementacao das funcoes-membro da classe Tree
*/
void Tree::preorder() {
    preorder_rec(root);
}

void Tree::inorder() {
    inorder_rec(root);
}

void Tree::posorder() {
    posorder_rec(root);
}

Tree::Tree() {
    root = nullptr;
}

// Cria um novo no com chave key e seus
// filhos serao as raizes de tl e tr.
// tl e tr serao arvores vazias ao final dessa funcao
Tree::Tree(int key, Tree& tl, Tree& tr) 
{
    root = new Node(key, tl.root, tr.root); // chama o construtor do struct Node
    tl.root = nullptr; // faz a arvore tl ficar vazia
    tr.root = nullptr; // faz a arvore tr ficar vazia
}

bool Tree::empty() {
    return root == nullptr;
}

bool Tree::contain(int key) {
    return contain_rec(root, key); // chama a funcao recursiva auxiliar
}

void Tree::clear() {
    root = clear_rec(root);
}

int Tree::size() {
    return size_rec(root);
}

Tree::~Tree() {
    clear();
}

string Tree::serializa() {
    stringstream ss;
    serialize_rec(root, ss);
    return ss.str();
}

Tree::Tree(std::string serial) {
    stringstream ss { serial };
    root = deserializa(ss);
}