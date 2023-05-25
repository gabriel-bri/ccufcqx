#include <iostream>
#include "avl.h"
using namespace std;

void dobra(int& v) { v *= 2; }
void incrementa(int& v) { v += 1; }

int main() {
    avl_tree t1, t2;

    for(int i = 1; i <= 20; i++)
        t1.add(i);

    for(int i = 21; i <= 29; i++)
        t2.add(i);

    avl_tree* ptr = t1.intercala(t2);
    
    ptr->bshow();   
    cout << "altura da arvore: " << ptr->height() << endl; 
}