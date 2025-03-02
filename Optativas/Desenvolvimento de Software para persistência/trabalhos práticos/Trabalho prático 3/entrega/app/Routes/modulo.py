from fastapi import APIRouter, Query, HTTPException
from bson import ObjectId
from typing import List, Dict, Any, Optional
from Models.models import Modulo
from Database.database import db 

router = APIRouter()

@router.post("/modulos", response_model=Modulo)
async def criar_modulo(modulo: Modulo):
    modulo_dict = modulo.dict(by_alias=True, exclude={"id"})
    
    novo_modulo = await db.modulos.insert_one(modulo_dict)
    
    modulo_criado = await db.modulos.find_one({"_id": novo_modulo.inserted_id})
    
    if not modulo_criado:
        raise HTTPException(status_code=400, detail="Erro ao criar Modulo")

    modulo_criado["_id"] = str(modulo_criado["_id"])

    return modulo_criado

@router.get("/modulos/quantidade")
async def quantidade_modulos():
    total_modulos = await db.modulos.count_documents({})
    return {"quantidade modulos": total_modulos}

@router.get("/modulos/paginados", response_model=Dict[str, Any])
async def paginacao_modulos(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    try:
        total = await db.modulos.count_documents({})

        modulos_cursor = db.modulos.find().skip(offset).limit(limit)
        modulos = await modulos_cursor.to_list(length=limit)
        
        for modulo in modulos:
            modulo["_id"] = str(modulo["_id"])
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)

        return {
            "data": modulos,
            "pagination": {
                "total": total,
                "current_page": current_page,
                "total_pages": total_pages,
                "page_size": limit,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao realizar paginação.")

@router.get("/modulos/{modulo_id}", response_model=Modulo)
async def buscar_modulos_por_id(modulo_id: str) -> Dict[str, Any]:
    filtro = {"_id": ObjectId(modulo_id)} if ObjectId.is_valid(modulo_id) else {"_id": modulo_id}

    modulo = await db.modulos.find_one(filtro)

    if not modulo:
        raise HTTPException(status_code=404, detail="Modulo não encontrado")

    modulo["_id"] = str(modulo["_id"])

    if "cursos" in modulo and isinstance(modulo["cursos"], list):
        modulo["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in modulo["cursos"]
    ]
    
    return modulo

@router.get("/modulos", response_model=List[Modulo])
async def listar_modulos():
    modulos = await db.modulos.find().to_list(None)
    
    for modulo in modulos:
        modulo["_id"] = str(modulo["_id"])
        
        if "cursos" in modulo and isinstance(modulo["cursos"], list):
            modulo["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in modulo["cursos"]]

    return modulos

@router.put("/modulos/{modulo_id}", response_model=Modulo)
async def atualizar_modulo(modulo_id: str, modulo: Modulo):
    if not ObjectId.is_valid(modulo_id):
        raise HTTPException(status_code=400, detail="Id inválido")
    
    modulo_dict = modulo.dict(by_alias=True, exclude={"id"})
     
    resultado = await db.modulos.update_one({"_id": ObjectId(modulo_id)}, {"$set" : modulo_dict})
    
    if resultado.matched_count == 0:
        raise HTTPException (status_code=404, detail="Modulo não encontrado")
    
    modulo_atualizado = await db.modulos.find_one({"_id": ObjectId(modulo_id)})
    modulo_atualizado["_id"] = str(modulo_atualizado["_id"])
    
    return modulo_atualizado

@router.delete("/modulos/{modulo_id}", status_code=200)
async def excluir_modulo(modulo_id: str):
    if not ObjectId.is_valid(modulo_id):
        raise HTTPException(status_code=400, detail="ID de Modulo inválido")
    
    modulo_obj_id = ObjectId(modulo_id)
    
    modulo = await db.modulos.find_one({"_id": modulo_obj_id})
    if not modulo:
        raise HTTPException(status_code=404, detail="Modulo não encontrado")
        
    
    delete_resultado = await db.modulos.delete_one({"_id": modulo_obj_id})
    if delete_resultado.deleted_count == 0:
        raise HTTPException(status_code=500, detail="Erro ao excluir Modulo")
    
    return {"messagem": "Modulo excluido e removido do curso com sucesso"}

