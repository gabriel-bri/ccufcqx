# Imports para o FasTAPI e manipulação de dados
from fastapi import Path, APIRouter, HTTPException, Query, Request, status, Depends, File, UploadFile # File e Upload para envio de arquivos 
from typing import Annotated
from pymongo.collection import Collection
from pymongo import ReturnDocument
from utils.utils import validate_object_id
# Models e schemas
from models.eleicao import EleicaoCreate, EleicaoBase, EleicaoPublic, EleicaoUpdate
from schemas.eleicao import eleicao_entity_from_db, eleicao_entities_from_db, eleicao_entity
# Outros imports
from datetime import datetime
from typing import List, Optional
import logging
# Para abrir os arquivos zip e csv
import zipfile 
from io import BytesIO
import pandas as pd

from models.candidato import CandidatoCreate, CandidatoBase, CandidatoPublic, CandidatoUpdate
from schemas.candidato import candidato_entity, candidato_entities
from models.Candidatura import CandidaturaBase, CandidaturaCreate, CandidaturaPublic, CandidaturaUpdate
from schemas.Candidatura import candidatura_entity_from_db, candidatura_entities_from_db

async def get_candidato_collection(request: Request) -> Collection:
    """Returns the candidato collection from MongoDB"""
    return request.app.database["candidato"]

CandidatoCollection = Annotated[Collection, Depends(get_candidato_collection)]
async def get_candidatura_collection(request: Request) -> Collection:
    """Returns the candidatura collection from MongoDB"""
    return request.app.database["candidatura"]

CandidaturaCollection = Annotated[Collection, Depends(get_candidatura_collection)]

ERROR_DETAIL = "Some error occurred: {e}"
NOT_FOUND = "Not found"

async def get_eleicao_collection(request: Request) -> Collection:
    """Returns the candidato collection from MongoDB"""
    return request.app.database["eleicao"]

EleicaoCollection = Annotated[Collection, Depends(get_eleicao_collection)]

router = APIRouter()

logger = logging.getLogger("app_logger")

# ------------ FUNÇÕES AUXILIDARES ------------
# Função para tratar o arquivo ZIP de candidatos
async def tratar_zip_candidatos(candidatos_file):
    # Definição das colunas desejadas para os candidatos
    colunas_desejadas_candidatos = [
        "CD_ELEICAO", "DS_ELEICAO", "DT_ELEICAO", "ANO_ELEICAO", 
        "CD_TIPO_ELEICAO", "NM_TIPO_ELEICAO", "TP_ABRANGENCIA", "NR_TURNO"
    ]

    # Carregar o arquivo ZIP de Candidatos
    dados_zip_candidatos = await candidatos_file.read()
    with zipfile.ZipFile(BytesIO(dados_zip_candidatos), 'r') as zip_ref_candidatos:
        # Filtrar apenas os arquivos CSV que contêm "BRASIL" no nome
        arquivos_candidatos = [f for f in zip_ref_candidatos.namelist() if f.endswith('.csv') and 'BRASIL' in f]
        
        # Se não encontrar nenhum arquivo com "BRASIL" no nome, lançar erro
        if not arquivos_candidatos:
            logger.error("Nenhum arquivo CSV contendo 'BRASIL' no nome foi encontrado no ZIP.")
            raise HTTPException(status_code=400, detail="Nenhum arquivo CSV contendo 'BRASIL' no nome foi encontrado no ZIP.")
        
        dataframes_candidatos = []
        for arquivo_candidato in arquivos_candidatos:
            with zip_ref_candidatos.open(arquivo_candidato) as csv_file_candidato:
                try:
                    # Ler o CSV com as colunas desejadas
                    df_eleicao = pd.read_csv(csv_file_candidato, sep=';', encoding='latin1', usecols=colunas_desejadas_candidatos)
                    dataframes_candidatos.append(df_eleicao)
                except ValueError as e:
                    logger.error(f"Erro ao ler o arquivo CSV de candidatos: {str(e)}")
                    raise HTTPException(status_code=400, detail=f"Erro ao ler o arquivo CSV de candidatos: {str(e)}")
        
        # Concatenar todos os DataFrames de candidatos
        df_candidatos = pd.concat(dataframes_candidatos, ignore_index=True)
  
    # Remover duplicatas com base no código da eleição    
    df_eleicao_unico = df_eleicao.drop_duplicates(subset=['CD_ELEICAO'])
    # Converter a coluna de data  para datetime no formato correto
    df_eleicao_unico['DT_ELEICAO'] = pd.to_datetime(df_eleicao_unico['DT_ELEICAO'], format="%d/%m/%Y", errors='coerce')
    df_eleicao_unico.columns = df_eleicao_unico.columns.str.lower()
   
    return df_eleicao_unico

