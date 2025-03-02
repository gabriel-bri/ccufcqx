from fastapi import APIRouter, Query, HTTPException
from bson import ObjectId
from typing import List, Dict, Any, Optional
from Models.models import Aula, Modulo
from Database.database import db 

router = APIRouter()

@router.post("/aulas", response_model=Aula)
async def criar_aula(aula: Aula):
    aula_dict = aula.dict(by_alias=True, exclude={"id"})
    
    nova_aula = await db.aulas.insert_one(aula_dict)
    
    aula_criada = await db.aulas.find_one({"_id": nova_aula.inserted_id})
    
    if not aula_criada:
        raise HTTPException(status_code=400, detail="Erro ao criar aula")

    # Converte o `_id` do MongoDB para string antes de retornar
    aula_criada["_id"] = str(aula_criada["_id"])

    return aula_criada

@router.get("/aulas/quantidade")
async def quantidade_aulas():
    total_aulas = await db.aulas.count_documents({})
    return {"quantidade aulas": total_aulas}

@router.get("/aulas/filtrar")
async def filtrar_aulas (
    titulo: Optional[str] = Query(None, min_length=3),
    descricao: Optional[str] = Query(None, min_length=3)
) -> List[Dict]:
    try:
        filtros: Dict = {}
                   
        
        if titulo:
            filtros["titulo"] = {"$regex": titulo, "$options" : "i"}
            
        
        if descricao:
            filtros["descricao"] = {"$regex": descricao, "$options" : "i"}
        
        cursor = db.aulas.find(filtros, {"_id": 0})  # Retorna um cursor assíncrono
        aulas: List[Dict] = await cursor.to_list(length=None) 
        
        return aulas
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro inesperado ao filtrar aulas")
    
    

@router.get("/aulas/paginados", response_model=Dict[str, Any])
async def paginacao_aulas(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    try:
        total = await db.aulas.count_documents({})

        aulas_cursor = db.aulas.find().skip(offset).limit(limit)
        aulas = await aulas_cursor.to_list(length=limit)
        
        for aula in aulas:
            aula["_id"] = str(aula["_id"])
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)

        return {
            "data": aulas,
            "pagination": {
                "total": total,
                "current_page": current_page,
                "total_pages": total_pages,
                "page_size": limit,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao realizar paginação.")

@router.get("/aulas/{aula_id}", response_model=Aula)
async def buscar_aulas_por_id(aula_id: str) -> Dict[str, Any]:
    filtro = {"_id": ObjectId(aula_id)} if ObjectId.is_valid(aula_id) else {"_id": aula_id}

    aula = await db.aulas.find_one(filtro)
    
    

    if not aula:
        raise HTTPException(status_code=404, detail="Aula não encontrada")

    aula["_id"] = str(aula["_id"])
    

    if "modulos" in aula and isinstance(aula["modulos"], list):
        aula["modulos"] = [str(modulo_id) if isinstance(modulo_id, ObjectId) else modulo_id for modulo_id in aula["modulos"]]
        
    if "modulo_id" in aula and isinstance(aula["modulo_id"], ObjectId):
        aula["modulo_id"] = str(aula["modulo_id"])

    return aula

@router.get("/aulas", response_model=List[Aula])
async def listar_aulas():
    aulas = await db.aulas.find().to_list(None)
    
    for aula in aulas:
        aula["_id"] = str(aula["_id"])
        
        # Converte os IDs dos cursos para string, se existirem
        if "modulos" in aula and isinstance(aula["modulos"], list):
            aula["modulos"] = [str(modulo_id) if isinstance(modulo_id, ObjectId) else modulo_id for modulo_id in aula["modulos"]]

    return aulas

@router.put("/aulas/{aula_id}", response_model=Aula)
async def atualizar_aula(aula_id: str, aula: Aula):
    if not ObjectId.is_valid(aula_id):
        raise HTTPException(status_code=400, detail="Id inválido")
    
    aula_dict = aula.dict(by_alias=True, exclude={"id"})
     
    resultado = await db.aulas.update_one({"_id": ObjectId(aula_id)}, {"$set" : aula_dict})
    
    if resultado.matched_count == 0:
        raise HTTPException (status_code=404, detail="Aula não encontrada")
    
    aula_atualizada = await db.aulas.find_one({"_id": ObjectId(aula_id)})
    aula_atualizada["_id"] = str(aula_atualizada["_id"])
    
    return aula_atualizada

@router.delete("/aulas/{aula_id}", status_code=200)
async def excluir_aula(aula_id: str):
    if not ObjectId.is_valid(aula_id):
        raise HTTPException(status_code=400, detail="ID de aula inválida")
    
    aula_obj_id = ObjectId(aula_id)
    
    aula = await db.aulas.find_one({"_id": aula_obj_id})
    if not aula:
        raise HTTPException(status_code=404, detail="Aula não encontrada")
    
    
    delete_resultado = await db.aulas.delete_one({"_id": aula_obj_id})
    if delete_resultado.deleted_count ==0:
        raise HTTPException(status_code=500, detail="Erro ao excluir Aula")
    
    await db.modulos.update.many(
        {"aulas": aula_obj_id},
        {"$pull": {"aulas": aula_obj_id}}
    )
    
    return {"messagem": "Aula excluida e removido do curso com sucesso"}




    
    
