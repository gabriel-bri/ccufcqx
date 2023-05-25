#include <iostream>
#include <vector>
#include "node.h"
#include "avl.h"
using namespace std;

// retorna a altura do nó.
// se a arvore for vazia ela tem altura 0
// caso contrario, retorna o valor que está no campo height
int avl_tree::height(Node *node) {
    return (node == nullptr) ? 0 : node->height;
}

int avl_tree::balance(Node *node) {
    return height(node->right) - height(node->left);
}

Node* avl_tree::rightRotation(Node *p) {
    Node *u = p->left;
    p->left = u->right;
    u->right = p;
    // recalcular as alturas de p e de u
    p->height = 1 + max(height(p->left),height(p->right));
    u->height = 1 + max(height(u->left),height(u->right));
    return u;
}

Node* avl_tree::leftRotation(Node *p) {
    Node *u = p->right;
    p->right = u->left;
    u->left = p;
    // recalcular as alturas de p e de u
    p->height = 1 + max(height(p->right),height(p->left));
    u->height = 1 + max(height(u->left),height(u->right));
    return u;
}

// função pública que recebe uma chave e a insere
// somente se ela não for repetida
void avl_tree::add(int key) {
    root = add(root, key);
}

// função recursiva privada que recebe uma raiz de arvore
// e uma chave e insere a chave na tree se e somente se 
// ela nao for repetida. Claro, tem que deixar AVL novamente
Node* avl_tree::add(Node *p, int key) {
    if(p == nullptr)
        return new Node(key);
    if(key == p->key) 
        return p;
    if(key < p->key)
        p->left = add(p->left, key);
    else 
        p->right = add(p->right, key);
    
    p = fixup_node(p, key);

    return p;
}

