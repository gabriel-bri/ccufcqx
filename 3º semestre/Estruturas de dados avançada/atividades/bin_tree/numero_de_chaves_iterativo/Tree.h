#ifndef TREE_H
#define TREE_H
#include <string>
#include <sstream>

struct Node;

class Tree {
public:
    Tree(std::string serial);
    void bshow();
    int size();
    ~Tree();
private:
    Node *_root;
    Node *_clear(Node *node);
    void _bshow(Node *node, std::string heranca);
    void _serializeTree(std::stringstream& ss, Node **node);
    int _size_iterativo(Node *node);
};

#endif