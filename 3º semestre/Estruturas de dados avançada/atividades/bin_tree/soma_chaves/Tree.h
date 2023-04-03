#ifndef TREE_H
#define TREE_H
#include <string>
#include <sstream>

struct Node;

class Tree {
public:
    Tree(std::string serial);
    void inorder();   // percurso em ordem simetrica
    void bshow();
    int sum_keys();
    int min_key();
    int total_internal_nodes();
    int um_filho();
    ~Tree();
private:
    Node *_root;
    void _bshow(Node *node, std::string heranca);
    void _serializeTree(std::stringstream& ss, Node **node);
    Node *_clear(Node *root);
    void _inorder(Node *node);
    int _sum_keys(Node *node);
    int _min_key(Node *node);
    int _total_internal_nodes(Node *node);
    int _um_filho(Node *node);
};

#endif