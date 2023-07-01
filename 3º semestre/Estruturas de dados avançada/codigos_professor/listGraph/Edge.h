#ifndef EDGE_H
#define EDGE_H
#include <string>
#include <iostream>
#include <limits>
#include <sstream>

class Edge {
private:
    int _source;      // o vertice de origem da aresta
    int _dest;        // o vertice de destino da aresta
    double _weight;   // o peso da aresta

public:
    // Constroi uma aresta de source para dest com peso w
    // Se w nao for especificado ele eh setado para 1.0
    Edge(int source, int dest, double w = 1.0);

    // Constroi uma aresta falsa com source e dest igual a -1 e 
    // weight igual a infinito
    Edge();

    // Constroi uma aresta que eh uma copia de outra
    Edge(const Edge& other);

    // Compara se duas arestas sao iguais. Duas arestas sao iguais se 
    // seus vertices de origem e destino sao iguais. O peso eh desconsiderado.
    bool operator==(const Edge& other) const;

    int get_dest() const; // retorna o destino

    int get_source() const; // retorna a origem

    double get_weight() const; // retorna o peso

    std::string to_string() const; // retorna uma representacao de string da aresta

    // sobrecarga do operador de insercao
    friend std::ostream& operator<<(std::ostream&, const Edge&);
};

#endif