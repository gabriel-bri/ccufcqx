### CandidatosApi
Candidatos API é uma API REST desenvolvida para fornecer acesso a dados relacionados a candidaturas, eleições, partidos, e análises visuais dessas informações. A aplicação foi construída utilizando FastAPI e fornece documentação interativa via Swagger UI para facilitar o consumo dos seus serviços.

## Visão Geral

Esta API permite:
- Gerenciar informações de candidatos e suas candidaturas.
- Realizar análises detalhadas sobre partidos e suas estatísticas.
- Visualizar gráficos interativos de despesas de campanha, distribuição de candidatos e outros insights.
- Consultar e gerenciar dados de eleições, com suporte a filtros e paginação.

## Rotas da API

### Rotas de Candidatura
Essas rotas são responsáveis por operações CRUD (criar, ler, atualizar e deletar) sobre os registros de candidaturas.

- **GET /candidatura/**  
  Lista os candidatos com suporte à paginação (entre 1 e 100 itens por página).

- **GET /candidatura/{id}**  
  Retorna os detalhes de um candidato específico utilizando o campo SQ_CANDIDATO.

- **GET /candidatura/mongoId/{id}**  
  Retorna os dados do candidato utilizando o ObjectId do MongoDB.

- **POST /candidatura/**  
  Cria um novo registro de candidatura.

- **PATCH /candidatura/{id}**  
  Atualiza parcialmente as informações de um candidato.

- **PUT /candidatura/{id}**  
  Substitui integralmente os dados de um candidato.

- **DELETE /candidatura/{id}**  
  Remove um candidato a partir do SQ_CANDIDATO.

### Rotas de Análises de Partidos
Essas rotas oferecem análises e estatísticas sobre os partidos, permitindo insights sobre as candidaturas e revogações.

- **GET /candidatura/cassacoes/motivos**  
  Exibe a contagem de cassações agrupadas pelo motivo.

- **GET /candidatura/partidos/partidos_detalhes**  
  Fornece estatísticas detalhadas dos partidos.

- **GET /candidatura/partidos/candidatos_eleitos**  
  Lista os candidatos eleitos agrupados por partido.

- **GET /candidatura/partidos/partidos_detalhes_por_cargo**  
  Apresenta os detalhes dos partidos segmentados por cargo.

### Rotas de Visualização
Rotas que geram gráficos e visualizações para facilitar a compreensão dos dados.

- **GET /candidatura/chart/party_expenses**  
  Gera um gráfico de barras exibindo as despesas de campanha por partido.

- **GET /candidatura/chart/candidatos_estado**  
  Cria uma visualização distribuindo os candidatos por estado.

- **GET /candidatura/chart/cassacoes_estado**  
  Produz um gráfico que mostra o número de cassações por estado.

- **GET /candidatura/chart/eleitos_estado**  
  Fornece uma visualização dos candidatos eleitos organizados por estado.

### Rotas de Eleição
Rota dedicadas ao gerenciamento e consulta de informações sobre eleições.

- **GET /eleicao/**  
  Lista as eleições com suporte à paginação.

- **GET /eleicao/{id}**  
  Consulta os detalhes de uma eleição específica.

- **POST /eleicao/**  
  Cria um novo registro de eleição.

- **PATCH /eleicao/{id}**  
  Atualiza as informações de uma eleição existente.

- **GET /eleicao/search**  
  Permite a busca por eleições através da descrição.

- **GET /eleicao/list**  
  Realiza listagem avançada de eleições com filtros de datas.

## Entidades Principais

### Candidatura
Representa os registros de candidatos registrados na API. Cada candidatura é identificada pelo campo SQ_CANDIDATO e pode ser referenciada tanto pelo ID tradicional quanto pelo ObjectId do MongoDB.

### Partido
Contém informações e estatísticas relacionadas aos partidos políticos, permitindo análises sobre o desempenho e revogações.

### Eleição
Abrange os dados das eleições, com detalhes que possibilitam filtros avançados com base em datas e descrições.

## Funcionalidades Adicionais

- **Validação de Dados**  
  Todas as entradas na API passam por um rigoroso processo de validação para garantir integridade e segurança.

- **Mecanismo de Log**  
  A API implementa logging detalhado para facilitar o monitoramento e resolução de problemas.

- **Swagger UI**  
  Uma interface de documentação interativa, gerada automaticamente pelo FastAPI, permite testar e visualizar facilmente as rotas.

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/josiasdevCandidatosAPI.git
```

2. Baixe a base de dados:
```bash
python get_data.py
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
uvicorn main:app --reload
```

5. Acesse a documentação interativa via Swagger UI em:
```bash
http://localhost:8000/docs
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues para melhorar a API.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
