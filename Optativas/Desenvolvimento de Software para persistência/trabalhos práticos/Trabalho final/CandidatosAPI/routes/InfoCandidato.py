from fastapi import APIRouter, HTTPException, Query, Request, status, Depends
from typing import Annotated
from models.infoCandidato import InfoCandidatoCreate, InfoCandidatoBase, InfoCandidatoPublic, InfoCandidatoUpdate
from pymongo.collection import Collection
from pymongo import ReturnDocument
from typing import List, Optional
import logging


from schemas.infoCandidato import info_candidato_entity, info_candidatos_entity

ERROR_DETAIL = "Some error occurred: {e}"
NOT_FOUND = "Not found"

async def get_info_candidato_collection(request: Request) -> Collection:
    """Returns the info candidato collection from MongoDB"""
    return request.app.database["infoCandidato"]

InfoCandidatoCollection = Annotated[Collection, Depends(get_info_candidato_collection)]

logger = logging.getLogger("app_logger")
router = APIRouter()


@router.post("/", 
    response_description="Registers a new InfoCandidato", 
    status_code=status.HTTP_201_CREATED, response_model=InfoCandidatoCreate)
async def create_info_candidato(info_candidato_collection: InfoCandidatoCollection, info_candidato: InfoCandidatoCreate):
    try:
        info_candidato_data = info_candidato.dict()
        result = info_candidato_collection.insert_one(info_candidato_data)
        
        if (created := info_candidato_collection.find_one({"_id": result.inserted_id})) is None:
            raise HTTPException(500, "Failed to create Info Candidato")
            
        return info_candidato_entity(created)
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))
    
@router.get("/", 
    response_description="Retrieves Info Candidatos", 
    response_model=list[InfoCandidatoPublic])
async def read_info_candidatos(
    info_candidato_collection: InfoCandidatoCollection,
    page: Annotated[int, Query(ge=1, description="Pagination offset starting at 1")] = 1,
    limit: Annotated[int, Query(le=100, ge=1, description="Items per page (1-100)")] = 100
):
    cursor = info_candidato_collection.find().skip((page - 1) * limit).limit(limit)
    return info_candidatos_entity(cursor)

@router.get("/count", response_description="Get total Info Candidato count")
async def read_info_candidato_count(info_candidato_collection: InfoCandidatoCollection):
    try:
        return {"count": info_candidato_collection.count_documents({})}
    except Exception as e:
        raise HTTPException(500, detail=ERROR_DETAIL.format(e=e))

@router.get("/{id}",
    response_description="Retrieves Individual Info Candidato by nr_titulo", 
    response_model=InfoCandidatoPublic)
async def read_info_candidato(
    info_candidato_collection: InfoCandidatoCollection, 
    id: int
):
    try:
        if (info_candidato := info_candidato_collection.find_one({"nr_titulo_eleitoral_candidato": id})) is None:
            raise HTTPException(404, detail=NOT_FOUND)
        return info_candidato_entity(info_candidato)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.patch("/{id}",
    response_description="Partially updates an Info Candidato", 
    response_model=InfoCandidatoPublic)
