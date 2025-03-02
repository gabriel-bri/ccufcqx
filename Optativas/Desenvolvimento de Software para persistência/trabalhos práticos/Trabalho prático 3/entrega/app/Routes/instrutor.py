from fastapi import APIRouter, Query, HTTPException
from bson import ObjectId
from typing import List, Dict, Any, Optional
from Models.models import Instrutor
from Database.database import db 

router = APIRouter()

@router.post("/instrutores", response_model=Instrutor)
async def criar_instrutor(instrutor: Instrutor):
    instrutor_dict = instrutor.dict(by_alias=True, exclude={"id"})
    
    novo_instrutor = await db.instrutores.insert_one(instrutor_dict)
    
    instrutor_criado = await db.instrutores.find_one({"_id": novo_instrutor.inserted_id})
    
    if not instrutor_criado:
        raise HTTPException(status_code=400, detail="Erro ao criar Instrutor")

    instrutor_criado["_id"] = str(instrutor_criado["_id"])

    return instrutor_criado

@router.get("/instrutores/quantidade")
async def quantidade_instrutores():
    total_instrutores = await db.instrutores.count_documents({})
    return {"quantidade instrutores": total_instrutores}

@router.get("/instrutores/paginados", response_model=Dict[str, Any])
async def paginacao_instrutores(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    try:
        total = await db.instrutores.count_documents({})

        instrutores_cursor = db.instrutores.find().skip(offset).limit(limit)
        instrutores = await instrutores_cursor.to_list(length=limit)
        
        for instrutor in instrutores:
            instrutor["_id"] = str(instrutor["_id"])
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)

        return {
            "data": instrutores,
            "pagination": {
                "total": total,
                "current_page": current_page,
                "total_pages": total_pages,
                "page_size": limit,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao realizar paginação.")

@router.get("/instrutores/{instrutor_id}", response_model=Instrutor)
async def buscar_instrutores_por_id(instrutor_id: str) -> Dict[str, Any]:
    filtro = {"_id": ObjectId(instrutor_id)} if ObjectId.is_valid(instrutor_id) else {"_id": instrutor_id}

    instrutor = await db.instrutores.find_one(filtro)

    if not instrutor:
        raise HTTPException(status_code=404, detail="Instrutor não encontrado")

    instrutor["_id"] = str(instrutor["_id"])

    if "cursos" in instrutor and isinstance(instrutor["cursos"], list):
        instrutor["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in instrutor["cursos"]
    ]
    
    return instrutor

@router.get("/instrutores", response_model=List[Instrutor])
async def listar_instrutores():
    instrutores = await db.instrutores.find().to_list(None)
    
    for instrutor in instrutores:
        instrutor["_id"] = str(instrutor["_id"])
        
        if "cursos" in instrutor and isinstance(instrutor["cursos"], list):
            instrutor["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in instrutor["cursos"]]

    return instrutores

@router.put("/instrutores/{instrutor_id}", response_model=Instrutor)
async def atualizar_instrutor(instrutor_id: str, instrutor: Instrutor):
    if not ObjectId.is_valid(instrutor_id):
        raise HTTPException(status_code=400, detail="Id inválido")
    
    instrutor_dict = instrutor.dict(by_alias=True, exclude={"id"})
     
    resultado = await db.instrutores.update_one({"_id": ObjectId(instrutor_id)}, {"$set" : instrutor_dict})
    
    if resultado.matched_count == 0:
        raise HTTPException (status_code=404, detail="Instrutor não encontrado")
    
    instrutor_atualizado = await db.instrutores.find_one({"_id": ObjectId(instrutor_id)})
    instrutor_atualizado["_id"] = str(instrutor_atualizado["_id"])
    
    return instrutor_atualizado

@router.delete("/instrutores/{instrutor_id}", status_code=200)
async def excluir_instrutor(instrutor_id: str):
    if not ObjectId.is_valid(instrutor_id):
        raise HTTPException(status_code=400, detail="ID de Instrutor inválido")
    
    instrutor_obj_id = ObjectId(instrutor_id)
    
    instrutor = await db.instrutores.find_one({"_id": instrutor_obj_id})
    if not instrutor:
        raise HTTPException(status_code=404, detail="Instrutor não encontrado")
        
    
    delete_resultado = await db.instrutores.delete_one({"_id": instrutor_obj_id})
    if delete_resultado.deleted_count == 0:
        raise HTTPException(status_code=500, detail="Erro ao excluir Instrutor")
    
    
    return {"messagem": "Instrutor excluido e removido do curso com sucesso"}