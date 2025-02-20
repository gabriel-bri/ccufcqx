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

% Defini��es de sexo
sexo(jose, masculino).
sexo(maria, feminino).
sexo(joao, masculino).
sexo(ana, feminino).
sexo(helena, feminino).
sexo(joana, feminino).
sexo(mario, masculino).
sexo(carlos, masculino).

% Irm�: X � irm� de Y se X e Y t�m o mesmo progenitor, sendo X feminino e Y qualquer um
irma(X, Y) :- progenitor(P, X), progenitor(P, Y), X \= Y, sexo(X, feminino).

% Irm�o: X � irm�o de Y se X e Y t�m o mesmo progenitor, sendo X masculino e Y qualquer um
irmao(X, Y) :- progenitor(P, X), progenitor(P, Y), X \= Y, sexo(X, masculino).

% Descendente: X � descendente de Y se Y � progenitor de X ou se X � descendente de um filho de Y
descendente(X, Y) :- progenitor(Y, X).
descendente(X, Y) :- progenitor(Y, Z), descendente(X, Z).

% M�e: X � m�e de Y se X � progenitor de Y e X � do sexo feminino
mae(X, Y) :- progenitor(X, Y), sexo(X, feminino).

% Pai: X � pai de Y se X � progenitor de Y e X � do sexo masculino
pai(X, Y) :- progenitor(X, Y), sexo(X, masculino).

% Av�: X � av� de Y se X � progenitor de Z e Z � pai ou m�e de Y
avo(X, Y) :- progenitor(X, Z), progenitor(Z, Y), sexo(X, masculino).

% Av�: X � av� de Y se X � progenitor de Z e Z � pai ou m�e de Y
ava(X, Y) :- progenitor(X, Z), progenitor(Z, Y), sexo(X, feminino).

% Tio: X � tio de Y se X � irm�o de um dos pais de Y
tio(X, Y) :- (irmao(X, Z); irmao(Z, X)), (pai(Z, Y); mae(Z, Y)).

% Tia: X � tia de Y se X � irm� de um dos pais de Y
tia(X, Y) :- (irma(X, Z); irma(Z, X)), (pai(Z, Y); mae(Z, Y)).

% Primo: X � primo de Y se X � filho de um irm�o ou irm� de um dos pais de Y
primo(X, Y) :- (irmao(Z, W); irma(Z, W)), progenitor(W, Y), progenitor(Z, X).

% Prima: X � prima de Y se X � filha de uma irm� ou irm�o de um dos pais de Y
prima(X, Y) :- (irmao(Z, W); irma(Z, W)), progenitor(W, Y), progenitor(Z, X), sexo(X, feminino).