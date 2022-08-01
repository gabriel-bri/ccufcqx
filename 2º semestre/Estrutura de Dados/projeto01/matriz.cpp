#include "Projeto.h"
#include <fstream>
using namespace std;

    Matriz::Matriz(int linhas, int colunas) {
        Ltam = linhas;
        Ctam = colunas;
        head = new Node(-1, -1, 0, nullptr, nullptr); // head da matriz
        head->abaixo = head;
        head->direita = head;

        Node *aux = head;
        for(int i = 1; i <= linhas; i++) { //Cria todos os "heads" de cada linhas
            Node *head_Line = new Node(i, -1, 0, nullptr, nullptr);
            head_Line->direita = head_Line;
            aux->abaixo = head_Line;
            aux = head_Line;
        }
        aux->abaixo = head; // circular
        aux = head;
        for(int j = 1; j <= colunas; j++) { //Cria todos os "heads" de cada coluna
            Node *head_Col = new Node(-1, j, 0, nullptr, nullptr);
            head_Col->abaixo = head_Col;
            aux->direita = head_Col;
            aux = head_Col;
        }
        aux->direita = head; // circular
    }
    
    Matriz::~Matriz() {
        Node *it_heads = head->direita;
        Node *it_elems;
        for(int j = 0; j < Ctam; j++) { //deleta as colunas e os elementos armazenados na matriz
            it_elems = it_heads->abaixo;
            while(it_elems != it_heads) { // percorre a coluna deletando as células até retornar ao head da coluna
                Node *aux = it_elems;
                it_elems = it_elems->abaixo;
                delete aux;
            }
            it_heads = it_heads->direita;
            delete it_elems; // deleta o head da coluna
        }
        it_heads = head->abaixo;
        for(int i = 0; i < Ltam; i++) { //deleta os heads das linhas
            it_elems = it_heads;
            it_heads = it_heads->abaixo;
            delete it_elems;
        }
        delete head;
    }
    
    bool Matriz::naMatriz(int i, int j) {
        return i <= Ltam && i >= 1 && j <= Ctam && j >= 1;
    }
    
    void Matriz::insert(int i, int j, double value) {
        if(i > Ltam || i < 1 || j > Ctam || j < 1) //impossível inserir fora da matriz
            return;
        
        Node *aux = head->direita; 
        while(aux->coluna != j) // percorre as colunas até achar a correta
            aux = aux->direita;
        Node *it = aux;
        while(it->abaixo->linha != -1 && it->abaixo->linha < i) // percorre a coluna até achar o local correto de inserção
            it = it->abaixo;
        
        if(it->abaixo->linha == i) { // Se já existir um nó na posição i j, atualiza o valor e sai do insert
            it->abaixo->valor = value;
            return;
        }
        
        Node *novo = new Node(i, j, value, nullptr, it->abaixo); 
        it->abaixo = novo;  // cria e encadeia o novo nó
        
        //coloca o novo nó na linha correta
        aux = head->abaixo;
        while(aux->linha != i) // percorre as linhas até achar a correta
            aux = aux->abaixo;;
        it = aux;
        while(it->direita->coluna != -1 && it->direita->coluna < j) // percorre a linha até achar o local correto de inserção
            it = it->direita;
        novo->direita = it->direita;
        it->direita = novo; // encadeia o novo nó na linha
    }
    
    double Matriz::getValue(int i,int j) {
        if(i > Ltam || i < 1 || j > Ctam || j < 1) {
            cout << "Impossível obter valor de fora da matriz" << endl;
            return 0;
        }
        Node *aux = head->direita;
        while(aux->coluna != j) // percorre até achar a coluna correta
            aux = aux->direita;
        Node *it = aux->abaixo;
        while(it != aux || i == it->linha) //percorre até achar a célula correta ou até o head da coluna se não existir
            it = it->abaixo;
        return it->valor;
    }
    
    int Matriz::getTamLinhas() {
        return Ltam;
    }
    
    int Matriz::getTamCols() {
        return Ctam;
    }

    Node* Matriz::getHead() {
        return head;
    }

    void Matriz::print() {
        Node *aux = head;
        Node *it = aux;
        for(int i = 1; i <= Ltam; i++) { // percorre as linhas
            aux = aux->abaixo;
            it = aux;
            for(int j = 1; j <= Ctam; j++) { // percorre as colunas
                if(it->direita->linha == -1) // Se não tiver ninguém à direita (voltando pro ínicio), imprime 0
                    cout << 0 << " ";
                else if(it->direita->coluna == j) { // Se a coluna do nó estiver de acordo com o contador j, imprime o valor e vai pra frente
                    it = it->direita;
                    cout << it->valor << " ";
                }
                else
                    cout << 0 << " ";
            }
            cout << endl;
        }
    }

    Matriz *soma (Matriz *A, Matriz *B) {
        int linhas = A->getTamLinhas();
        int colunas = A->getTamCols();
        if(linhas != B->getTamLinhas() || colunas != B->getTamCols()) // Se não for possível somar, nullptr
            return nullptr;
        Node *auxA = A->getHead();
        Node *itA = auxA->direita;
        Node *auxB = B->getHead();
        Node *itB = auxB->direita;
        Matriz *C = new Matriz(linhas, colunas);
        
        for(int i = 1; i <= linhas; i++) { // percorre as linhas
            auxA = auxA->abaixo;
            itA = auxA->direita;
            auxB = auxB->abaixo;
            itB = auxB->direita;
            while(itA->coluna != -1 || itB->coluna != -1) { // percorre a linha de cada matriz enquanto as duas não acabarem
                if(itA->coluna == itB->coluna) { // Se linha e coluna forem equivalentes, insere a soma na nova matriz e avança as 2 matrizes
                    C->insert(i, itA->coluna, itA->valor+itB->valor);
                    itA = itA->direita;
                    itB = itB->direita;
                } else if (itA->coluna < itB->coluna && itA->coluna != -1 || itB->coluna == -1) { // Se o nó de A tem valor da coluna menor q o nó de B, A+0 e avança A
                    C->insert(i, itA->coluna, itA->valor);
                    itA = itA->direita;
                } else { // do contrário, B+0 e avança B
                    C->insert(i, itB->coluna, itB->valor);
                    itB = itB->direita;
                }
            }
        }
        return C;
    }
    
    Matriz *multiplica(Matriz *A, Matriz *B) {
        int linhasA = A->getTamLinhas();
        int linhasB = B->getTamLinhas();
        int colunasA = A->getTamCols();
        int colunasB = B->getTamCols();

        if(colunasA != linhasB) // Se não for possivel multiplicar, nullptr
            return nullptr;
        
        Node *auxA = A->getHead();
        Node *itA;
        Node *auxB;
        Node *itB;
        Matriz *C = new Matriz(linhasA, colunasB);
        int valor = 0, valorA = 0, valorB = 0;

        for(int i = 1; i <= linhasA; i++) { // percorre as linhas da matriz A
            auxA = auxA->abaixo;
            auxB = B->getHead();
            for(int j = 1; j <= colunasB; j++) { // percorre as colunas da matriz B
                auxB = auxB->direita;
                itB = auxB;
                itA = auxA;
                valor = 0;
                for(int k = 1; k <= colunasA; k++) { // percorre as colunas de A e linhas de B
                    if(k != 1 && itA->linha == -1 && itB->coluna == -1)
                        break;
                    valorA = valorB = 0;
                    if(itA->direita->coluna == k) // Se a coluna do nó de A à direita for igual ao contador k, vai pra direita
                        itA = itA->direita;
                    if(itB->abaixo->linha == k) // Se a linha do nó de B à baixo for igual ao contador k, vai pra baixo
                        itB = itB->abaixo;
                    if(itA->coluna == k) // Se a coluna do nó de A for igual ao contador k, guarda o valor da coluna de A
                        valorA = itA->valor;
                    if(itB->linha == k) // Se a linha do nó for igual ao contador k, guarda o valor da linha de B
                        valorB = itB->valor;
                    valor += valorA*valorB; // soma o valor de A * B com o resultado das multiplicações antes deles
                }
                C->insert(i, j, valor);
            }
        }
        return C;
    }

    Matriz *lerMatrizDeArquivo(std::string arq) {
        ifstream arquivo;
        arquivo.open(arq);
        int linha, coluna;
        double valor;
        arquivo >> linha;
        arquivo >> coluna;
        Matriz *nova = new Matriz(linha, coluna);
        while(arquivo >> linha) {
            arquivo >> coluna;
            arquivo >> valor;
            nova->insert(linha, coluna, valor);
        }
        arquivo.close();
        return nova;
    }
