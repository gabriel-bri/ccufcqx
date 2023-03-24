#include <iostream>
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
}