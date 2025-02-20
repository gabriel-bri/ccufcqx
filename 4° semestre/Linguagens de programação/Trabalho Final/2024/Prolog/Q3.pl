% Fatos sobre os progenitores
progenitor(X, Y) :- (
  X = jose, Y = joao ;
  X = maria, Y = joao ;
  X = jose, Y = ana ;
  X = maria, Y = ana ;
  X = ana, Y = helena ;
  X = ana, Y = joana ;
  X = joao, Y = mario ;
  X = helena, Y = carlos ;
  X = mario, Y = carlos                    
).

% Definições de sexo
sexo(jose, masculino).
sexo(maria, feminino).
sexo(joao, masculino).
sexo(ana, feminino).
sexo(helena, feminino).
sexo(joana, feminino).
sexo(mario, masculino).
sexo(carlos, masculino).

% Irmã: X é irmã de Y se X e Y têm o mesmo progenitor, sendo X feminino e Y qualquer um
irma(X, Y) :- progenitor(P, X), progenitor(P, Y), X \= Y, sexo(X, feminino).

% Irmão: X é irmão de Y se X e Y têm o mesmo progenitor, sendo X masculino e Y qualquer um
irmao(X, Y) :- progenitor(P, X), progenitor(P, Y), X \= Y, sexo(X, masculino).

% Descendente: X é descendente de Y se Y é progenitor de X ou se X é descendente de um filho de Y
descendente(X, Y) :- progenitor(Y, X).
descendente(X, Y) :- progenitor(Y, Z), descendente(X, Z).

% Mãe: X é mãe de Y se X é progenitor de Y e X é do sexo feminino
mae(X, Y) :- progenitor(X, Y), sexo(X, feminino).

% Pai: X é pai de Y se X é progenitor de Y e X é do sexo masculino
pai(X, Y) :- progenitor(X, Y), sexo(X, masculino).

% Avô: X é avô de Y se X é progenitor de Z e Z é pai ou mãe de Y
avo(X, Y) :- progenitor(X, Z), progenitor(Z, Y), sexo(X, masculino).

% Avó: X é avó de Y se X é progenitor de Z e Z é pai ou mãe de Y
ava(X, Y) :- progenitor(X, Z), progenitor(Z, Y), sexo(X, feminino).

% Tio: X é tio de Y se X é irmão de um dos pais de Y
tio(X, Y) :- (irmao(X, Z); irmao(Z, X)), (pai(Z, Y); mae(Z, Y)).

% Tia: X é tia de Y se X é irmã de um dos pais de Y
tia(X, Y) :- (irma(X, Z); irma(Z, X)), (pai(Z, Y); mae(Z, Y)).

% Primo: X é primo de Y se X é filho de um irmão ou irmã de um dos pais de Y
primo(X, Y) :- (irmao(Z, W); irma(Z, W)), progenitor(W, Y), progenitor(Z, X).

% Prima: X é prima de Y se X é filha de uma irmã ou irmão de um dos pais de Y
prima(X, Y) :- (irmao(Z, W); irma(Z, W)), progenitor(W, Y), progenitor(Z, X), sexo(X, feminino).