#ifndef GRAPH_H
#define GRAPH_H

#include <list>
#include <vector>
#include <limits>
#include "Edge.h"
using std::list;
using std::vector;
using std::numeric_limits;

/**
 * Classe que especifica um TAD ListGraph que implementa um 
 * grafo como uma lista de adjacencias.
 * Um grafo é um conjunto de vertices e um conjunto de arestas.
 * Vertices sao representados pelos inteiros 0 a n-1.
 * Arestas sao pares ordenados de vertices.
*/
class ListGraph {
private:
    int _num_v;               // numero de vertices
    int _num_e;               // numero de arestas
    bool _directed;           // flag para indicar se eh direcionado
    vector<list<Edge>> _adj;  // listas de adjacencias

public:
    /**
     * Construtor. Constroi o grafo
     * @param n O numero de vertices
     * @param d True se esse eh um grafo direcionado
    */
    ListGraph(int n, bool d);

    // Destrutor
    ~ListGraph() = default;

    /**
     * Retorna o numero de vertices
     * @param O numero de vertices
     */
    int get_num_v() const { return _num_v; }

    /**
     * Retorna o numero de arestas
     * @param O numero de arestas
     */
    int get_num_e() const { return _num_e; }

    /**
     * Determina se esse eh um grafo direcionado
     * @return true se e somente se esse eh um grafo direcionado
     */
    bool is_directed() const { return _directed; }

    /**
     * Insere uma nova aresta no grafo
     * @param edge A nova aresta
     */
    void insert(const Edge& edge);

    /**
     * Determina se uma aresta existe
     * @param source O vertice de origem
     * @param dext O vertice de destino
     * @return true se existe uma aresta de source para dest
    */
    bool is_edge(int source, int dest) const;

    /** Obtem a aresta entre dois vertices
     * @param source O vertice origem
     * @param dest O vertice destino
     * @return A aresta entre os dois vertices ou uma aresta
     * com peso igual a numeric_limits<double>::infinity() se nao existe nenhuma aresta
     */
    Edge get_edge(int source, int dest) const;

    /**
     * Retorna uma referencia para a lista de adjacencias de um vertice
     * @param source O vertice origem
     * @return Uma const reference para a lista de adjacencias de um vertice
    */
    list<Edge>& neighbors(int source);
    const list<Edge>& neighbors(int source) const;

    /** 
     * Retorna um iterator para a primeira aresta adjacent ao vertice especificado.
     * @param source O vertice origem
     * @return Um iterador para as arestas adjacentes a source
    */
    list<Edge>::iterator begin(int source);
    list<Edge>::const_iterator begin(int source) const;

    /** Retorna um iterador uma posicao apos a ultima aresta 
     * adjacente ao vertice especificado
     * @param source O vertice origem
     */
    list<Edge>::iterator end(int source);
    list<Edge>::const_iterator end(int source) const;

    // Funcoes deletadas
    ListGraph(const ListGraph&) = delete;
    ListGraph& operator=(const ListGraph&) = delete;

};


#endif