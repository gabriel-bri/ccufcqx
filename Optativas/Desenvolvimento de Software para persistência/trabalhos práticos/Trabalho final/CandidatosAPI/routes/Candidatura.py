from fastapi import APIRouter, HTTPException, Query, Request, status, Depends
from typing import Annotated, Dict, List
from models.Candidatura import CandidaturaBase, CandidaturaCreate, CandidaturaPublic, CandidaturaUpdate
from pymongo.collection import Collection
from pymongo import ReturnDocument
from utils.utils import validate_object_id
from schemas.Candidatura import candidatura_entity_from_db, candidatura_entities_from_db
import logging

ERROR_DETAIL = "Some error occurred: {e}"
NOT_FOUND = "Not found"

async def get_candidatura_collection(request: Request) -> Collection:
    """Returns the candidatura collection from MongoDB"""
    return request.app.database["candidatura"]

CandidaturaCollection = Annotated[Collection, Depends(get_candidatura_collection)]
logger = logging.getLogger("app_logger")

router = APIRouter()

@router.post("/", response_description="Registers a new Candidatura", status_code=status.HTTP_201_CREATED, response_model=CandidaturaPublic)
async def create_candidatura(candidatura_collection: CandidaturaCollection, candidatura: CandidaturaCreate):
    try:
        candidatura_data = candidatura.model_dump()
        result = candidatura_collection.insert_one(candidatura_data)
        created = candidatura_collection.find_one({"_id": result.inserted_id})
        if created is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create Candidatura")
        logger.info(f"Candidatura created with id: {result.inserted_id}")
        return candidatura_entity_from_db(created)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error creating Candidatura: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ERROR_DETAIL.format(e=e))

@router.get("/", response_description="Retrieves Candidaturas", response_model=list[CandidaturaPublic])
async def read_candidaturas(
    candidatura_collection: CandidaturaCollection,
    page: Annotated[int, Query(ge=1, description="Pagination offset starting at 1")] = 1,
    limit: Annotated[int, Query(le=100, ge=1, description="Items per page (1-100)")] = 100
):
    try:
        cursor = candidatura_collection.find().skip((page - 1) * limit).limit(limit)
        logger.info(f"Retrieved Candidaturas with pagination: page={page}, limit={limit}")
        candidatos = list(cursor)
        return candidatura_entities_from_db(candidatos)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error retrieving Candidaturas: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ERROR_DETAIL.format(e=e))

@router.get("/count", response_description="Get total Candidatura count")
async def read_candidatura_count(candidatura_collection: CandidaturaCollection):
    try:
        count = candidatura_collection.count_documents({})
        logger.info(f"Total Candidatura count: {count}")
        return {"count": count}
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error getting Candidatura count: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ERROR_DETAIL.format(e=e))


@router.get("/{id}", response_description="Retrieves Individual Candidatura by SQ_CANDIDATO", response_model=CandidaturaPublic)
async def read_candidatura(candidatura_collection: CandidaturaCollection, id: int):
    try:
        candidatura = candidatura_collection.find_one({"sq_candidato": id})
        if candidatura is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
        logger.info(f"Retrieved Candidatura with sq_candidato: {id}")
        return candidatura_entity_from_db(candidatura)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error retrieving Candidatura with sq_candidato {id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ERROR_DETAIL.format(e=e))


@router.get("/mongoId/{id}", response_description="Retrieves Individual Candidatura by ID of mongo db", response_model=CandidaturaPublic)
async def read_candidatura(candidatura_collection: CandidaturaCollection, id: str = Depends(validate_object_id)):
    try:
        candidatura = candidatura_collection.find_one({"_id": id})
        if candidatura is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
        logger.info(f"Retrieved Candidatura with id: {id}")
        return candidatura_entity_from_db(candidatura)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error retrieving Candidatura with id {id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ERROR_DETAIL.format(e=e))