async def update_info_candidato(
    info_candidato_collection: InfoCandidatoCollection, 
    info_candidato: InfoCandidatoUpdate,
    id: int
):
    try:
        update_data = info_candidato.dict(exclude_unset=True)
        
        updated = info_candidato_collection.find_one_and_update(
            {"nr_titulo_eleitoral_candidato": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        
        if not updated:
            raise HTTPException(404, detail=NOT_FOUND)
            
        return info_candidato_entity(updated)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.put("/{id}", 
    response_description="Fully update an Info Candidato", 
    response_model=InfoCandidatoPublic)
async def fully_update_info_candidato(
    info_candidato_collection: InfoCandidatoCollection, 
    info_candidato: InfoCandidatoBase,
    id: int
):
    try:
        update_data = info_candidato.dict()
        
        updated = info_candidato_collection.find_one_and_update(
            {"nr_titulo_eleitoral_candidato": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        
        if not updated:
            raise HTTPException(404, detail=NOT_FOUND)
            
        return info_candidato_entity(updated)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.delete("/{id}",
    response_description="Deletes an Info Candidato")
async def delete_info_candidato(
    info_candidato_collection: InfoCandidatoCollection, 
    id: int
):
    try:
        result = info_candidato_collection.delete_one({"nr_titulo_eleitoral_candidato": id})
        
        if result.deleted_count == 0:
            raise HTTPException(404, detail=NOT_FOUND)
            
        return {"status": "success", "message": "Info Candidato deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))
    

# Filtros

@router.get("/filtrar", response_description="Retrieves Info Candidatos with filters", response_model=List[InfoCandidatoPublic])
async def list_info_candidatos(
    info_candidato_collection: InfoCandidatoCollection,
    ds_nacionalidade: Optional[str] = Query(None, description="Filtrar por descrição da nacionalidade da candidata ou candidato (BRASILEIRA NATURALIZADA, BRASILEIRA NATA, ESTRANGEIRO, NÃO DIVULGÁVEL, PORTUGUESA COM IGUALDADE DE DIREITOS)"),
    nm_municipio_nascimento: Optional[str] = Query(None, description="Filtrar por Nome do município de nascimento da candidata ou candidato."),
    st_quilombola: Optional[bool] = Query(None, description="Filtrar a candidata ou candidato considera-se quilombola (true: Sim, false: Não)"),
    vr_despesa_max_campanha: Optional[float] = Query(None, description="Filtrar por Valor máximo, em reais, de despesas de campanha declarada pelo partido para aquela candidata ou candidato (Números)"),
    st_reeleicao: Optional[bool] = Query(None, description="Filtrar a candidata ou candidato está concorrendo à reeleição (true: Sim, false: Não)"),
    skip: int = Query(ge=0, description="Número de registros para pular", default=0),
    limit: int = Query(ge=1, le=100, description="Número máximo de registros a retornar", default=10)
):
    try:
        # Construir o filtro dinâmico
        query = {}
        
        if ds_nacionalidade:
            query["ds_nacionalidade"] = ds_nacionalidade
        
        if nm_municipio_nascimento:
            query["nm_municipio_nascimento"] = nm_municipio_nascimento
        
        if st_quilombola:
            try:
                query["st_quilombola"] = bool(st_quilombola)
            except ValueError:
                logger.error(f"Parâmetro 'st_quilombola' deve ser um boolean (true: Sim, false: Não)")
                raise HTTPException(status_code=400, detail=f"Parâmetro 'st_quilombola' deve ser um boolean válido (true: Sim, false: Não)")
        
        if vr_despesa_max_campanha:
            try:
                query["vr_despesa_max_campanha"] = float(vr_despesa_max_campanha)
            except ValueError:
                logger.error(f"Parâmetro 'vr_despesa_max_campanha' deve ser um número")
                raise HTTPException(status_code=400, detail=f"Parâmetro 'vr_despesa_max_campanha' deve ser um número válido")
        if st_reeleicao:
            try:
                query["st_reeleicao"] = bool(st_reeleicao)
            except ValueError:
                logger.error(f"Parâmetro 'st_reeleicao' deve ser um boolean (true: Sim, false: Não)")
                raise HTTPException(status_code=400, detail=f"Parâmetro 'st_reeleicao' deve ser um boolean válido (true: Sim, false: Não)")
            
        
        # Executar consulta com paginação
        cursor = info_candidato_collection.find(query).skip(skip).limit(limit)
        
        # Converter para lista de entidades
        info_candidatos = [info_candidatos_entity(info_candidato) for info_candidato in cursor]
        
        # Verificar se encontrou resultados
        if not info_candidatos:
            logger.error(f"Informações do candidatos não encontrada a partir dos filtros.")
            raise HTTPException(404, detail=NOT_FOUND)
        
        logger.info(f"Informações do candidatos encontrada a partir dos filtros.")            
        return info_candidatos
        
    except HTTPException as http_exc:
        # Captura e retorna a exceção específica HTTPException com o código de erro adequado
        raise http_exc
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))