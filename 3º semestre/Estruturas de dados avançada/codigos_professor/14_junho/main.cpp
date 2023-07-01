#include <iostream>
#include <fstream>
#include <vector>
#include <list>
using namespace std;

int main() {
    fstream file;
    file.open("grafo.txt");
    int n, m;
    file >> n >> m;

    vector<list<int>> grafo;
    grafo.resize(n);

    int count {m};
    while(count > 0) {
        int u, v;
        file >> u >> v;
        grafo[u].push_back(v);
        grafo[v].push_back(u);
        count--;
    }
    file.close();

    for(int i = 0; i < n; ++i) {
        cout << "v[" << i << "]: ";
        for(auto vizinho : grafo[i]) {
            cout << vizinho << " ";
        }
        cout << endl;
    }
}