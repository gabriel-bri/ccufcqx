CREATE TABLE usuarios (
	id SERIAL PRIMARY KEY,
	nome varchar,
	peso float,
	altura float
);

CREATE TABLE alongamento (
	codigo_de_plano SERIAL PRIMARY KEY,
	Alongamento_ParteSuperior_do_Corpo BOOLEAN,
	Alongamento_Dor_nas_Costas BOOLEAN,
	Alongamento_Parte_Inferior_do_Corpo BOOLEAN, 
	Postura_de_Crianca BOOLEAN,
	Alongamento_peito BOOLEAN,
	Alongamento_de_Ombros BOOLEAN,
	Alongamento_Cobra BOOLEAN,
	Alongamento_Triceps BOOLEAN,
	Alongamento_Panturrilha BOOLEAN,
	quem_pratica int,
	foreign key (quem_pratica) references usuarios(id)
);

create table yoga (
	codigo_de_plano SERIAL PRIMARY KEY,
	Concentracao_Mental BOOLEAN,
	Aprimoramento_Mental BOOLEAN,
	Encolhimento_dos_ombros BOOLEAN,
	Inclinacao_para_os_lados BOOLEAN,
	Postura_da_Esfinge BOOLEAN,
	Ponte BOOLEAN,
	Bananeira BOOLEAN,
	Estocada_Crescente BOOLEAN,
	quem_pratica int,
	foreign key (quem_pratica) references usuarios(id)
);

CREATE TABLE meditacao_guiada (
	codigo_de_plano SERIAL PRIMARY KEY,
	Concentracao BOOLEAN,
	Emocoes BOOLEAN,
	Estresse BOOLEAN,
	quem_pratica int,
	foreign key (quem_pratica) references usuarios(id)
);

CREATE TABLE relatorio_semana (
	id_relatorio SERIAL PRIMARY KEY,
	duracao_em_horas int,
	historico varchar,
	qual_usuario int,
	foreign key (qual_usuario) references usuarios(id)
);

CREATE TABLE lembretes (
	id_lembrete SERIAL PRIMARY KEY,
	notificacao_atividade varchar,
	Monitoramento_de_Ingestão_de_Agua BOOLEAN,
	qual_usuario int,
	foreign key (qual_usuario) references usuarios(id)	
);

CREATE TABLE configuracoes_gerais (
	codigo_versao SERIAL PRIMARY KEY,
	modo_noturno BOOLEAN,
	qual_usuario int,
	foreign key (qual_usuario) references usuarios(id)	
);


insert into usuarios values (default, 'Joao', 68.5, 1.50);
insert into usuarios values (default, 'Marcos', 70, 1.80);
insert into usuarios values (default, 'Livia', 50, 1.90);
insert into usuarios values (default, 'Allison', 40.5, 1.54);
insert into usuarios values (default, 'Francisco', 55, 1.65);
insert into usuarios values (default, 'Silva', 68.5, 1.50);
insert into usuarios values (default, 'Afonso', 70.5, 1.80);
insert into usuarios values (default, 'Marina', 90.5, 1.84);
insert into usuarios values (default, 'Jair', 100, 1.80);
insert into usuarios values (default, 'Peter', 85, 1.75);

insert into alongamento values (default, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, 1);
insert into alongamento values (default, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, FALSE, FALSE, TRUE, 2);
insert into alongamento values (default, FALSE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, 3);
insert into alongamento values (default, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, 4);
insert into alongamento values (default, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, FALSE, TRUE, 5);
insert into alongamento values (default, TRUE, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE, FALSE, TRUE, 6);
insert into alongamento values (default, TRUE, FALSE, TRUE, FALSE, FALSE, FALSE, TRUE, FALSE, TRUE, 7);
insert into alongamento values (default, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, 8);
insert into alongamento values (default, TRUE, FALSE, TRUE, TRUE, FALSE, FALSE, TRUE, FALSE, TRUE, 9);
insert into alongamento values (default, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, TRUE, FALSE, TRUE, 10);

