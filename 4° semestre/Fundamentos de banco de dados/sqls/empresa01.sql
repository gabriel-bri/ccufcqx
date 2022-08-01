drop schema empresa cascade;
create schema empresa;
set schema 'empresa';
-- livia
create table localizacoes_dep(dnumero integer, dlocal varchar(30));

-- Funcionario - Paulo
create table funcionario(pnome varchar(30) not null, 
						 minicial varchar(30), 
						 unome varchar(30) not null, 
						 cpf varchar(11) primary key,
						 datanasc date, 
						 endereco varchar(30) not null, 
						 sexo varchar(1), 
						 salario decimal, 
						 cpf_supervisor varchar(11),
						 dnr integer,
						 rg varchar(30) unique);
						 
alter table funcionario add constraint fk_cpf_supervisor 
foreign key (cpf_supervisor) references Funcionario(cpf);						 

-- Wilhelm - Departamento
create table departamento(dnome varchar(30), 
						  dnumero integer, 
						  cpf_gerente varchar(11), 
						  data_inicio_gerente date,
						  primary key(dnumero));

-- Projeto - Maria Alice
create table projeto (projnome varchar(50), projnumero integer, 
					  projlocal varchar (50), dnum integer); 

alter table projeto add constraint pk_projeto primary key (projnumero);

-- Trabalha_Em - Edvaldo Oliveira
create table trabalha_em( Fcfp varchar(11), Pnr integer, Horas integer,
						 foreign key (Fcfp) references Funcionario(cpf));

-- dependente -  joão Paulo
create table dependente(Fcpf varchar(11),
						Nome_dependente varchar(30),
						Sexo varchar(1),
						Datanasc date, 
						Parentesco varchar(30));


