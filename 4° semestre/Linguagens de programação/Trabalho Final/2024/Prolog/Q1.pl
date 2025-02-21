% Definição das arestas do grafo
aresta(0, 1).
aresta(1, 2).
aresta(2, 3).
aresta(3, 0).

% Predicado para verificar adjacência
adjacente(X, Y) :- aresta(X, Y).
adjacente(X, Y) :- aresta(Y, X).

% Predicado para verificar se uma lista de vértices forma um caminho
caminho([_]).
caminho([X, Y | Resto]) :- adjacente(X, Y), caminho([Y | Resto]).

% Predicado para calcular o grau de um vértice
grau(V, G) :- findall(_, adjacente(V, _), Adjacentes), length(Adjacentes, G).