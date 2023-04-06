#ifndef TREE_H
#define TREE_H
#include <string>
#include <sstream>

struct Node;

class Tree {
public:
    Tree(std::string serial);
    void preorder();  // percurso em pre-ordem
    void inorder();   // percurso em ordem simetrica
    void bshow();
    void delete_leaves();
    void delete_leaves_with_value(int key);
    int count_leaves();
    ~Tree();
private:
    Node *_root;
    Node *_clear(Node *root);
    void _preorder(Node *node);
    void _inorder(Node *node);
    void _bshow(Node *node, std::string heranca);
    void _serializeTree(std::stringstream& ss, Node **node);
    Node *_delete_leaves(Node *node);
    Node* _delete_leaves_with_value(int key, Node *node);
    int _count_leaves(Node *node);
};

#endif