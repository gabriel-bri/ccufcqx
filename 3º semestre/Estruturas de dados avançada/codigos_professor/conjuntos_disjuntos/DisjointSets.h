#ifndef DSETS_H
#define DSETS_H
#include <vector>
using std::vector;

/**
 * Implementation of the disjoint-sets data structure
 * using path compression and union by rank
 */
class DisjointSets {
public:
    DisjointSets( int numElements );   // construtor cria os conjuntos iniciais
    int findSet( int x );             // retorna o representante
    void unionSets( int x, int y );   // une dois conjuntos

private:
    struct Node { 
        int parent; 
        int rank; 
    };
    vector<Node> sets;
};

#endif