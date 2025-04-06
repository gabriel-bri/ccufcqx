import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import zipfile
import pandas as pd

from config.database import mongodb_client

from schemas.candidato import candidato_entity
from schemas.infoCandidato import info_candidato_entity

from models.candidato import CandidatoCreate
from models.infoCandidato import InfoCandidatoCreate

ZIP_PATH_CANDIDATO = '../resources/consulta_cand_2024.zip'
CSV_FILENAME_CANDIDATO = 'consulta_cand_2024_BRASIL.csv'

ZIP_PATH_CANDIDATO_COMP = '../resources/consulta_cand_complementar_2024.zip'
CSV_FILENAME_CANDIDATO_COMP = 'consulta_cand_complementar_2024_BRASIL.csv'

with zipfile.ZipFile(ZIP_PATH_CANDIDATO, 'r') as zip_ref:
    with zip_ref.open(CSV_FILENAME_CANDIDATO) as csv_file:
        candidatos = pd.read_csv(csv_file, sep=';', encoding='cp1252')
        candidatos.columns = candidatos.columns.str.lower()

        candidatos["dt_nascimento"] = pd.to_datetime(
            candidatos["dt_nascimento"], format="%d/%m/%Y", errors="coerce"
        )

        for key in CandidatoCreate.model_fields.keys():
            candidatos = candidatos[~candidatos[key].isnull()]

        candidatos = candidatos[['nr_titulo_eleitoral_candidato', 'sq_candidato', 'nm_candidato', 'dt_nascimento', 'ds_genero', 'ds_grau_instrucao', 'ds_cor_raca', 'ds_ocupacao']]

with zipfile.ZipFile(ZIP_PATH_CANDIDATO_COMP, 'r') as zip_ref:
    with zip_ref.open(CSV_FILENAME_CANDIDATO_COMP) as csv_file:
        candidatos_comp = pd.read_csv(csv_file, sep=';', encoding='cp1252')
        candidatos_comp.columns = candidatos_comp.columns.str.lower()

        candidatos_comp = pd.merge(candidatos_comp, candidatos, on='sq_candidato')
        
        for key in InfoCandidatoCreate.model_fields.keys():
            candidatos_comp = candidatos_comp[~candidatos_comp[key].isnull()]

        candidatos_comp = candidatos_comp[['nr_titulo_eleitoral_candidato', 'ds_nacionalidade', 'nm_municipio_nascimento', 'st_quilombola', 'vr_despesa_max_campanha', 'st_reeleicao', 'st_declarar_bens', 'st_prest_contas']]

db = mongodb_client['eleicoes']

print(candidatos_comp.dtypes)

info_candidato_collection = db['infoCandidato']
for candidato_comp in candidatos_comp.to_dict(orient="records"):
    try:
        info_candidato_data = info_candidato_entity(candidato_comp)
        info_candidato_collection.insert_one(info_candidato_data)
    except Exception as e:
        print("Something went wrong", e)

collection = db['candidato']
for candidato in candidatos.to_dict(orient="records"):
    try:
        candidato_data = candidato_entity(candidato)
        collection.insert_one(candidato_data)
    except Exception as e:
        print("Something went wrong", e)
