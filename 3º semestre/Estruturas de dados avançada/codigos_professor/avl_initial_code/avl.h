#ifndef AVL_H
#define AVL_H
#include "node.h"

class avl_tree {
public:
    avl_tree() = default;
    avl_tree(const avl_tree& t) = delete;
    avl_tree& operator=(const avl_tree& t) = delete;
    void add(int key);
    void bshow() const;
    void clear();
    ~avl_tree();
    
private:
    Node *root {nullptr};
    int height(Node *node);
    int balance(Node *node);
    Node* rightRotation(Node *p);
    Node* leftRotation(Node *p);
    Node* add(Node *p, int key);
    Node* fixup_node(Node *p, int key);
    void bshow(Node *node, std::string heranca) const;
    Node* clear(Node *node);
};

#endif