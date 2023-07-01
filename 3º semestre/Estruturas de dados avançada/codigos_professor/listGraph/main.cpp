#include <iostream>
#include "Edge.h"
#include "ListGraph.h"
using namespace std;

void print(const ListGraph& graph) {
    for(int i = 0; i < graph.get_num_v(); ++i) {
        cout << i << ": ";
        for(auto v = graph.begin(i); v != graph.end(i); ++v) {
            cout << *v << " ";
        }
        cout << endl;
    }
}

int main() {
    ListGraph graph(5, false); // grafo com 5 vertices V = {0,1,2,3,4} nao direcionado
    graph.insert(Edge(0,1));
    graph.insert(Edge(1,2));
    graph.insert(Edge(2,3));
    graph.insert(Edge(3,4));
    graph.insert(Edge(4,0));
    print(graph);
}