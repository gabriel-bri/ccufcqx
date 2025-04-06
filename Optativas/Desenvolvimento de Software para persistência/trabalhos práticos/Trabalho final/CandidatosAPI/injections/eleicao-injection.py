import zipfile
import pandas as pd
import os
import sys
# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from schemas.eleicao import eleicao_entity
from config.database import mongodb_client
from pydantic import ValidationError

# Caminho dos arquivos ZIP e das colunas desejadas
ZIP_PATH_CANDIDATOS = '../resources/consulta_cand_2024.zip'


# Colunas para realizar o tratamento
colunas_desejadas_candidatos = [
    "CD_ELEICAO", "DS_ELEICAO", "DT_ELEICAO", "ANO_ELEICAO",
    "CD_TIPO_ELEICAO", "NM_TIPO_ELEICAO", "TP_ABRANGENCIA", "NR_TURNO"
]

# ------------ LEITURA DOS ARQUIVOS DE CANDIDATOS ------------
with zipfile.ZipFile(ZIP_PATH_CANDIDATOS, 'r') as zip_ref_candidatos:
    # Filtrar apenas os arquivos CSV que contêm 'BRASIL' no nome
    arquivos_candidatos = [f for f in zip_ref_candidatos.namelist() if f.endswith('.csv') and 'BRASIL' in f]

    if not arquivos_candidatos:
        print("AVISO: Nenhum arquivo CSV contendo 'BRASIL' no nome foi encontrado.")
        sys.exit(1)  # Interrompe o programa caso não encontre arquivos válidos
    
    dataframes_candidatos = []
    for arquivo_candidato in arquivos_candidatos:
        with zip_ref_candidatos.open(arquivo_candidato) as csv_file_candidato:
            try:
                # Lê o CSV apenas com as colunas desejadas
                df_eleicao = pd.read_csv(csv_file_candidato, sep=';', encoding='latin1', usecols=colunas_desejadas_candidatos)
                dataframes_candidatos.append(df_eleicao)
            except ValueError as e:
                print(f"Erro ao ler o arquivo {arquivo_candidato}: {str(e)}")
                sys.exit(1)  # Interrompe o programa imediatamente

# Remover duplicatas com base no código da eleição
df_eleicao_unico = df_eleicao.drop_duplicates(subset=['CD_ELEICAO'])
# Converter a coluna de data  para datetime no formato correto
df_eleicao_unico['DT_ELEICAO'] = pd.to_datetime(df_eleicao_unico['DT_ELEICAO'], format="%d/%m/%Y", errors='coerce')
df_eleicao_unico.columns = df_eleicao_unico.columns.str.lower()
print("Tratamento dos dados finalizados.")
print(f"Total de dados a serem carregados: {df_eleicao_unico.shape[0]}")
print("Inserindo dados no banco. Aguarde...")

# ------------ Inserção no banco de dados ------------
db = mongodb_client['eleicoes']
collection = db['eleicao']
for eleicao in df_eleicao_unico.to_dict(orient="records"):
    try:
        # Criar a instância de EleicaoBase
        dados_eleicao = eleicao_entity(eleicao)

        # Verificar se já existe o cd_eleicao no banco de dados
        if collection.find_one({'cd_eleicao': dados_eleicao['cd_eleicao']}) is not None:
            print(f"Eleição com cd_eleicao {dados_eleicao['cd_eleicao']} já existe no banco de dados.")
        else:
            # Inserir no banco de dados
            result = collection.insert_one(dados_eleicao)  # Inserindo o dicionário

            # Verificar se o documento foi inserido corretamente
            if result.inserted_id:
                print(f"Eleição com cd_eleicao {dados_eleicao['cd_eleicao']} inserida com sucesso!")
            else:
                print("Erro ao inserir os dados no banco.")

    except ValidationError as e:
        print(f"Erro de validação: {e}")
    except Exception as e:
        print(f"Algo deu errado: {e}")
