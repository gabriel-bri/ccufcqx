/*
create table setor(
  	cod_setor int, 
  	nome_setor varchar,
 	 primary key (cod_setor)
);
*/

-- insert into setor values (1, 'Limpeza');
-- insert into setor values (2, 'Escritório e papelaria');
/*
create table produto(
 	cod_produto int, 
 	nome_produto varchar, 	
 	categoria varchar, 
	cod_setor int,
 	FOREIGN KEY (cod_setor) REFERENCES setor(cod_setor),
 	PRIMARY KEY (cod_produto)
 );
 */
--  select setor.nome_setor from setor
--  INNER JOIN produto as p on p.cod_setor = setor.cod_setor
--  WHERE p.categoria = 'Informática'
 
--  insert into produto values (1, 'Mouse LOGITECH', 'Informática', 2)

/*
 create table fornecedor (
 	cod_fornecedor varchar, 
 	nome_fornecedor varchar, 
 	cidade varchar,
	primary key (cod_fornecedor)
);
*/

-- insert into fornecedor values ('F01', 'João Fornecimento', 'Recife');

/*
 create table fornecedor_Prod(
 	cod_fornecedor varchar, 
 	cod_produto int, 
 	preco float,
 	FOREIGN KEY (cod_fornecedor) REFERENCES fornecedor(cod_fornecedor),
	FOREIGN KEY (cod_produto) REFERENCES produto(cod_produto)
);

*/


--  insert into fornecedor_Prod values ('F01', 1, 500)

-- select p.nome_produto from produto as p
-- INNER JOIN fornecedor_Prod as fp on fp.cod_produto = p.cod_produto
-- INNER JOIN fornecedor on fp.cod_fornecedor = fornecedor.cod_fornecedor
-- WHERE fornecedor.cod_fornecedor = 'F01'

/*
 select fornecedor.nome_fornecedor from produto as p
 INNER JOIN fornecedor_Prod as fp on fp.cod_produto = p.cod_produto
 INNER JOIN fornecedor on fp.cod_fornecedor = fornecedor.cod_fornecedor
 WHERE fornecedor.cidade = 'Recife'
 */

-- select f.nome_fornecedor from fornecedor as f
-- INNER JOIN fornecedor_Prod as fp on f.cod_fornecedor = f.cod_fornecedor
-- WHERE f.cidade = 'Recife'

-- select p.nome_produto from produto as p
-- INNER JOIN fornecedor_Prod as fp on fp.cod_produto = p.cod_produto
-- WHERE fp.preco >= 100

-- select f.nome_fornecedor from fornecedor as f
-- INNER JOIN fornecedor_Prod as fp on fp.cod_fornecedor = f.cod_fornecedor
-- INNER JOIN produto as p on p.cod_produto = fp.cod_produto
-- INNER JOIN setor as s on s.cod_setor = p.cod_setor
-- WHERE s.nome_setor = 'Escritório e papelaria' and fp.preco > 50

