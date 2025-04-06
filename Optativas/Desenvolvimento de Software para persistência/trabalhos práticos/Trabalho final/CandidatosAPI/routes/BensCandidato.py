from fastapi import APIRouter, HTTPException, Query, Request, status, Depends
from typing import Annotated
from models.BensCandidato import BensCandidatoBase, BensCandidatoCreate, BensCandidatoPublic, BensCandidatoUpdate
from pymongo.collection import Collection
from pymongo import ReturnDocument
from datetime import date, time
from utils.utils import validate_object_id
from schemas.BensCandidato import bens_candidato_entity_from_db, bens_candidato_entities_from_db
from schemas.Candidatura import candidatura_entity_from_db
import logging
from bson import ObjectId

ERROR_DETAIL = "Some error occurred: {e}"
NOT_FOUND = "Not found"

async def get_bens_candidato_collection(request: Request) -> Collection:
    """Returns the bens_candidato collection from MongoDB"""
    return request.app.database["bens_candidato"]

BensCandidatoCollection = Annotated[Collection, Depends(get_bens_candidato_collection)]

async def get_candidatura_collection(request: Request) -> Collection:
    """Returns the candidatura collection from MongoDB"""
    return request.app.database["candidatura"]

CandidaturaCollection = Annotated[Collection, Depends(get_candidatura_collection)]

logger = logging.getLogger("app_logger")



router = APIRouter()

@router.post("/", 
    response_description="Registers a new BensCandidato", 
    status_code=status.HTTP_201_CREATED, response_model=BensCandidatoPublic)
async def create_bens_candidato(bens_candidato_collection: BensCandidatoCollection, bens_candidato: BensCandidatoCreate):
    try:
        bens_candidato_data = bens_candidato.model_dump()
        
        # Converte campos datetime.date para string
        if isinstance(bens_candidato_data['dt_ult_atual_bem_candidato'], date):
            bens_candidato_data['dt_ult_atual_bem_candidato'] = bens_candidato_data['dt_ult_atual_bem_candidato'].isoformat()
        
        # Converte campos datetime.time para string
        if isinstance(bens_candidato_data['hh_ult_atual_bem_candidato'], time):
            bens_candidato_data['hh_ult_atual_bem_candidato'] = bens_candidato_data['hh_ult_atual_bem_candidato'].isoformat()
        
        result = bens_candidato_collection.insert_one(bens_candidato_data)
        
        if (created := bens_candidato_collection.find_one({"_id": result.inserted_id})) is None:
            raise HTTPException(500, "Failed to create BensCandidato")
        
        logger.info(f"BensCandidato created with id: {result.inserted_id}")
        return bens_candidato_entity_from_db(created)
    except Exception as e:
        logger.error(f"Error creating BensCandidato: {e}")
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.get("/", 
    response_description="Retrieves BensCandidatos", 
    response_model=list[BensCandidatoPublic])
async def read_bens_candidatos(
    bens_candidato_collection: BensCandidatoCollection,
    page: Annotated[int, Query(ge=1, description="Pagination offset starting at 1")] = 1,
    limit: Annotated[int, Query(le=100, ge=1, description="Items per page (1-100)")] = 100
):
    cursor = bens_candidato_collection.find().skip((page - 1) * limit).limit(limit)
    logger.info(f"Retrieved BensCandidatos with pagination - page: {page}, limit: {limit}")
    return bens_candidato_entities_from_db(cursor)


@router.get("/count", response_description="Get total BensCandidato count")
async def read_bens_candidato_count(bens_candidato_collection: BensCandidatoCollection):
    try:
        count = bens_candidato_collection.count_documents({})
        logger.info(f"Total BensCandidato count: {count}")
        return {"count": count}
    except Exception as e:
        logger.error(f"Error retrieving BensCandidato count: {e}")
        raise HTTPException(500, detail=ERROR_DETAIL.format(e=e))

@router.get("/{id}",
    response_description="Retrieves Individual BensCandidato by ID", 
    response_model=BensCandidatoPublic)
