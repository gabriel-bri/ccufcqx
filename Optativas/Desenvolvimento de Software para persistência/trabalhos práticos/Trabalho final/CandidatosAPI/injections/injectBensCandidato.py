import sys
import zipfile
import pandas as pd
from pathlib import Path

# Ajusta o diretório raiz do projeto no sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from schemas.BensCandidato import bens_candidato_entity
from config.database import mongodb_client

ZIP_PATH = '../resources/bem_candidato_2024.zip'
CSV_FILENAME = 'bem_candidato_2024_BRASIL.csv'

ZIP_PATH_CANDIDATO = '../resources/consulta_cand_2024.zip'
CSV_FILENAME_CANDIDATO = 'consulta_cand_2024_BRASIL.csv'

with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
    with zip_ref.open(CSV_FILENAME) as csv_file:
        benscandidato = pd.read_csv(csv_file, sep=';', encoding='cp1252')
        benscandidato = benscandidato[
            [
                'SQ_CANDIDATO',
                'NR_ORDEM_BEM_CANDIDATO',
                'DS_TIPO_BEM_CANDIDATO',
                'DS_BEM_CANDIDATO',
                'VR_BEM_CANDIDATO',
                'DT_ULT_ATUAL_BEM_CANDIDATO',
                'HH_ULT_ATUAL_BEM_CANDIDATO'
            ]
        ]

with zipfile.ZipFile(ZIP_PATH_CANDIDATO, 'r') as zip_ref:
    with zip_ref.open(CSV_FILENAME_CANDIDATO) as csv_file:
        candidato = pd.read_csv(csv_file, sep=';', encoding='cp1252')
        candidato = candidato[
            [
                'NR_TITULO_ELEITORAL_CANDIDATO',
                'SQ_CANDIDATO'
            ]
        ]

# Mescla os DataFrames
merged_df = pd.merge(benscandidato, candidato, on='SQ_CANDIDATO')
merged_df.columns = merged_df.columns.str.lower()

# Ajuste de tipos para ficar compatível com o modelo
merged_df['sq_candidato'] = merged_df['sq_candidato'].astype(str)
merged_df['nr_titulo_eleitoral_candidato'] = merged_df['nr_titulo_eleitoral_candidato'].astype(str)

# VR_BEM_CANDIDATO -> substitui vírgula por ponto e converte pra float
merged_df['vr_bem_candidato'] = (
    merged_df['vr_bem_candidato'].str.replace(',', '.').astype(float)
)

# Ajusta data (dd/mm/yyyy) para conter só a data
merged_df['dt_ult_atual_bem_candidato'] = pd.to_datetime(
    merged_df['dt_ult_atual_bem_candidato'],
    format='%d/%m/%Y',
    errors='coerce'
).dt.date  # manter apenas o dia/mês/ano

# Converte dt_ult_atual_bem_candidato para string
merged_df['dt_ult_atual_bem_candidato'] = merged_df['dt_ult_atual_bem_candidato'].astype(str)

# Ajusta hora (HH:MM:SS) para conter só o horário
# Como o PyMongo não salva datetime.time diretamente, convertemos para string
merged_df['hh_ult_atual_bem_candidato'] = pd.to_datetime(
    merged_df['hh_ult_atual_bem_candidato'],
    format='%H:%M:%S',
    errors='coerce'
).dt.strftime('%H:%M:%S')  # manter apenas o horário

print(merged_df.head())
print(merged_df.dtypes)
print(merged_df.count())
print(merged_df.isnull().sum())

db = mongodb_client['eleicoes']
collection = db['bens_candidato']

# Insere no MongoDB, tudo convertendo a dict
for _, row in merged_df.iterrows():
    entity = bens_candidato_entity(row.to_dict())
    collection.insert_one(entity)

print("Dados inseridos com sucesso!")
