#include <iostream>
#include <vector>

using namespace std;
vector<int> matchingStrings(vector<string> strings, vector<string> consultas) {
    //Cria uma variável que armazena o total de vezes que a palavra
    //foi encontrada
    int total = 0;
    //Cria uma string de procura
    string procura;
    
    //Cria um vector para armazenar a quantidade encontrada
    vector<int> quantidade;
    //Define o tamanho do vetor de quantidade de acordo
    //com a quantidade de consultas pedidas
    quantidade.reserve(consultas.capacity());

    //Percorre o vetor de consultas
    for(int i = 0; i < consultas.size(); i++) {
        //Salva a palavra na posição atual.
        procura = consultas[i];

        //Percorre todo o vetor com as palavras procurando
        //o dado da palavra procura
        for(int i = 0; i < strings.size(); i++) {
            if(procura == strings[i]) {
                total += 1;
                //Caso encontre no array a igualdade entre
                //palavras ele incrementa em um a quantidade.
            }
        }

        //Coloca a quantidade no final do vetor.
        quantidade.push_back(total);
        //Zera a flag para uma nova rodada.
        total = 0;
    }

    //Retorna a quantidade
    return quantidade;
}

int main() {

    //Pede ao usuário o tamanho do vetor que ele deseja.
    int tamanho;
    cin >> tamanho;

    //Cria o vector de nome palavras e define o seu tamanho 
    //de acordo com a entrada do usuário.
    vector<string> palavras;
    palavras.reserve(tamanho);


    //Cria uma varíavel do tipo string que irá receber as palavras que o usuário
    //deseja.
    string strEntrada;

    //Realiza um loop até a quantidade de palavras definida pelo o usuário.
    for(int i = 0; i < tamanho; i++) {
        //Recebe os valores que deverão ser colocados.
        cin >> strEntrada;
        //Adiciona sempre ao final do vetor a palavra digitada pelo o usuário.
        palavras.push_back(strEntrada);
    }


    //Pede ao usuário o tamanho do vetor que ele deseja para armazenar as palavras para buscar.
    int tamanhoBusca;
    cin >> tamanhoBusca;

    //Cria o vector das palavras que o usuário irá procurar.
    vector<string> buscarPalavras;
    //Reserva o tamanho de acordo com a quantidade a ser procurada;
    buscarPalavras.reserve(tamanhoBusca);

    //Define a string para armazenar as palavras a serem buscadas.
    string strBuscar;

    for(int i = 0; i < tamanhoBusca; i++) {
        //Recebe os valores que deverão ser colocados.
        cin >> strBuscar;
        //Adiciona sempre ao final do vetor a palavra digitada pelo o usuário.
        buscarPalavras.push_back(strBuscar);        
    }

    //Recebe o resultado da função com o vetor já preenchido.
    vector<int> totFinal = matchingStrings(palavras, buscarPalavras);

    //Imprime o resultado.
    for(int i = 0; i < totFinal.size(); i++) {
        if(i != 0) {
            cout << " ";
        }
        cout << totFinal[i];
    }
 
    cout << "\n";
 
    return 0;
}