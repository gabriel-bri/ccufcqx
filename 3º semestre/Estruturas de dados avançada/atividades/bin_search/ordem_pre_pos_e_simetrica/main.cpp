#include <iostream>
#include <string>
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

	cout << "inorder: ";
	arv.inorder();
	cout << endl;
	cout << "preorder: ";
	arv.preorder();
	cout << endl;

	arv.clear();

	skeys.clear();
	getline(cin, skeys);
	stringstream sss { skeys };

	while(sss >> value) {
		arv.add(value);
	}

	cout << "inorder: ";
	arv.inorder();
	cout << endl;
	cout << "preorder: ";
	arv.preorder();
	cout << endl;

	return 0;
}