insert into yoga values (default, TRUE, FALSE, TRUE, FALSE, FALSE, TRUE, TRUE, FALSE, 1);
insert into yoga values (default, FALSE, FALSE, TRUE, TRUE, FALSE, TRUE, FALSE, FALSE, 2);
insert into yoga values (default, FALSE, TRUE, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE, 3);
insert into yoga values (default, TRUE, FALSE, TRUE, FALSE, FALSE, FALSE, TRUE, FALSE, 4);
insert into yoga values (default, FALSE, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE, FALSE, 5);
insert into yoga values (default, FALSE, FALSE, TRUE, FALSE, TRUE, TRUE, FALSE, FALSE, 6);
insert into yoga values (default, TRUE, FALSE, TRUE, FALSE, FALSE, TRUE, TRUE, FALSE, 7);
insert into yoga values (default, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, FALSE, 8);
insert into yoga values (default, TRUE, FALSE, TRUE, TRUE, FALSE, TRUE, TRUE, FALSE, 9);
insert into yoga values (default, TRUE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, 10);

insert into meditacao_guiada values (default, TRUE, FALSE, TRUE, 1);
insert into meditacao_guiada values (default, FALSE, FALSE, TRUE, 2);
insert into meditacao_guiada values (default, FALSE, FALSE, TRUE, 3);
insert into meditacao_guiada values (default, TRUE, FALSE, FALSE, 4);
insert into meditacao_guiada values (default, FALSE, FALSE, TRUE, 5);
insert into meditacao_guiada values (default, TRUE, TRUE, TRUE, 6);
insert into meditacao_guiada values (default, TRUE, FALSE, TRUE, 7);
insert into meditacao_guiada values (default, TRUE, FALSE, TRUE, 8);
insert into meditacao_guiada values (default, TRUE, TRUE, TRUE, 9);
insert into meditacao_guiada values (default, FALSE, FALSE, FALSE, 10);

insert into relatorio_semana values (default, 8, 'Necessita realizar o fortalecimento das emoções', 1);
insert into relatorio_semana values (default, 5, 'Necessita realizar os exercícios de yoga com mais precisão', 2);
insert into relatorio_semana values (default, 4, 'Necessita realizar o fortalecimento das emoções', 3);
insert into relatorio_semana values (default, 7, 'Aluno bastante dedicado', 4);
insert into relatorio_semana values (default, 10, 'Necessita realizar aulas de yoga', 5);
insert into relatorio_semana values (default, 6, 'Aluno sem nenhuma observação', 6);
insert into relatorio_semana values (default, 6, 'Aluno sem nenhuma observação', 7);
insert into relatorio_semana values (default, 4, 'Aluno sem nenhuma observação', 8);
insert into relatorio_semana values (default, 2, 'Aluno sem nenhuma observação', 9);
insert into relatorio_semana values (default, 1, 'Aluno sem nenhuma observação', 10);

insert into lembretes values (default, 'Yoga', TRUE, 1);
insert into lembretes values (default, 'Meditação Guiada', FALSE, 2);
insert into lembretes values (default, 'Yoga', TRUE, 3);
insert into lembretes values (default, 'Alongamento', FALSE, 4);
insert into lembretes values (default, 'Meditação Guiada', TRUE, 5);
insert into lembretes values (default, 'Yoga', FALSE, 6);
insert into lembretes values (default, 'Meditação Guiada', TRUE, 7);
insert into lembretes values (default, 'Alongamento', FALSE, 8);
insert into lembretes values (default, 'Yoga', FALSE, 9);
insert into lembretes values (default, 'Meditação Guiada', FALSE, 10);

insert into configuracoes_gerais values (default, TRUE, 1);
insert into configuracoes_gerais values (default, FALSE, 2);
insert into configuracoes_gerais values (default, FALSE, 3);
insert into configuracoes_gerais values (default, FALSE, 4);
insert into configuracoes_gerais values (default, TRUE, 5);
insert into configuracoes_gerais values (default, FALSE, 6);
insert into configuracoes_gerais values (default, TRUE, 7);
insert into configuracoes_gerais values (default, TRUE, 8);
insert into configuracoes_gerais values (default, TRUE, 9);
insert into configuracoes_gerais values (default, FALSE, 10);