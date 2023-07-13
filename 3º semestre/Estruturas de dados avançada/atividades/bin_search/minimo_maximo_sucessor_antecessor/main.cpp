#include <iostream>
#include <string>
#include <climits>
#include <sstream>
#include "bst.h"
using namespace std;

int main()
{
	BST arv;
	string skeys;
	
	getline(cin, skeys); // read a string containing all keys separated by spaces

	stringstream ss { skeys };
	int value;

	while(ss >> value) {
		arv.add(value);
	}

	int v;
	cin >> v;

	cout << "minimo: " << arv.minimum() << endl;
	cout << "maximo: " << arv.maximum() << endl;

	int pred = arv.predecessor(v);
	if(pred == INT_MIN)
		cout << v << " nao tem antecessor ou nao esta na arvore" << endl;
	else 
		cout << "antecessor(" << v << ") = " << pred << endl;

	int succ = arv.successor(v);
	if(succ == INT_MAX)
		cout << v << " nao tem sucessor ou nao esta na arvore" << endl;
	else 
		cout << "sucessor(" << v << ") = " << succ << endl;

	return 0;
}