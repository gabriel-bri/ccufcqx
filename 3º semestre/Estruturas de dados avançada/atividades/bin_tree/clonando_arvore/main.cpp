#include <iostream>
#include <string>
#include "Tree.h"
using namespace std;

int main()
{
	string line1, line2;
    getline(cin, line1);
    getline(cin, line2);
    Tree bt1(line1);
    Tree bt2(line2);
    Tree *bt3 = bt1.clone();
    if(bt1.identical(bt3)) 
        cout << "identica" << endl;
    else 
        cout << "diferente" << endl;
    if(bt2.identical(bt3)) 
        cout << "identica" << endl;
    else 
        cout << "diferente" << endl;
    if(bt1.identical(&bt2)) 
        cout << "identica" << endl;
    else 
        cout << "diferente" << endl;
	return 0;
}