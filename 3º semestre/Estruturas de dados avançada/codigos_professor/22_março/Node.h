#ifndef NODE_H
#define NODE_H

struct Node {
    // atributos de um Node
    int key;
    Node* left; 
    Node* right;

    Node(int key, Node* left, Node* right) // Construtor
    {
        this->key = key;
        this->left = left;
        this->right = right;
    }
};

#endif 