# ------------ ROTAS ------------
# Retorna candidatos por ano
@router.get("/candidatos-por-ano", response_description="Retrieve candidates for election year", response_model=List[CandidatoPublic])
async def get_candidates_by_year(
    eleicao_collection: EleicaoCollection,
    candidatura_collection: CandidaturaCollection,
    candidato_collection: CandidatoCollection,
    ano: int = Query(..., description="Ano da eleição para retornar os candidatos"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    try:
        # Pesquisa de eleições pelo ano
        query = {"ano_eleicao": int(ano)}
        
        # Busca as eleições
        eleicao_cursor = eleicao_collection.find(query)
        eleicoes = eleicao_cursor.to_list(length=1000)
        
        if not eleicoes:
            logger.error(f"Eleição não encontrada para o ano {ano}.")
            raise HTTPException(404, detail=NOT_FOUND)
            
        # Extrai os códigos de eleição
        codigos_eleicao = [eleicao["cd_eleicao"] for eleicao in eleicoes]
        
        # Busca candidaturas para esses códigos de eleição
        candidaturas_cursor = candidatura_collection.find(
            {"cd_eleicao": {"$in": codigos_eleicao}}
        )
        candidaturas = candidaturas_cursor.to_list(length=10000)
        
        if not candidaturas:
            logger.error(f"Nenhuma candidatura encontrada para o ano {ano}.")
            raise HTTPException(404, detail="Nenhuma candidatura encontrada")
        
        # Extrai os sq_candidato únicos
        sq_candidatos = list(set(candidatura["sq_candidato"] for candidatura in candidaturas))
        
        # Busca informações dos candidatos
        candidatos_cursor = candidato_collection.find(
            {"sq_candidato": {"$in": sq_candidatos}}
        ).skip(skip).limit(limit)
        
        candidatos = candidatos_cursor.to_list(length=10000)
        
        if not candidatos:
            logger.error(f"Nenhum candidato encontrado para o ano {ano}.")
            raise HTTPException(404, detail="Nenhum candidato encontrado")
        
        # Converte para entidades
        resultado = [candidato_entity(candidato) for candidato in candidatos]
        
        logger.info("Retornando resultados.")
        return resultado
        
    except HTTPException as http_exc:
        raise http_exc
            
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))
        
# Endpoint para filtrar eleições por vários parâmetros
@router.get("/pesquisar", response_description="Search Eleicoes by text", response_model=List[EleicaoPublic])
async def search_eleicoes(
    eleicao_collection: EleicaoCollection,
    busca: str = Query(..., description="Texto para pesquisar na descrição da eleição"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    try:
        # Pesquisa de texto na descrição
        query = {"ds_eleicao": {"$regex": busca, "$options": "i"}}  # Case insensitive
        
        cursor = eleicao_collection.find(query).skip(skip).limit(limit)
        eleicoes = [eleicao_entity_from_db(eleicao) for eleicao in cursor]
        if not eleicoes:
            logger.error(f"Eleição não encontrada a partir da descrição da eleição.")
            raise HTTPException(404, detail=NOT_FOUND)
        logger.error(f"Eleição encontrada a partir da descrição da eleição.")
        return eleicoes
    
    except HTTPException as http_exc:
        # Captura e retorna a exceção específica HTTPException com o código de erro adequado
        raise http_exc
            
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))
    
