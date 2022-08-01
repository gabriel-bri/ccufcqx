-- Consultas:

-- Consulta 1: As seguintes consultas verificam quais usuários estão dentro das seguntes condições (ordenados do menor peso ao maior peso):

select id, peso, altura
from usuarios
where peso >= 80 and altura >= 1.8
order by peso ASC

select id, peso, altura
from usuarios
where peso <= 80 and altura <= 1.8
order by peso ASC

select id, peso, altura
from usuarios
where peso >= 80 and altura <= 1.8
order by peso ASC

select id, peso, altura
from usuarios
where peso <= 80 and altura >= 1.8
order by peso ASC



-- Consulta 2: Verifica a soma total das horas de exercicios feitos e a media durante aquela semana

select SUM(duracao_em_horas), AVG(duracao_em_horas)
from relatorio_semana


-- Consulta 3: Mostra quais usuarios realizaram as 3 meditações guiadas disponiveis.

select quem_pratica
from meditacao_guiada
where concentracao = 'true' and emocoes = 'true' and estresse = 'true'


-- Consulta 4: Mostras quais usuarios realizaram as posturas com maior nível de dificuldade: Postura da Esfinge, Ponte e Bananeira.

select quem_pratica
from yoga
where postura_da_esfinge = 'true' and ponte = 'true' and bananeira = 'true'


-- Consulta 5: Exibe quais usuários realizaram todos os exercicios de alongamento.

select quem_pratica
from alongamento
where Alongamento_ParteSuperior_do_Corpo and
	Alongamento_Dor_nas_Costas and
	Alongamento_Parte_Inferior_do_Corpo and
	Postura_de_Crianca and
	Alongamento_peito and
	Alongamento_de_Ombros and
	Alongamento_Cobra and
	Alongamento_Triceps and
	Alongamento_Panturrilha = 'true'
