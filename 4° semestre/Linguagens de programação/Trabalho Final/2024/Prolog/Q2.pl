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
comprimento([], 0).
comprimento([_ | Resto], N) :- comprimento(Resto, N1), N is N1 + 1.

% Consultas

?- adiciona(3, [1, 2], L).  % Adiciona 3 à lista [1, 2]
L = [3, 1, 2].

?- apaga(2, [1, 2, 3, 2], L).  % Remove todas as ocorrências de 2 da lista [1, 2, 3, 2]
L = [1, 3].

?- concatena([1, 2], [3, 4], L).  % Concatena as listas [1, 2] e [3, 4]
L = [1, 2, 3, 4].

?- membro(2, [1, 2, 3]).  % Verifica se 2 é membro da lista [1, 2, 3]
true.

?- comprimento([1, 2, 3], N).  % Calcula o comprimento da lista [1, 2, 3]
N = 3.