@router.get("/filtrar", response_description="Retrieves Eleicoes with filters", response_model=List[EleicaoPublic])
async def list_eleicoes(
    eleicao_collection: EleicaoCollection,
    ano: Optional[str] = Query(None, description="Filtrar por ano da eleição (deve ser um número)"),
    abrangencia: Optional[str] = Query(None, description="Filtrar por tipo de abrangência (MUNICIPAL, ESTADUAL, FEDERAL)"),
    data_inicio: Optional[str] = Query(None, description="Data inicial (formato YYYY-MM-DD)"),
    data_fim: Optional[str] = Query(None, description="Data final (formato YYYY-MM-DD)"),
    tipo_eleicao: Optional[str] = Query(None, description="Código do tipo de eleição (deve ser um número)"),
    turno: Optional[str] = Query(None, description="Número do turno (deve ser um número)"),
    skip: int = Query(0, ge=0, description="Número de registros para pular"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a retornar")
):
    try:
        # Construir o filtro dinâmico
        query = {}
        
        if ano:
            try:
                query["ano_eleicao"] = int(ano)
            except ValueError:
                logger.error(f"Parâmetro 'ano' deve ser um número inteiro válido")
                raise HTTPException(status_code=400, detail=f"Parâmetro 'ano' deve ser um número inteiro válido")
            
        if abrangencia:
            query["tp_abrangencia"] = abrangencia
            
        if tipo_eleicao:
            try:
                query["cd_tipo_eleicao"] = int(tipo_eleicao)
            except ValueError:
                logger.error(f"Parâmetro 'tipo_eleicao' deve ser um número inteiro válido")
                raise HTTPException(status_code=400, detail=f"Parâmetro 'tipo_eleicao' deve ser um número inteiro válido")
            
        if turno:
            try:
                query["nr_turno"] = int(turno)
            except ValueError:
                logger.error(f"Parâmetro 'turno' deve ser um número inteiro válido")
                raise HTTPException(status_code=400, detail=f"Parâmetro 'turno' deve ser um número inteiro válido")
            
        # Filtros de data
        date_filter = {}
        if data_inicio:
            try:
                date_filter["$gte"] = datetime.fromisoformat(data_inicio)
            except ValueError:
                logger.error(f"Formato de data inválido para 'data_inicio': Use YYYY-MM-DD")
                raise HTTPException(status_code=400, detail=f"Formato de data inválido para 'data_inicio': Use YYYY-MM-DD")
                
        if data_fim:
            try:
                date_filter["$lte"] = datetime.fromisoformat(data_fim)
            except ValueError:
                logger.error(f"Formato de data inválido para 'data_fim': Use YYYY-MM-DD")
                raise HTTPException(status_code=400, detail=f"Formato de data inválido para 'data_fim': Use YYYY-MM-DD")
                
        if date_filter:
            query["dt_eleicao"] = date_filter
        
        # Executar consulta com paginação
        cursor = eleicao_collection.find(query).skip(skip).limit(limit)
        
        # Converter para lista de entidades
        eleicoes = [eleicao_entity_from_db(eleicao) for eleicao in cursor]
        
        # Verificar se encontrou resultados
        if not eleicoes:
            logger.error(f"Eleição não encontrada a partir dos filtros.")
            raise HTTPException(404, detail=NOT_FOUND)
        
        logger.info(f"Eleição encontrada a partir dos filtros.")            
        return eleicoes
        
    except HTTPException as http_exc:
        # Captura e retorna a exceção específica HTTPException com o código de erro adequado
        raise http_exc
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

# Filtro por data
@router.get("/filtrar/data", response_description="Retrieves Eleicoes using dates", response_model=List[EleicaoPublic])
async def list_eleicoes(
    eleicao_collection: EleicaoCollection,
    data_inicio: Optional[str] = Query(None, description="Data inicial (formato YYYY-MM-DD)"),
    data_fim: Optional[str] = Query(None, description="Data final (formato YYYY-MM-DD)"),
    skip: int = Query(0, ge=0, description="Número de registros para pular"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a retornar")
):
    try:
        # Construir o filtro dinâmico
        query = {}
            
        # Filtros de data
        date_filter = {}
        if data_inicio:
            try:
                date_filter["$gte"] = datetime.fromisoformat(data_inicio)
            except ValueError:
                logger.error(f"Formato de data inválido para 'data_inicio': Use YYYY-MM-DD")
                raise HTTPException(status_code=400, detail=f"Formato de data inválido para 'data_inicio': Use YYYY-MM-DD")
                
        if data_fim:
            try:
                date_filter["$lte"] = datetime.fromisoformat(data_fim)
            except ValueError:
                logger.error(f"Formato de data inválido para 'data_fim': Use YYYY-MM-DD")
                raise HTTPException(status_code=400, detail=f"Formato de data inválido para 'data_fim': Use YYYY-MM-DD")
                
        if date_filter:
            query["dt_eleicao"] = date_filter
        
        # Executar consulta com paginação
        cursor = eleicao_collection.find(query).skip(skip).limit(limit)
        
        # Converter para lista de entidades
        eleicoes = [eleicao_entity_from_db(eleicao) for eleicao in cursor]
        
        # Verificar se encontrou resultados
        if not eleicoes:
            logger.error(f"Eleição não encontrada a partir dos filtros.")
            raise HTTPException(404, detail=NOT_FOUND)
        
        logger.info(f"Eleição encontrada a partir dos filtros.")            
        return eleicoes
        
    except HTTPException as http_exc:
        # Captura e retorna a exceção específica HTTPException com o código de erro adequado
        raise http_exc
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))
    
