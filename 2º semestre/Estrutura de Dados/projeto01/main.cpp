#include <iostream>
#include <vector>
#include <sstream>
#include "Projeto.h"
using namespace std;

int main() {
	vector<Matriz*> matrizes; // Vetor de ponteiros para matrizes

    while(true) {
		string cmd;
		getline(cin, cmd);

		stringstream ss{ cmd };
		vector<string> tokens;
		string buffer;

		while(ss >> buffer) {
			tokens.push_back(buffer);
		}
        // finaliza o programa e/ou limpa as matrizes armazenadas
		if(tokens[0] == "sair" || tokens[0] == "libera") {
			for(int i = 0; i < matrizes.size(); ++i) {
				delete matrizes[i];
				matrizes[i] = nullptr;
			}
			matrizes.clear();
			if(tokens[0] == "sair")
				break;
			cout << "matrizes limpas" << endl;
		}
		// cria <nome_do_arquivo>
		else if(tokens[0] == "cria") {
            string arq = tokens[1];
            Matriz *m = lerMatrizDeArquivo(arq);
			matrizes.push_back(m);
		}
		// insere <valor> [i] [j] [k]
		else if(tokens[0] == "insere") {
			double valor = stod(tokens[1]);
			int i = stoi(tokens[2]);
            int j = stoi(tokens[3]);
			int k = stoi(tokens[4]);
			matrizes[k]->insert(i,j,valor);
		}
		// imprime [k]
		else if(tokens[0] == "imprime") {
			int k = stoi(tokens[1]);
			matrizes[k]->print();
		}
        // valor [i] [j] [k]
		else if(tokens[0] == "valor") {
            int i = stoi(tokens[1]);
            int j = stoi(tokens[2]);
			int k = stoi(tokens[3]);
			if(!matrizes[k]->naMatriz(i,j))
				cout << "fora das dimensões da matriz" << endl;
			else
				cout << "valor: " << matrizes[k]->getValue(i,j) << endl;
		}
		// soma [fst] [snd] 
		else if(tokens[0] == "soma") {
            int fst = stoi(tokens[1]);
            int snd = stoi(tokens[2]);
			Matriz *C = soma(matrizes[fst],matrizes[snd]);
			if(C == nullptr) 
                cout << "nao foi possivel somar" << endl;
            else {
                C->print();
                matrizes.push_back(C);
            }
		}
        // multiplica [fst] [snd] 
		else if(tokens[0] == "multiplica") {
            int fst = stoi(tokens[1]);
            int snd = stoi(tokens[2]);
			Matriz *C = multiplica(matrizes[fst],matrizes[snd]);
			if(C == nullptr) 
                cout << "nao foi possivel multiplicar" << endl;
            else {
                C->print();
                matrizes.push_back(C);
            }
		}
		else {
			cout << "comando inexistente" << endl;
		}
	}
	return 0;
}
