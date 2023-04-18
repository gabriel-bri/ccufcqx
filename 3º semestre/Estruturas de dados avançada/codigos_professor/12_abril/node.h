#ifndef NODE_H
#define NODE_H

struct Node {
    // atributos
    int key;
    int height;
    Node *left;
    Node *right;

    // Construtor
    Node (int key, Node *left = nullptr, Node *right = nullptr, int height = 1)
        : key(key), height(height), left(left), right(right)
    {
    }
};

#endif 