# Contar registros
@router.get("/count", response_description="Get total Eleição count")
async def read_eleicao_count(eleicao_collection: EleicaoCollection):
    try:
        count = eleicao_collection.count_documents({})
        logger.info(f"Total de eleições armazenadas no banco: {count}")
        return {"count": count}
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(500, detail=ERROR_DETAIL.format(e=e))
    
# Inserção manual de eleição.
@router.post("/", 
    response_description="Registers a new Eleição", 
    status_code=status.HTTP_201_CREATED, response_model=EleicaoCreate)
async def create_eleicao(eleicao_collection: EleicaoCollection, eleicao: EleicaoCreate):
    try:
        eleicao_data = eleicao.model_dump()

        if eleicao_collection.find_one({'cd_eleicao': eleicao_data['cd_eleicao']}) is not None:
            logger.error(f"Eleição com cd_eleicao {eleicao_data['cd_eleicao']} já existe no banco de dados.")
            raise HTTPException(status_code=400, detail=f"Eleição com cd_eleicao {eleicao_data['cd_eleicao']} já existe no banco de dados.")
          
        # Inserir o dado no banco de dados
        result = eleicao_collection.insert_one(eleicao_data)

        # Recuperar o documento inserido usando cd_eleicao
        created = eleicao_collection.find_one({"cd_eleicao": eleicao_data["cd_eleicao"]})
            
        # Caso não tenha encontrado o documento após inserção, lançar erro
        if not created:
            logger.erro("Erro ao criar eleição.")
            raise HTTPException(status_code=500, detail="Erro ao criar Eleição")
        
        logger.info(f"Eleição com cd_eleicao {eleicao_data['cd_eleicao']} inserida no banco de dados.")
        return eleicao_entity_from_db(created)
    
    except HTTPException as http_exc:
        # Captura e retorna a exceção específica HTTPException com o código de erro adequado
        raise http_exc

    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

# Fazer upload de arquivo zip para carregar os dados de eleição.
@router.post("/upload/carregar-dados-eleicao", 
    response_description="Import data to DB using a ZIP file.", 
    status_code=status.HTTP_201_CREATED)
