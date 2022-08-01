#include <iostream>
#include <iomanip>

using namespace std;

struct Aluno {
    int matricula;
    char* nome;
    float media;

};

Aluno* criaAluno() {
    int mat;
    char* nome = new char[100];
    float media;
    cout << "= = = = = = = = = = = = = = = = = = = = = = = =";
    cout << "\n";
    cout << "Digite a matrícula: ";
    cin >> mat;

    cout << "Digite o nome: ";
    cin.ignore();
    cin.get(nome, 100);

    cout << "Digite a média: ";
    cin >> media;
    cout << "= = = = = = = = = = = = = = = = = = = = = = = =";
    cout << "\n";
    Aluno* a = new Aluno;
    a->matricula = mat;
    a->nome = nome;
    a->media = media;

    return a;  
}

void printAluno(Aluno* a) {
    cout << "\n";
    cout << "- - - - - - - - - " << "\n";
    cout << "Nome do aluno: " << a->nome << "\n";
    cout << "Matrícula do aluno: " << a->matricula << "\n";
    cout << "Média do aluno: " << a->media << "\n";
    cout << "- - - - - - - - - " << "\n";
}

int buscaAluno(Aluno** v, int n, int matricula) {
    for(int i = 0; i < n; i++) {
        Aluno* a = v[i];
       if(v[i]->matricula == matricula) {
           return i;
       }
    }

    return -1;
}
int main() {
    int n;
    cout << "Digite o tamanho do vetor: ";
    cin >> n;

    Aluno* v[n];
    for(int i = 0; i < n; i++) {
        v[i] = criaAluno();
    }

    cout << "\n";

    int matricula;
    cout << "Digite a matrícula do aluno: ";
    cin >> matricula;

    int res = buscaAluno(v, n, matricula);

    if(res >= 0) {
        printAluno(v[res]);
    }

    else {
        cout << "NÃO ENCONTRADO O ALUNO COM A MATRÍCULA " << matricula;
    }

    for(int i = 0; i < n; i++) {
        v[i] = criaAluno();
    }

    for(int i = 0; i < n; i++) {
        delete v[i]->nome;
        delete v[i];
    }

    return 0;
}