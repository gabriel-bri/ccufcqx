#include <iostream>
#include <string>
using namespace std;

template < typename K, typename D >
struct Node {
    K chave;
    D dado;
    Node *left;
    Node *right;
    int height;
};

struct Carro {
    int ano_de_fabricacao;
    string marca;
};

int main() {
    
    Carro car {1997, "Chevrolet"};

    Node<int, Carro*> *ptr = new Node<int, Carro*>;
    ptr->chave = car.ano_de_fabricacao;
    ptr->dado = &car;
    ptr->left = nullptr;
    ptr->right = nullptr;
    ptr->height = 1;

    cout << ptr->dado->ano_de_fabricacao << endl;
    cout << ptr->dado->marca << endl;

    delete ptr;

}