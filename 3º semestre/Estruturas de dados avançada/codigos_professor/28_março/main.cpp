#include <iostream>
#include <iomanip>
#include "Tree.h"
using namespace std;

int main() {
    /* Cria a arvore:
    
              3
            /   \ 
           4     5
               /   \ 
              6     7
    */

    Tree empty;
    Tree t4 (4, empty, empty);
    Tree t6 (6, empty, empty);
    Tree t7 (7, empty, empty);
    Tree t5 (5, t6, t7);
    Tree t3 (3, t4, t5);

    t3.preorder();
    cout << endl;

    cout << boolalpha << t3.contain(10) << endl;
    cout << boolalpha << t3.contain(7) << endl;

    cout << t3.serializa() << endl;

    Tree novaTree ("2 3 # # 4 # #"); // cria uma arvore a partir de uma serial
    novaTree.preorder();
    cout << endl;
}