-- Visões:

-- Visão Materializada: Aluno Ativo - Agrupa os usuários que passaram mais de 5 horas realizando algum tipo de atividade durante a semana,
-- e tambem realizaram injestão de água através da aba lembretes.

create materialized view Aluno_Ativo as(
	select r.qual_usuario as id_usuario
	from relatorio_semana r, lembretes l
	where r.qual_usuario = l.qual_usuario and r.duracao_em_horas > 5 and l.monitoramento_de_ingestão_de_agua = 'true'
	order by duracao_em_horas ASC
);



-- Visão Virtual: Aluno de Atividade Intensa - Agrupa os usuários que realizaram as atividades mais 'intensas' das abas yoga e alongamento

create or replace view Aluno_de_atividadeIntensa as(
select a.quem_pratica as id_usuario
from alongamento a, yoga y
where a.quem_pratica = y.quem_pratica and alongamento_partesuperior_do_corpo
	and alongamento_parte_inferior_do_corpo
	and alongamento_cobra
	and postura_de_crianca
	and ponte
	and bananeira
	and postura_da_esfinge = 'true'
group by a.quem_pratica
);

-- Trigger

-- Trigger Atualiza_Aluno: Visões materializadas não conseguem ser atualizadas de forma automatica
-- portanto, as triggers abaixo realizam essa atualização sempre que um usuário se enquadra nos requisitos
-- da visão Aluno_Ativo, que são aqueles que consumem água regularmente e realizam exercícios acima de 5 horas durante a semana.

create trigger t_attAlunoAtivo
after insert or update on lembretes
for each row
execute procedure att_AlunoAtivo();


create or replace function att_AlunoAtivo() returns trigger
as
$$
begin
	refresh materialized view Aluno_Ativo;
	return NULL;
end
$$
language plpgsql;

create trigger t_attAlunoAtivo2
after insert or update on relatorio_semana
for each row
execute procedure att_AlunoAtivo2();

create or replace function att_AlunoAtivo2() returns trigger
as
$$
begin
	refresh materialized view Aluno_Ativo;
	return NULL;
end
$$
language plpgsql;

-- Procedures

-- Procedure Novo Usuário: Cadastra um novo usuário na tabela Usuarios do banco de dados.
create or replace procedure novoUsuario (peso float, altura float) as
$$
declare
	maximo int;
begin
	select max(id) from usuarios into maximo;
	insert into usuarios values (maximo + 1, peso, altura);
end;

$$ language plpgsql;

call novoUsuario (90, 1.90);