async def upload_dados_eleicao(
    eleicao_collection: EleicaoCollection,
    candidatos_file: UploadFile = File(...)
):
    if not candidatos_file:
        logger.error("É necessário enviar um arquivo ZIP.")
        raise HTTPException(status_code=400, detail="É necessário enviar um arquivo ZIP.")

    if not candidatos_file.filename.endswith(".zip"):
        logger.error("O arquivo enviado não é um ZIP válido.")
        raise HTTPException(status_code=400, detail="O arquivo enviado não é um ZIP válido.")

    try:
        # Processar os dados do arquivo ZIP
        df_eleicao_unico = await tratar_zip_candidatos(candidatos_file)

        # Inserir os registros no banco de dados
        for eleicao in df_eleicao_unico.to_dict(orient="records"):
            dados_eleicao = eleicao_entity(eleicao)

            # Verificar se já existe no banco de dados
            if eleicao_collection.find_one({'cd_eleicao': dados_eleicao['cd_eleicao']}):
                logger.error(f"Eleição com cd_eleicao {dados_eleicao['cd_eleicao']} já existe no banco de dados.")
                raise HTTPException(
                    status_code=400, 
                    detail=f"Eleição com cd_eleicao {dados_eleicao['cd_eleicao']} já existe no banco de dados."
                )

            # Inserir no banco de dados
            eleicao_collection.insert_one(dados_eleicao)
        logger.info(f"Dados importados com sucesso! Total de dados processados: {len(df_eleicao_unico)}")
        return {"message": "Dados importados com sucesso!", "total_registros": len(df_eleicao_unico)}

    except HTTPException as http_exc:
        raise http_exc  # Mantém o status correto

    except Exception as e:
        logger.error(f"Erro ineseperado: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
# Pegar todos os registros
@router.get("/", 
    response_description="Retrieves Eleição", 
    response_model=list[EleicaoPublic])
async def read_eleicoes(
    eleicao_collection: EleicaoCollection,
    page: Annotated[int, Query(ge=1, description="Pagination offset starting at 1")] = 1,
    limit: Annotated[int, Query(le=100, ge=1, description="Items per page (1-100)")] = 100
):
    try:
        cursor = eleicao_collection.find().skip((page - 1) * limit).limit(limit)
        logger.info(f"Recuperando eleições com paginação: page={page}, limit={limit}")
        return eleicao_entities_from_db(cursor)
    except Exception as e:
        logger.error(f"Erro ineseperado: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Deletar uma eleição
@router.delete("/{id}",
    response_description="Deletes a Eleição")
async def delete_cd_eleicao(
    eleicao_collection: EleicaoCollection,
    id: int
):
    try:
        result = eleicao_collection.delete_one({"cd_eleicao": id})
        
        if result.deleted_count == 0:
            logger.error(f"Eleição com o código {id} não encontrada.")
            raise HTTPException(404, detail=NOT_FOUND)
        
        logger.info("Eleção deletada com sucesso.")    
        return {"status": "success", "message": "Eleção deletada com sucesso."}
    except HTTPException as http_exc:
        raise http_exc  # Mantém o status correto
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))
    
# Atualizar eleição
@router.put("/{id}", 
    response_description="Fully update a Eleição", 
    response_model=EleicaoPublic)
async def fully_update_eleicao(
    eleicao_collection: EleicaoCollection, 
    eleicao: EleicaoBase,
    id: int
):
    try:
        update_data = eleicao.model_dump()
        
        updated = eleicao_collection.find_one_and_update(
            {"cd_eleicao": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        
        if not updated:
            logger.error(f"Eleição com o código {id} não encontrada.")
            raise HTTPException(404, detail=NOT_FOUND)
        
        logger.error(f"Eleição atualzada com sucesso")
        return eleicao_entity_from_db(updated)
    except HTTPException as http_exc:
        raise http_exc  # Mantém o status correto
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))
    
# Pegar via cod_eleicao
@router.get("/{id}",
    response_description="Retrieves Individual Eleição by ID", 
    response_model=EleicaoPublic)
async def read_eleicao(
    eleicao_collection: EleicaoCollection, 
    id: int
):
    try:
        if (eleicao := eleicao_collection.find_one({"cd_eleicao": id})) is None:
            logger.error(f"Eleição com o código {id} não encontrada.")
            raise HTTPException(404, detail=NOT_FOUND)
        
        logger.error(f"Recuperando eleição com o código {id}")
        return eleicao_entity_from_db(eleicao)
    
    except HTTPException as http_exc:
        raise http_exc  # Mantém o status correto
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

# Método patch para atualizar
@router.patch("/{id}",
    response_description="Partially updates a Eleição", 
    response_model=EleicaoPublic)
async def update_eleicao(
    eleicao_collection: EleicaoCollection, 
    eleicao: EleicaoUpdate,
    id: int
):
    try:
        update_data = eleicao.model_dump(exclude_unset=True)
        
        updated = eleicao_collection.find_one_and_update(
            {"cd_eleicao": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        
        if not updated:
            logger.error(f"Eleição com o código {id} não encontrada.")
            raise HTTPException(404, detail=NOT_FOUND)
        logger.error(f"Eleição atualzada com sucesso")       
        return eleicao_entity_from_db(updated)
    
    except HTTPException as http_exc:
        raise http_exc  # Mantém o status correto
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))
