#include <iostream>
#include <cstdlib>
#include <iomanip>
using namespace std;

struct aluno {
   int matricula;
   char nome[50];
   float media;
};

aluno le_aluno() {
   aluno a;
   cin >> a.matricula;
   cin.ignore(); // lê e descarta o caractere '\n' do buffer
   cin.get(a.nome, 50);
   cin >> a.media;
   return a;
}

/* 
Recebe vetor de alunos e novo aluno, e insere o novo aluno no final do vetor.
- v: vetor de alunos
- n: tamanho do vetor de alunos (passado por referência)
- novo: novo aluno a ser inserido no final do vetor.
Pseudocódigo:
   altere o tamanho do vetor v para conter *n+1 elementos, pondo endereço em v
   se não conseguir alocar (v == 0) imprima msg de erro e retorne 0
   coloque o aluno 'novo' na última posição do vetor (posição *n)
   aumente em 1 o tamanho do vetor (incrementar *n)
   retorne v
*/
aluno *insere_aluno(aluno *v, int *n, aluno a) {
   //aumentar o n
   *n = *n + 1;
   //ajuste para quando v não está alocado
   if (v == 0) {
      //preciso alocar o v
      v = new aluno[1];
   }

   else {  //v ja alocado  // [3] -> [4]
      //vamos precisar realocar o vetor
      //criar um novo vertor maior
      aluno *novo = new aluno[*n];
      //copiamos os elementos do antigo para o novo
      for (int i = 0; i < (*n - 1); i++) { //percorre o antigo
         novo[i] = v[i];
      }
      //deletamos o antigo
      delete[] v;
      v = novo;
   }
   //inserir
   v[*n - 1] = a;
   return v;
}

/*
Recebe vetor de alunos, e retira do vetor o primeiro aluno com matrícula igual à
matrícula passada como parâmetro.
- v: vetor de alunos
- n: tamanho do vetor de alunos (passado por referência)
- matricula: matrícula do aluno a ser removido.
Pseudocódigo:
   para i de 0 até o tamanho do vetor menos 1
      se a matrícula do i-ésimo elemento do vetor é igual à 'matrícula' passada como parâmetro
         copie último elemento do vetor para a posição i
         realoque vetor para conter um elemento a menos, pondo endereço em v
         se não for possível realocar, imprima mensagem de erro e retorne
         reduza em 1 o tamanho do vetor (decrementar *n)
         break
   retorne o endereço de memória do vetor realocado
*/
aluno *remove_aluno(aluno *v, int *n, int matricula) {
   if (v != nullptr){
      for (int i = 0; i < *n; i++){
         if (v[i].matricula == matricula){
            //vou ter que apagar
            //pegar o ultimo e colocar na posição do i
            v[i] = v[*n - 1];
            //realocar
            aluno *novo = new aluno[*n - 1];
            //fazer a copia
            for (int j = 0; j < *n - 1; j++){
               novo[j] = v[j];
            }
            //deleto o antigo
            delete[] v;

            *n = *n - 1;
            return v;
         }
      }
      return v;
   }
   return v;
}

int main() {
   int num_oper = 0, i, n = 0;
   cin >> num_oper;
   aluno *v = 0; ///nullptr

   for (i = 0; i < num_oper; i++) {
      cin.ignore(); // lê e descarta o caractere '\n' do buffer
      char oper;
      cin >> oper;
      if (oper == 'i') {
         aluno a = le_aluno();
         v = insere_aluno(v, &n, a);
      }

      else {
         int mat;
         cin >> mat;
         v = remove_aluno(v, &n, mat);
      }
   }
   cout << "\n\n>>";
   for (i = 0; i < n; i++) {
      cout << v[i].matricula << "\n"
           << v[i].nome << "\n"
           << std::fixed << setprecision(1) << v[i].media << "\n";
   }

   delete[] v;

   return 0;
}