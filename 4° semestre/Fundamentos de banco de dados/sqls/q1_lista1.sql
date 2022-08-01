-----------
--- Script cria o básico para você conseguir responder as questões
-----------
 /*
  create table evento (
  	cod_evento int unique, nome varchar, 
  	data date, hora time, valor float, 
  	cod_local int, cod_produtora int,
  	FOREIGN KEY (cod_local) REFERENCES local (cod_local),
  		FOREIGN KEY (cod_produtora) REFERENCES produtora (cod_produtora)	
 );
 */

/*
insert into evento values (1, 'Lançamento do Jogo do Bicho', '2021-07-28', '24:00:00', 250.6, 1, 1);
insert into evento values (2, 'Fortal 2019', '2021-07-28', '24:00:00', 250.6, 2, 1);
insert into evento values (3, 'The Hackers Conference', '2019-05-10', '24:00:00', 500, 2, 1);
insert into evento values (4, 'The Hackers Conference', '2020-05-10', '24:00:00', 500, 2, 1)
insert into evento values (5, 'Forró Estourado ao Vivo', '2020-05-10', '24:00:00', 560000, 2, 1)
*/

/*
 create table ingresso(
 	id_ingresso int,
 	cod_evento int, 
 	nome varchar, 
 	cpf varchar,
 	PRIMARY KEY (id_ingresso),
  	FOREIGN KEY (cod_evento) REFERENCES evento(cod_evento)
 )
*/
-- insert into ingresso values (1, 5, 'Joao da Silva', '111.111.111-11');

-- create table local (
-- 	cod_local int, 
-- 	nome_local varchar, 
-- 	logradouro varchar, 
-- 	bairro varchar, 
-- 	numero int, 
-- 	cidade varchar, 
-- 	CEP varchar,
-- 	PRIMARY KEY (cod_local)
-- )

---insert into local values (1, 'Centro de Eventos', 'Rua das Flores', 'Centro', 120, 'Fortaleza', '60811-341');
---insert into local values (2, 'Castelão', 'Rua do Barraco', 'Maraponga', 120, 'Fortaleza', '60811-341');

-- create table produtora (
-- 	cod_produtora int, 
-- 	nome varchar, 
-- 	telefone varchar, 
-- 	logradouro varchar, 
-- 	bairro varchar, 
-- 	numero int, 
-- 	cidade varchar, 
-- 	CEP varchar,
-- 	PRIMARY KEY (cod_produtora)
-- )

-- insert into produtora values (1, 'RM-Eventos', '(11)1111-1111', 'Rua São Francisco',
-- 'Meireles', 100, 'Fortaleza', '60165-121');