async def read_bens_candidato(
    bens_candidato_collection: BensCandidatoCollection, 
    id: str = Depends(validate_object_id)
):
    try:
        if (bens_candidato := bens_candidato_collection.find_one({"_id": id})) is None:
            logger.warning(f"BensCandidato with id {id} not found")
            raise HTTPException(404, detail=NOT_FOUND)
        logger.info(f"Retrieved BensCandidato with id: {id}")
        return bens_candidato_entity_from_db(bens_candidato)
    except Exception as e:
        logger.error(f"Error retrieving BensCandidato with id {id}: {e}")
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.patch("/{id}",
    response_description="Partially updates a BensCandidato", 
    response_model=BensCandidatoPublic)
async def update_bens_candidato(
    bens_candidato_collection: BensCandidatoCollection, 
    bens_candidato: BensCandidatoUpdate,
    id: str = Depends(validate_object_id)
):
    try:
        update_data = bens_candidato.model_dump(exclude_unset=True)
        
        # Converte campos datetime.date para string
        if 'dt_ult_atual_bem_candidato' in update_data and isinstance(update_data['dt_ult_atual_bem_candidato'], date):
            update_data['dt_ult_atual_bem_candidato'] = update_data['dt_ult_atual_bem_candidato'].isoformat()
        
        # Converte campos datetime.time para string
        if 'hh_ult_atual_bem_candidato' in update_data and isinstance(update_data['hh_ult_atual_bem_candidato'], time):
            update_data['hh_ult_atual_bem_candidato'] = update_data['hh_ult_atual_bem_candidato'].isoformat()
        
        updated = bens_candidato_collection.find_one_and_update(
            {"_id": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        
        if not updated:
            logger.warning(f"BensCandidato with id {id} not found for update")
            raise HTTPException(404, detail=NOT_FOUND)
        
        logger.info(f"BensCandidato with id {id} updated")
        return bens_candidato_entity_from_db(updated)
    except Exception as e:
        logger.error(f"Error updating BensCandidato with id {id}: {e}")
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.put("/{id}", 
    response_description="Fully update a BensCandidato", 
    response_model=BensCandidatoPublic)
async def fully_update_bens_candidato(
    bens_candidato_collection: BensCandidatoCollection, 
    bens_candidato: BensCandidatoBase,
    id: str = Depends(validate_object_id)
):
    try:
        update_data = bens_candidato.model_dump()
        
        # Converte campos datetime.date para string
        if 'dt_ult_atual_bem_candidato' in update_data and isinstance(update_data['dt_ult_atual_bem_candidato'], date):
            update_data['dt_ult_atual_bem_candidato'] = update_data['dt_ult_atual_bem_candidato'].isoformat()
        
        # Converte campos datetime.time para string
        if 'hh_ult_atual_bem_candidato' in update_data and isinstance(update_data['hh_ult_atual_bem_candidato'], time):
            update_data['hh_ult_atual_bem_candidato'] = update_data['hh_ult_atual_bem_candidato'].isoformat()
        
        updated = bens_candidato_collection.find_one_and_update(
            {"_id": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        
        if not updated:
            logger.warning(f"BensCandidato with id {id} not found for full update")
            raise HTTPException(404, detail=NOT_FOUND)
        
        logger.info(f"BensCandidato with id {id} fully updated")
        return bens_candidato_entity_from_db(updated)
    except Exception as e:
        logger.error(f"Error fully updating BensCandidato with id {id}: {e}")
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.delete("/{id}",
    response_description="Deletes a BensCandidato")
async def delete_bens_candidato(
    bens_candidato_collection: BensCandidatoCollection, 
    id: str = Depends(validate_object_id)
):
    try:
        result = bens_candidato_collection.delete_one({"_id": id})
        
        if result.deleted_count == 0:
            logger.warning(f"BensCandidato with id {id} not found for deletion")
            raise HTTPException(404, detail=NOT_FOUND)
        
        logger.info(f"BensCandidato with id {id} deleted successfully")
        return {"status": "success", "message": "BensCandidato deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting BensCandidato with id {id}: {e}")
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))
    

# @router.get("/media/todos", response_description="Calcula a média dos bens de todos os candidatos com paginação")
# async def calcular_media_todos_candidatos(
#     bens_candidato_collection: BensCandidatoCollection,
#     ordem: str = Query("desc", enum=["asc", "desc"]),  # Ordenação opcional
#     limit: int = Query(10, ge=1, le=100),  # Limite de resultados por página (1 a 100)
#     page: int = Query(1, ge=1)  # Página atual (mínimo 1)
# ):
#     try:
#         skip = (page - 1) * limit  # Cálculo do offset para paginação

#         pipeline = [
#             {
#                 "$group": {
#                     "_id": "$sq_candidato",
#                     "media_bens": {"$avg": "$vr_bem_candidato"}
#                 }
#             },
#             {
#                 "$sort": {"media_bens": 1 if ordem == "asc" else -1}  # Ordenação crescente/decrescente
#             },
#             {
#                 "$skip": skip  # Pular registros para paginação
#             },
#             {
#                 "$limit": limit  # Limitar número de registros retornados
#             }
#         ]
#         result = list(bens_candidato_collection.aggregate(pipeline))

#         if not result:
#             logger.warning("Nenhum bem encontrado para candidatos nesta página")
#             raise HTTPException(status_code=404, detail="Nenhum bem encontrado para esta página")

#         # Formatando o retorno
#         candidatos_media = [{"sq_candidato": r["_id"], "media_bens": r["media_bens"]} for r in result]

#         logger.info(f"Página {page} carregada com sucesso ({len(candidatos_media)} candidatos).")
#         return {
#             "pagina_atual": page,
#             "limite_por_pagina": limit,
#             "total_resultados": len(candidatos_media),
#             "dados": candidatos_media
#         }

#     except Exception as e:
#         logger.error(f"Erro ao calcular média com paginação: {e}")
#         raise HTTPException(status_code=500, detail=f"Erro ao calcular média: {e}")

# @router.get("/bens/{sq_candidato}", response_description="Lista os bens de um candidato específico")
# async def listar_bens_candidato(
#     sq_candidato: str,
#     bens_candidato_collection: BensCandidatoCollection
# ):
#     bens = list(bens_candidato_collection.find({"sq_candidato": sq_candidato}, {"_id": 0}))

#     if not bens:
#         raise HTTPException(status_code=404, detail="Nenhum bem encontrado para este candidato")

#     return {"sq_candidato": sq_candidato, "bens": bens}

# //////////////tudo abaixo sao tentativas//////////////////////////////////


@router.get("/candidatura/{id}/bens", response_description="Recupera uma candidatura por ID e calcula a média dos bens de todos os candidatos")
async def read_candidatura_e_calcular_media(
    candidatura_collection: CandidaturaCollection,
    bens_candidato_collection: BensCandidatoCollection,
    id: int,
    ordem: str = Query("desc", enum=["asc", "desc"], description="Ordenação da média dos bens"),
    limit: int = Query(10, ge=1, le=100, description="Limite de resultados por página"),
    page: int = Query(1, ge=1, description="Número da página")
):
    try:
    
        # Recupera a candidatura específica por ID
        if (candidatura := candidatura_collection.find_one({"sq_candidato": id})) is None:
            raise HTTPException(404, detail=NOT_FOUND)
        candidatura_data = candidatura_entity_from_db(candidatura)

        
        # Calcula a média dos bens de todos os candidatos com paginação
        skip = (page - 1) * limit
        pipeline = [
            {"$group": {"_id": id, "media_bens": {"$avg": "$vr_bem_candidato"}}},
            {"$sort": {"media_bens": 1 if ordem == "asc" else -1}},
            {"$skip": skip},
            {"$limit": limit}
        ]
        result = list(bens_candidato_collection.aggregate(pipeline))
        
        if not result:
            raise HTTPException(status_code=404, detail="Nenhum bem encontrado para esta página")
        
        def format_currency(value):
            return "{:,.2f}".format(value).replace(",", "X").replace(".", ",").replace("X", ".")
        
        candidatos_media = [{ "media_bens": format_currency(round(r["media_bens"], 2))} for r in result]

    
        
        return {
            "candidatura": candidatura_data,
            "pagina_atual": page,
            "limite_por_pagina": limit,
            "total_resultados": len(candidatos_media),
            "dados": candidatos_media
        }
    

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao recuperar candidatura e calcular média dos bens: {e}")