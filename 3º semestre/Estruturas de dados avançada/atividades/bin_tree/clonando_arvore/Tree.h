#ifndef TREE_H
#define TREE_H
#include <string>
#include <sstream>

struct Node;

class Tree {
public:
    Tree();
    Tree(std::string serial);
    void inorder();   // percurso em ordem simetrica
    void bshow();
    bool identical(Tree *t);
    Tree *clone();
    ~Tree();
private:
    Node *_root;
    Node *_clear(Node *node);
    void _inorder(Node *node);
    void _bshow(Node *node, std::string heranca);
    void _serializeTree(std::stringstream& ss, Node **node);
    bool _identical(Node *nd1, Node *nd2);
    Node *_clone(Node *node);
};

#endif