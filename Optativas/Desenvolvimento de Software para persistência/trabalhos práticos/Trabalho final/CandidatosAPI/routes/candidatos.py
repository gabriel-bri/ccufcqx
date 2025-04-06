from fastapi import APIRouter, HTTPException, Query, Request, status, Depends
from typing import Annotated
from models.candidato import CandidatoCreate, CandidatoBase, CandidatoPublic, CandidatoUpdate
from pymongo.collection import Collection
from pymongo import ReturnDocument
import logging
from schemas.candidato import candidato_entity, candidato_entities

ERROR_DETAIL = "Some error occurred: {e}"
NOT_FOUND = "Not found"

async def get_candidato_collection(request: Request) -> Collection:
    """Returns the candidato collection from MongoDB"""
    return request.app.database["candidato"]

CandidatoCollection = Annotated[Collection, Depends(get_candidato_collection)]

router = APIRouter()
logger = logging.getLogger("app_logger")

@router.post("/", 
    response_description="Registers a new Candidato", 
    status_code=status.HTTP_201_CREATED, response_model=CandidatoCreate)
async def create_candidato(accident_collection: CandidatoCollection, accident: CandidatoCreate):
    try:
        accident_data = accident.model_dump()
        result = accident_collection.insert_one(accident_data)
        
        if (created := accident_collection.find_one({"_id": result.inserted_id})) is None:
            logger.error("Failed to create Candidato")
            raise HTTPException(500, "Failed to create Candidato")
        logger.info("New candidato inserted")
        return candidato_entity(created)
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.get("/filter")
async def filter_candidatos_by_name(
    candidato_collection: CandidatoCollection,
    name: str | None = None,  
    page: int = 1,
    limit: int = 100
):
    try:
        query_filter = {}

        if name:
            query_filter['nm_candidato'] = {"$regex": name, "$options": "i"}

        skip = (page - 1) * limit
        results = candidato_collection.find(query_filter).skip(skip).limit(limit).to_list()
        if not results:
            logger.error(NOT_FOUND)
            raise HTTPException(404, detail=NOT_FOUND)

        logger.info("Filtering candidato using filters")
        return candidato_entities(results)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.get("/", 
    response_description="Retrieves Candidatos", 
    response_model=list[CandidatoPublic])
async def read_candidatos(
    candidato_collection: CandidatoCollection,
    page: Annotated[int, Query(ge=1, description="Pagination offset starting at 1")] = 1,
    limit: Annotated[int, Query(le=100, ge=1, description="Items per page (1-100)")] = 100
):
    try:
        cursor = candidato_collection.find().skip((page - 1) * limit).limit(limit)
        logger.info("Retriving candidato data")
        return candidato_entities(cursor)
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(500, detail=ERROR_DETAIL.format(e=e))    

@router.get("/count", response_description="Get total Candidato count")
async def read_candidato_count(candidato_collection: CandidatoCollection):
    try:
        logger.info("Getting total candidatos")
        return {"count": candidato_collection.count_documents({})}
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(500, detail=ERROR_DETAIL.format(e=e))

@router.get("/{id}",
    response_description="Retrieves Individual Candidato by nr_titulo", 
    response_model=CandidatoPublic)
async def read_candidato(
    candidato_collection: CandidatoCollection, 
    id: int
):
    try:
        if (candidato := candidato_collection.find_one({"nr_titulo_eleitoral_candidato": id})) is None:
            logger.error(NOT_FOUND)
            raise HTTPException(404, detail=NOT_FOUND)
        logger.info("Retrieves Individual Candidato by nr_titulo")
        return candidato_entity(candidato)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.patch("/{id}",
    response_description="Partially updates an Candidato", 
    response_model=CandidatoPublic)
async def update_candidato(
    candidato_collection: CandidatoCollection, 
    candidato: CandidatoUpdate,
    id: int
):
    try:
        update_data = candidato.model_dump(exclude_unset=True)
        
        updated = candidato_collection.find_one_and_update(
            {"nr_titulo_eleitoral_candidato": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        
        if not updated:
            logger.error(NOT_FOUND)
            raise HTTPException(404, detail=NOT_FOUND)
            
        return candidato_entity(updated)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.put("/{id}", 
    response_description="Fully update an Candidato", 
    response_model=CandidatoPublic)
async def fully_update_candidato(
    candidato_collection: CandidatoCollection, 
    candidato: CandidatoBase,
    id: int
):
    try:
        update_data = candidato.model_dump()
        
        updated = candidato_collection.find_one_and_update(
            {"nr_titulo_eleitoral_candidato": id},
            {"$set": update_data},
            return_document=ReturnDocument.AFTER
        )
        
        if not updated:
            logger.error(NOT_FOUND)
            raise HTTPException(404, detail=NOT_FOUND)
        logger.info("Fully update an Candidato")    
        return candidato_entity(updated)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))

@router.delete("/{id}",
    response_description="Deletes an Candidato")
async def delete_candidato(
    candidato_collection: CandidatoCollection, 
    id: int
):
    try:
        result = candidato_collection.delete_one({"nr_titulo_eleitoral_candidato": id})
        
        if result.deleted_count == 0:
            raise HTTPException(404, detail=NOT_FOUND)
            
        return {"status": "success", "message": "Candidato deleted successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(ERROR_DETAIL.format(e=e))
        raise HTTPException(status_code=500, detail=ERROR_DETAIL.format(e=e))