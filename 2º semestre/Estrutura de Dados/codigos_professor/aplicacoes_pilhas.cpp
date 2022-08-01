#include <iostream>
#include <cctype>
#include <string>
#include <stack>

using namespace std;

bool balanceada(string exp) {
	stack<char> pilha;

	for(unsigned i = 0; i < exp.size(); i++) {
		switch(exp[i]) {
			case '(': 
			case '[': pilha.push(exp[i]);
					  break;
			case ')': if(!pilha.empty() && pilha.top() == '(')
						pilha.pop();
					  else return false;
					  break;
			case ']': if(!pilha.empty() && pilha.top() == '[')
						pilha.pop();
					  else return false;
					  break;
			default : return false;
					  break;
		}
	}
	return pilha.empty();
}

int calculaPosfixa(string exp) {
	stack<int> pilha;

	for(unsigned i = 0; i < exp.size(); i++) {
		if(isdigit(exp[i])) {
			char ch = exp[i];
			pilha.push( atoi(&ch) );			
		}
		else {
			int a = pilha.top(); pilha.pop();
			int b = pilha.top(); pilha.pop();
			switch(exp[i]) {
				case '+': pilha.push(a + b); break;
				case '-': pilha.push(a - b); break;
				case '*': pilha.push(a * b); break;
				case '/': pilha.push(a / b); break;
			}
		}
	}
	return pilha.top();
}

string parentizadaParaPosfixa(string exp) {
	stack<char> pilha;
	string posfixa;

	for(unsigned i = 0; i < exp.size(); i++) {
		switch (exp[i]) {
			case '(': break;
			case ')': posfixa += pilha.top();
					  pilha.pop();
					  break;
			case '+': 
			case '-':
			case '*':
			case '/': pilha.push(exp[i]);
					  break;
			default : posfixa += exp[i];
					  break;
		}
	}

	return posfixa;
}

int main()
{
	string expressao;
	getline(cin, expressao);

	string posfixa = parentizadaParaPosfixa(expressao);
	cout << calculaPosfixa(posfixa) << endl;

	return 0;
}