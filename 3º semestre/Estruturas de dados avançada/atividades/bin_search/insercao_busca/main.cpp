#include <iostream>
#include <string>
#include <sstream> // cabecalho que define o tipo stringstream
#include "bst.h"
using namespace std;

int main()
{
	BST arv;
	string keys;
	getline(cin, keys); // ler uma string com todas as chaves

	stringstream ss { keys };
	int value;

	while(ss >> value) 
		arv.add(value); // Adiciona chaves na arvore

	arv.inorderParent();

	cout << endl;

	if(arv.contains(5))
		cout << "Contem 5" << endl;
	else
		cout << "Nao contem 5" << endl;

	if(arv.contains(78))
		cout << "Contem 78" << endl;
	else
		cout << "Nao contem 78" << endl;

	if(arv.contains(0))
		cout << "Contem 0" << endl;
	else
		cout << "Nao contem 0" << endl;
	
	return 0;
}