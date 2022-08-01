#include <iostream>
#include <vector>
using namespace std;


void show(vector<string> mat){
    for(int l = 0; l < (int) mat.size(); l++)
        cout << mat[l] << "\n";
}

bool esta_fora(vector<string> &mat, int l, int c) {
    int nl = mat.size();
    int nc = mat[0].size();

    if(l < 0 || l >= nl) {
        return true;
    }

    if(c < 0 || c >= nc) {
        return true;
    }

    return false;
}
void tocar_fogo(vector<string> &mat, int l, int c){
    int nl = mat.size();
    int nc = mat[0].size();
    //TODO faca seu codigo aqui
    if(esta_fora(mat, l, c) || mat[l][c] != '#') {
        return;
    }

    mat[l][c] = 'o';
    tocar_fogo(mat, l, c - 1); //esquerda
    tocar_fogo(mat, l - 1, c); //cima
    tocar_fogo(mat, l, c + 1);//direta
    tocar_fogo(mat, l + 1, c); //baixo
}

int main(){
    int nl = 0, nc = 0, lfire = 0, cfire = 0;
    scanf("%d %d %d %d\n", &nl, &nc, &lfire, &cfire);
    vector<string> mat;
    for(int l = 0; l < nl; l++){
        string line;
        cin >> line;
        mat.push_back(line);
    }
    tocar_fogo(mat, lfire, cfire);
    show(mat);
}