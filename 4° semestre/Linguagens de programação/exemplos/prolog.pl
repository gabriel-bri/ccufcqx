divertido(carro).
divertido(ps5).
divertido(xbox).
divertido(thelastofus).
divertido(thelastofusparte2).
divertido(thewitcher3).
divertido(java).


vermelho(cuscuz).
vermelho(rosa).
vermelho(seta).


verde(alface).
verde(hulk).
verde(grama).
verde(natureza).

gosta(joao,maria).
gosta(maria,joao).
gosta(pedro,gatos).
gosta(maria,carro):-divertido(carro).
gosta(lucas,maria):-divertido(ps4).
gosta(maria,carro):-divertido(carro).
gosta(joao,Algo):-gosta(maria,Algo).

gosta(lucas,Algo):-divertido(Algo).
gosta(maria,Algo):-divertido(Algo);verde(Algo).




pai(fernando,maria).
pai(fernando,mari).
mae(maria,joao).
mae(maria,carlos).
avou(julio,maria).



filho(X,Y):-pai(Y,X);mae(Y,X).

avou(X,Y):-pai(X,Z),(pai(Z,Y);mae(Z,Y)).
avoo(X,Y):-mae(X,Z),filho(Y,Z).

irmao(X,Y):- X\=Y,(pai(Z,X),pai(Z,Y));(mae(Z,X),mae(Z,Y)).






















desce(X,Y):-filho(X,Y).
desce(X,Y):-filho(X,Z),desce(Z,Y).



pertence(X,[X|L]).
pertence(X,[Y|L]):-pertence(X,L).


insere(X,L,[X|L]).


conc([],L2,L2).
conc([X|L1],L2,[X|L3]):-conc(L1,L2,L3).





mortal(lucas).
homem(socrates).
mortal(X):-homem(X).


