Node* avl_tree::fixup_node(Node *p, int key) {
    // recalcula a altura de p
    p->height = 1 + max(height(p->left),height(p->right));

    // calcula o balanço do p
    int bal = balance(p);

    if(bal >= -1 && bal <= 1) {
        return p;
    }

    if(bal < -1 && key < p->left->key) {
        p = rightRotation(p);
    }
    else if(bal < -1 && key > p->left->key) {
        p->left = leftRotation(p->left);
        p = rightRotation(p);
    }
    else if(bal > 1 && key > p->right->key) {
        p = leftRotation(p);
    }
    else if(bal > 1 && key < p->right->key) {
        p->right = rightRotation(p->right);
        p = leftRotation(p);
    }
    return p;
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

void avl_tree::remove(int key) {
    root = remove(root, key);
}

Node* avl_tree::remove(Node *node, int key) {
    if(node == nullptr) // node nao encontrado
        return nullptr; /*L\pauseL*/
    if(key < node->key) 
        node->left = remove(node->left, key);
    else if(key > node->key)
        node->right = remove(node->right, key); /*L\pauseL*/
    // encontramos no node
    else if(node->right == nullptr) { // sem filho direito
        Node *child = node->left;
        delete node;
        return child;
    }
    else // tem filho direito: troca pelo sucessor
        node->right = remove_successor(node, node->right); /*L\pauseL*/
    
    // Atualiza a altura do node e regula o node
    node = fixup_deletion(node); 
    return node;
}

Node* avl_tree::remove_successor(Node *root, Node *node) {
    if(node->left != nullptr)
        node->left = remove_successor(root, node->left);
    else {
        root->key = node->key;
        Node *aux = node->right;
        delete node;
        return aux;
    }
    // Atualiza a altura do node e regula o node
    node = fixup_deletion(node);
    return node;
}

Node* avl_tree::fixup_deletion(Node *node) {
    node->height = 1 + max(height(node->left),height(node->right));

    int bal = balance(node);

    // node pode estar desregulado, ha 4 casos a considerar
    if(bal > 1 && balance(node->right) >= 0) {
        return leftRotation(node);
    }
    else if(bal > 1 && balance(node->right) < 0) {
        node->right = rightRotation(node->right);
        return leftRotation(node);
    }
    else if(bal < -1 && balance(node->left) <= 0) {
        return rightRotation(node);
    }
    else if(bal < -1 && balance(node->left) > 0) { 
        node->left = leftRotation(node->left);
        return rightRotation(node);
    }
    return node;
} 

// Recebe um ponteiro para a raiz de uma arvore
// e retorna o ponteiro para o clone dessa arvore
Node* clone_rec(Node *node) {
    if(node == nullptr)
        return nullptr;
    else {
        Node *aux = new Node(node->key);
        aux->left = clone_rec(node->left);
        aux->right = clone_rec(node->right);
        return aux;
    }
}

// construtor de copia
// recebe uma avl_tree como parâmetro e cria um clone dessa 
// arvore e faz a minha arvore ser esse clone
avl_tree::avl_tree(const avl_tree& t) {
    this->root = clone_rec(t.root);
}

// sobrecarga do operador de atribuicao
avl_tree& avl_tree::operator=(const avl_tree& t)  {
    if(this != &t) {
        clear();
        this->root = clone_rec(t.root);
    }
    return *this;
}

// percurso em ordem simetrica que percorre os nodes
// executando a funcao f nas chaves dos nodes
// f eh um ponteiro para uma funcao
void inorder_rec(Node *node, void (*f)(int& key)) {
    if(node != nullptr) {
        inorder_rec(node->left, f);
        f(node->key);
        inorder_rec(node->right, f);
    }
}

// acessa as chaves da arvore em ordem simetrica
// executando a funcao f em todas as chaves 
void avl_tree::access_keys_inorder(void (*f)(int& key)) {
    inorder_rec(root, f);
}

int avl_tree::height() const {
    return root->height;
}

// recebe como parametros a raiz de uma arvore e um vetor
// e percorre a arvore em ordem simetrica preenchendo o vetor
// com as chaves encontradas
void inorder_rec(Node *node, std::vector<int>& v) {
    if(node != nullptr) {
        inorder_rec(node->left, v);
        v.push_back(node->key);
        inorder_rec(node->right, v);
    }
}

// recebe como argumento um vector e preenche esse vector
// com as chaves da arvore em ordem crescente
void avl_tree::keys_as_vector(std::vector<int>& v) const {
    inorder_rec(root, v);
}

// Cria uma arvore binaria de busca completa a partir de um vetor de chaves ordenado.
// Recebe como entrada o vetor, o indice inicial e o indice final do vetor
Node* build_complete_tree(const vector<int>& v, int l, int r) {
    if(l <= r) {
        int m = (l+r)/2;
        Node *aux = new Node(v[m]);
        aux->left = build_complete_tree(v,l,m-1);
        aux->right = build_complete_tree(v,m+1,r);
        return aux;
    }
    return nullptr;
}

// Recebe como entrada dois vetores v1 e v2 já ordenados e 
// intercala as chaves de v1 e v2 em um terceiro vetor v3.
// Ao final, v3 contem todas as chaves ordenadas.
void merge_vector(const vector<int>& v1, const vector<int>& v2, vector<int>& v3) {
    int i {0}, j {0};
    while(i < v1.size() && j < v2.size()) {
        if(v1[i] <= v2[j])
            v3.push_back(v1[i++]);
        else   
            v3.push_back(v2[j++]);
    }
    while(i < v1.size()) v3.push_back(v1[i++]);
    while(j < v2.size()) v3.push_back(v2[j++]);
}

// recebe um vetor ordenado e retorna true se e somente se ele tem numeros repetidos
bool has_repeated_keys(const vector<int>& v) {
    for(int i {0}; i < (int)v.size()-1; ++i) {
        if(v[i] == v[i+1])
            return true;
    }
    return false;
}

// funcao que recebe o ponteiro para a raiz de uma arvore com K nodes e ajusta o
// campo height de todos os K nodes dessa arvore.
// Complexidade: O(K)
int height_rec(Node *node) {
    if(node == nullptr)
        return 0;
    else {
        node->height = 1 + std::max(height_rec(node->left), height_rec(node->right));
        return node->height;
    }
}

// funcao que intercala duas arvores 
// T1 e T2 com n e m vertices, respectivamente.
// Essa funcao requer que as chaves das duas arvores sejam distintas.
// Retorna um ponteiro para uma terceira arvore que eh a 
// intercalacao de T1 e T2.
// Essa funcao tem complexidade O(m+n).
avl_tree* avl_tree::intercala(const avl_tree& t) {
    vector<int> v1, v2, v;                            // O(1)
    this->keys_as_vector(v1);                         // O(m)
    t.keys_as_vector(v2);                             // O(n)
    merge_vector(v1, v2, v);                          // O(m+n)
    if(has_repeated_keys(v))                          // O(m+n)
        throw runtime_error("chaves repetidas");      // O(1)
    Node *r = build_complete_tree(v, 0, v.size()-1);  // O(m+n)
    height_rec(r);                                    // O(m+n)
    avl_tree *ptr = new avl_tree;                     // O(1)
    ptr->root = r;                                    // O(1)
    return ptr;                                       // O(1)
}



