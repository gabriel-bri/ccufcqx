% Predicado para adicionar um elemento a uma lista
adiciona(X, L1, [X | L1]).

% Predicado para apagar todas as ocorrências de um elemento em uma lista
apaga(_, [], []).
apaga(X, [X | Resto], L2) :- apaga(X, Resto, L2).
apaga(X, [Y | Resto], [Y | L2]) :- X \= Y, apaga(X, Resto, L2).

% Predicado para concatenar duas listas
concatena([], L2, L2).
concatena([X | Resto], L2, [X | L3]) :- concatena(Resto, L2, L3).

% Predicado para verificar se um elemento é membro de uma lista
membro(X, [X | _]).
membro(X, [_ | Resto]) :- membro(X, Resto).

% Predicado para calcular o comprimento de uma lista
comprimento(X, []) :- X is 0.
comprimento(X, [_ | Resto]) :- comprimento(N1, Resto),X is N1 + 1.