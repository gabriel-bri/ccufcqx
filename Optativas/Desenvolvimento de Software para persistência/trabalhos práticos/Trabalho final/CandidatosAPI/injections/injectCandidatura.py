import sys
import zipfile
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))  # Adiciona o diretório raiz do projeto ao sys.path
from schemas.Candidatura import candidatura_entity
from config.database import mongodb_client

# Caminhos dos arquivos
ZIP_PATH_CANDIDATO = '../resources/consulta_cand_2024.zip'
CSV_FILENAME_CANDIDATO = 'consulta_cand_2024_BRASIL.csv'

ZIP_PATH_CASSACAO = '../resources/motivo_cassacao_2024.zip'
CSV_FILENAME_CASSACAO = 'motivo_cassacao_2024_BRASIL.csv'

data_array = []

# Carregar dados de candidatura
with zipfile.ZipFile(ZIP_PATH_CANDIDATO, 'r') as zip_ref:
    with zip_ref.open(CSV_FILENAME_CANDIDATO) as csv_file:
        candidatura_df = pd.read_csv(csv_file, sep=';', encoding='cp1252')
        # Converter os nomes das colunas para minúsculas
        candidatura_df.columns = candidatura_df.columns.str.lower()
        candidatura_df = candidatura_df[['sq_candidato', 'nm_candidato', 'cd_eleicao', 'sg_uf', 'ds_cargo', 'nr_candidato',
                                         'nr_partido', 'sg_partido', 'nm_partido', 'nr_turno', 'tp_agremiacao',
                                         'ds_sit_tot_turno']]

# Carregar dados de cassação
with zipfile.ZipFile(ZIP_PATH_CASSACAO, 'r') as zip_ref:
    with zip_ref.open(CSV_FILENAME_CASSACAO) as csv_file:
        cassacao_df = pd.read_csv(csv_file, sep=';', encoding='cp1252')
        # Converter os nomes das colunas para minúsculas
        cassacao_df.columns = cassacao_df.columns.str.lower()
        cassacao_df = cassacao_df[['sq_candidato', 'ds_tp_motivo', 'ds_motivo']]

# Mesclar os DataFrames com base na chave comum 'sq_candidato'
merged_df = pd.merge(candidatura_df, cassacao_df, on='sq_candidato', how='left')

# Preencher valores NaN com strings vazias
merged_df['ds_tp_motivo'] = merged_df['ds_tp_motivo'].fillna('')
merged_df['ds_motivo'] = merged_df['ds_motivo'].fillna('')


print(merged_df.head())
print('\n\n')
print(merged_df.dtypes)
print('\n\n')
print(merged_df.count())
print('\n\n')
print(merged_df.isnull().sum())

# Conectar ao banco MongoDB
db = mongodb_client['eleicoes']
collection = db['candidatura']

for _, row in merged_df.iterrows():
    entity = candidatura_entity(row.to_dict())
    collection.insert_one(entity)

print("Dados inseridos com sucesso!")
