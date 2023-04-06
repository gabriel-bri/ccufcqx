#include <iostream>
#include <sstream>
#include <string>
#include "Tree.h"

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


Tree::~Tree() {
    _root = _clear(_root);
}


Node *Tree::_clear(Node *node) {
    if(node != nullptr) { // caso geral: vamos liberar essa arvore
        node->left = _clear(node->left);
        node->right = _clear(node->right);
        delete node;
    }
    return nullptr;
}

void Tree::preorder() {
    _preorder(_root);
}

void Tree::_preorder(Node *node) {
    if(node != nullptr) { // Caso Geral
        std::cout << node->key << " ";
        _preorder(node->left);
        _preorder(node->right);
    }
}

void Tree::inorder() {
    _inorder(_root);
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


int Tree::count_leaves() { // TODO
    return _count_leaves(_root);
}

int Tree::_count_leaves(Node *node) { // TODO
    if (node == nullptr)
        return 0;

    if (node->left == nullptr && node->right == nullptr)
        return 1;
    
    return _count_leaves(node->left) + _count_leaves(node->right);
}

void Tree::delete_leaves() { // TODO
  _delete_leaves(_root);
}

Node* Tree::_delete_leaves(Node *node) { // TODO
    if (!node)
        return nullptr;

    if (!node->left && !node->right) {
        delete node;
        return nullptr;
    }

    node->left = _delete_leaves(node->left);
    node->right = _delete_leaves(node->right);

    return node;
}

void Tree::delete_leaves_with_value(int key) { // TODO
    _delete_leaves_with_value(key, _root);
}

Node* Tree::_delete_leaves_with_value(int key, Node *node) { // TODO
    if (node == nullptr) {
        return nullptr;
    }
    
    node->left = _delete_leaves_with_value(key, node->left);
    node->right = _delete_leaves_with_value(key, node->right);
    
    if (node->left == nullptr && node->right == nullptr && node->key == key) {
        free(node);
        return nullptr;
    }
    
    return node;
}


