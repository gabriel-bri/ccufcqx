#include <iostream>
#include "node.h"
#include "avl.h"
using namespace std;

int avl_tree::height(Node *node) {
         
}

int avl_tree::balance(Node *node) {
    
}

Node* avl_tree::rightRotation(Node *p) {
    
}

Node* avl_tree::leftRotation(Node *p) {
    
}

void avl_tree::add(int key) {
    
}

Node* avl_tree::add(Node *p, int key) {
    
}

Node* avl_tree::fixup_node(Node *p, int key) {
    
}

void avl_tree::clear() {
    root = clear(root);
}

Node *avl_tree::clear(Node *node) {
    if(node != nullptr) {
        node->left = clear(node->left);
        node->right = clear(node->right);
        delete node;
    }
    return nullptr;
}

avl_tree::~avl_tree() {
    clear();
}

void avl_tree::bshow() const {
    bshow(root, "");
}

void avl_tree::bshow(Node *node, std::string heranca) const {
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