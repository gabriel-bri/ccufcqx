#ifndef AVL_H
#define AVL_H
#include <vector>
#include <string>
#include "node.h"
#include "dynamic_set.h"

class avl_tree : public dynamic_set { // herda de dynamic_set
public:
    avl_tree() = default;
    avl_tree(const avl_tree& t); 
    avl_tree& operator=(const avl_tree& t); 
    int height() const;
    void bshow() const;
    ~avl_tree();

    avl_tree* intercala(const avl_tree& t);

    virtual void add(int key) override;                               // O(lg n)
    virtual void clear() override;                                    // O(n)
    virtual void remove(int key) override;                            // O(lg n)
    virtual void access_keys_inorder(void (*f)(int& key)) override;   // O(n)
    virtual void keys_as_vector(std::vector<int>& v) const override;  // O(n)
                        

    // ------------------------------------------------------------------------------
    // TAREFA DE CASA: Implementar essas funcoes abaixo:
    //virtual bool contains(int key) const override;                    // O(lg n)
    //virtual int minimum() const override;                             // O(lg n)
    //virtual int maximum() const override;                             // O(lg n)
    //virtual int successor(int key) const override;                    // O(lg n)
    //virtual int predecessor(int key) const override;                  // O(lg n)
    //virtual bool empty() const override;                              // O(1)
    //virtual int size() const override;                                // O(n) ou O(1)
    //-------------------------------------------------------------------------------

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
    Node* remove(Node *node, int key); 
    Node* remove_successor(Node *root, Node *node);
    Node* fixup_deletion(Node *node);
};

#endif