@router.patch("/{id}", response_description="Partially updates a Candidatura", response_model=CandidaturaPublic)
async def update_candidatura(candidatura_collection: CandidaturaCollection, candidatura: CandidaturaUpdate, id: str = Depends(validate_object_id)):
    try:
        update_data = candidatura.model_dump(exclude_unset=True)
        updated = candidatura_collection.find_one_and_update(
            {"_id": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        if not updated:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
        logger.info(f"Partially updated Candidatura with id: {id}")
        return candidatura_entity_from_db(updated)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error partially updating Candidatura with id {id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ERROR_DETAIL.format(e=e))


@router.put("/{id}", response_description="Fully update a Candidatura", response_model=CandidaturaPublic)
async def fully_update_candidatura(candidatura_collection: CandidaturaCollection, candidatura: CandidaturaBase, id: str = Depends(validate_object_id)):
    try:
        update_data = candidatura.model_dump()
        updated = candidatura_collection.find_one_and_update(
            {"_id": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        if not updated:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
        logger.info(f"Fully updated Candidatura with id: {id}")
        return candidatura_entity_from_db(updated)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error fully updating Candidatura with id {id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ERROR_DETAIL.format(e=e))


@router.delete("/{id}", response_description="Deletes a Candidatura by SQ_CANDIDATO")
async def delete_candidatura(candidatura_collection: CandidaturaCollection, id: int):
    try:
        result = candidatura_collection.delete_one({"sq_candidato": id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NOT_FOUND)
        logger.info(f"Deleted Candidatura with sq_candidato: {id}")
        return {"status": "success", "message": "Candidatura deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error deleting Candidatura with sq_candidato {id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=ERROR_DETAIL.format(e=e))


# Conta cassações agrupadas pelo motivo específico
@router.get("/cassacoes/motivos", response_description="Retrieve cassation counts grouped by specific reason")
async def get_cassacoes_by_motivo(candidatura_collection: Collection = Depends(get_candidatura_collection)) -> List[Dict]:
    try:
        pipeline = [
            {"$match": {
                "ds_motivo": {"$ne": "", "$exists": True}  # Ignora registros sem motivo definido
            }},
            {"$group": {
                "_id": "$ds_motivo",
                "total_cassacoes": {"$sum": 1}
            }},
            {"$sort": {"total_cassacoes": -1}}  # Ordena do maior para o menor número de cassações
        ]

        result = list(candidatura_collection.aggregate(pipeline))

        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No cassations found")

        return [
            {
                "motivo": item["_id"],
                "total_cassacoes": item["total_cassacoes"]
            }
            for item in result
        ]
    except Exception as e:
        logger.error(f"Error retrieving cassation count by reason: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Some error occurred: {e}")
    
@router.get("/partidos/partidos_detalhes", response_description="Retrieve simplified party details with situation counts and total candidates")
async def get_partido_detalhes_simplificado(candidatura_collection: Collection = Depends(get_candidatura_collection)) -> List[Dict]:
    try:
        pipeline = [
            {
                "$group": {
                    "_id": {
                        "partido": "$nr_partido",
                        "situacao": "$ds_sit_tot_turno"
                    },
                    "count": {"$sum": 1},
                    "nome_partido": {"$first": "$nm_partido"}
                }
            },
            {
                "$match": {
                    "_id.situacao": {"$nin": ["#NULO", "#NULO#"]}
                }
            },
            {
                "$group": {
                    "_id": "$_id.partido",
                    "situacoes": {
                        "$push": {
                            "k": "$_id.situacao",
                            "v": "$count"
                        }
                    },
                    "nome_partido": {"$first": "$nome_partido"},
                    "total_candidaturas": {"$sum": "$count"}  # Adiciona o total de candidaturas por partido
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "numero_partido": "$_id",
                    "nome_partido": 1,
                    "situacoes": {"$arrayToObject": "$situacoes"},
                    "total_candidaturas": 1  # Inclui o total de candidaturas
                }
            },
            {
                "$sort": {"numero_partido": 1}
            }
        ]

        result = list(candidatura_collection.aggregate(pipeline))

        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No party details found")

        return result

    except Exception as e:
        logger.error(f"Error retrieving simplified party details: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Some error occurred: {e}")

@router.get("/partidos/candidatos_eleitos", response_description="Retrieve simplified party details with situation counts")
async def get_partido_detalhes_simplificado(candidatura_collection: Collection = Depends(get_candidatura_collection)) -> List[Dict]:
    try:
        pipeline = [
            {
                "$group": {
                    "_id": {
                        "partido": "$nr_partido",
                        "situacao": "$ds_sit_tot_turno"
                    },
                    "count": {"$sum": 1},
                    "nome_partido": {"$first": "$nm_partido"}
                }
            },
            {
                "$match": {
                    "_id.situacao": {"$nin": ["#NULO", "#NULO#", "NÃO ELEITO", "2º TURNO", "SUPLENTE"]}
                }
            },
            {
                "$group": {
                    "_id": "$_id.partido",
                    "situacoes": {
                        "$push": {
                            "k": "$_id.situacao",
                            "v": "$count"
                        }
                    },
                    "nome_partido": {"$first": "$nome_partido"},
                    "total_eleitos": {
                        "$sum": {
                            "$cond": [
                                {"$in": ["$_id.situacao", ["ELEITO", "ELEITO POR MÉDIA", "ELEITO POR QP"]]},
                                "$count",
                                0
                            ]
                        }
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "numero_partido": "$_id",
                    "nome_partido": 1,
                    "total_eleitos": 1,
                    "situacoes": {"$arrayToObject": "$situacoes"}
                }
            },
            {
                "$sort": {"numero_partido": 1}
            }
        ]

        result = list(candidatura_collection.aggregate(pipeline))

        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No party details found")

        return result

    except Exception as e:
        logger.error(f"Error retrieving simplified party details: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Some error occurred: {e}")

@router.get("/partidos/partidos_detalhes_por_cargo", response_description="Retrieve party details with situation counts per cargo")
async def get_partido_detalhes_por_cargo(candidatura_collection: Collection = Depends(get_candidatura_collection)) -> List[Dict]:
    try:
        pipeline = [
            {
                "$group": {
                    "_id": {
                        "partido": "$nr_partido",
                        "cargo": "$ds_cargo",
                        "situacao": "$ds_sit_tot_turno"
                    },
                    "count": {"$sum": 1},
                    "nome_partido": {"$first": "$nm_partido"}
                }
            },
            {
                "$match": {
                    "_id.situacao": {"$nin": ["#NULO", "#NULO#"]}
                }
            },
            {
                "$group": {
                    "_id": {
                        "partido": "$_id.partido",
                        "cargo": "$_id.cargo"
                    },
                    "situacoes": {
                        "$push": {
                            "k": "$_id.situacao",
                            "v": "$count"
                        }
                    },
                    "nome_partido": {"$first": "$nome_partido"}
                }
            },
            {
                "$sort": {
                    "_id.partido": 1,
                    "_id.cargo": 1
                }
            },
            {
                "$group": {
                    "_id": "$_id.partido",
                    "nome_partido": {"$first": "$nome_partido"},
                    "cargos": {
                        "$push": {
                            "cargo": "$_id.cargo",
                            "situacoes": {"$arrayToObject": "$situacoes"}
                        }
                    }
                }
            },
            {
                "$sort": {
                    "_id": 1
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "numero_partido": "$_id",
                    "nome_partido": 1,
                    "cargos": 1
                }
            }
        ]

        result = list(candidatura_collection.aggregate(pipeline))

        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No party details found")

        # Estrutura a resposta para incluir o numero_partido no topo
        response = [
            {
                "numero_partido": item["numero_partido"],
                "nome_partido": item["nome_partido"],
                "cargos": item["cargos"]
            }
            for item in result
        ]

        return response

    except Exception as e:
        logger.error(f"Error retrieving party details by cargo: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Some error occurred: {e}")