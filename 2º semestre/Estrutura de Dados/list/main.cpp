#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include "LList.h"
using namespace std;

void print(LList* l) {
	for(l->moveToStart(); !l->inTheEnd(); l->next())
		cout << l->getValue() << " ";
	cout << endl;
}

int main()
{
	vector<LList*> listas;
	
	while(true) {
		string cmd;
		getline(cin, cmd);

		std::stringstream ss{ cmd };
		vector<string> tokens;
		string buffer;

		while(ss >> buffer) 
			tokens.push_back(buffer);

		// exit
		if(tokens[0] == "exit") {
			for(int i = 0; i < listas.size(); i++)
				delete listas[i];
			listas.clear();
			cout << "saindo..." << endl;
			break;
		}
		// cria
		else if(tokens[0] == "cria") {
			LList *lst = new LList;
			listas.push_back(lst);
		}
		// append [x] [l]
		else if(tokens[0] == "append") {
			int x = std::stoi(tokens[1]);
			int l = std::stoi(tokens[2]);
			listas[l]->append(x);
		}
		// copy [l]
		else if(tokens[0] == "copy") {
			int l = std::stoi(tokens[1]);
			LList *lcp = listas[l]->copy();
			listas.push_back(lcp);
		}
		// appendArray [l] [n] [a1] ... [an] 
		else if(tokens[0] == "appendArray") {
			int l = std::stoi(tokens[1]);
			int n = std::stoi(tokens[2]);
			int *v = new int[n];
			for(int i = 0; i < n; i++)
				v[i] = std::stoi(tokens[i+3]);
			listas[l]->appendArray(v, n);
		}
		// equal [l1] [l2] 
		else if(tokens[0] == "equal") {
			int l1 = std::stoi(tokens[1]);
			int l2 = std::stoi(tokens[2]);
			if(listas[l1]->equal(*listas[l2])) cout << "listas iguais" << endl;
			else cout << "listas diferentes" << endl;
		}
		// reverse [l]
		else if(tokens[0] == "reverse") {
			int l = std::stoi(tokens[1]);
			listas[l]->reverse();
		}
		// removeAll [x] [l]
		else if(tokens[0] == "removeAll") {
			int x = std::stoi(tokens[1]);
			int l = std::stoi(tokens[2]);
			listas[l]->removeAll(x);
		}
		// print [l] 
		else if(tokens[0] == "print") {
			int l = std::stoi(tokens[1]);
			if(listas[l]->empty()) cout << "lista " << l << " vazia" << endl;
			else {
				cout << "lista " << l << ": ";
				print(listas[l]);
			}
		}
		else {
			cout << "comando inexistente" << endl;
		}
	}
	return 0;
}
