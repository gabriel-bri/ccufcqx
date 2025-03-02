from fastapi import APIRouter, Query, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List, Dict, Any, Optional
from Models.models import Aluno
from Database.database import db

router = APIRouter()

@router.post("/alunos", response_model=Aluno)
async def criar_aluno(aluno: Aluno):
    aluno_dict = aluno.dict(by_alias=True, exclude={"id"})
    
    novo_aluno = await db.alunos.insert_one(aluno_dict)
    
    aluno_criado = await db.alunos.find_one({"_id": novo_aluno.inserted_id})
    
    if not aluno_criado:
        raise HTTPException(status_code=400, detail="Erro ao criar aluno")

    # Converte o `_id` do MongoDB para string antes de retornar
    aluno_criado["_id"] = str(aluno_criado["_id"])

    return aluno_criado

@router.get("/alunos/filtrar")
async def filtrar_alunos (
    nome_completo: Optional[str] = Query(None, min_length=3),
    contato_email: Optional[str] = Query(None, min_length=3)
) -> List[Dict]:
    try:
        filtros: Dict = {}
                   
        
        if nome_completo:
            filtros["nome_completo"] = {"$regex": nome_completo, "$options" : "i"}
            
        
        if contato_email:
            filtros["contato_email"] = {"$regex": contato_email, "$options" : "i"}
        
        cursor = db.alunos.find(filtros, {"_id": 0, "cursos": 0, "certificados": 0})
        alunos: List[Dict] = await cursor.to_list(length=None) 
        
        return alunos
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro inesperado ao filtrar alunos")
    

@router.get("/alunos", response_model=List[Aluno])
async def listar_aluno():
    alunos = await db.alunos.find().to_list(None)
    
    for aluno in alunos:
        aluno["_id"] = str(aluno["_id"])
        
        # Converte os IDs dos cursos para string, se existirem
        if "cursos" in aluno and isinstance(aluno["cursos"], list):
            aluno["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in aluno["cursos"]]

    return alunos


@router.get("/alunos/quantidade-total")
async def quantidade_alunos():
    total_alunos = await db.alunos.count_documents({})
    return {"quantidade alunos": total_alunos}

@router.get("/alunos/paginados", response_model=Dict[str, Any])
async def paginacao_alunos(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    try:
        total = await db.alunos.count_documents({})

        alunos_cursor = db.alunos.find().skip(offset).limit(limit)
        alunos = await alunos_cursor.to_list(length=limit)
        
        for aluno in alunos:
            aluno["_id"] = str(aluno["_id"])
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)


        return {
            "data": alunos,
            "pagination": {
                "total": total,
                "current_page": current_page,
                "total_pages": total_pages,
                "page_size": limit,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao realizar paginação.")
    


@router.get("/alunos/{aluno_id}", response_model=Aluno)
async def buscar_aluno_por_id(aluno_id: str) -> Dict[str, Any]:
    try:
        filtro = {"_id": ObjectId(aluno_id)}
    except Exception:
        filtro = {"_id": aluno_id}

    aluno = await db.alunos.find_one(filtro)
    
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    aluno["_id"] = str(aluno["_id"])
    
    if "cursos" in aluno and isinstance(aluno["cursos"], list):
        aluno["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in aluno["cursos"]]
    
    if "certificados" in aluno and isinstance(aluno["certificados"], list):
        aluno["certificados"] = [str(certificado_id) if isinstance(certificado_id, ObjectId) else certificado_id for certificado_id in aluno["certificados"]]

    
    return aluno

@router.put("/alunos/{aluno_id}", response_model=Aluno)
async def atualizar_aluno(aluno_id: str, aluno: Aluno):
    if not ObjectId.is_valid(aluno_id):
        raise HTTPException(status_code=400, detail="Id inválido")
    
    aluno_dict = aluno.dict(by_alias=True, exclude={"id"})
    
    
     
    resultado = await db.alunos.update_one({"_id": ObjectId(aluno_id)}, {"$set" : aluno_dict})
    
    if resultado.matched_count == 0:
        raise HTTPException (status_code=404, detail="Aluno não encontrado")
    
    aluno_atualizado = await db.alunos.find_one({"_id": ObjectId(aluno_id)})
    aluno_atualizado["_id"] = str(aluno_atualizado["_id"])
    
    
    
    return aluno_atualizado

@router.delete("/alunos/{aluno_id}", status_code=200)
async def excluir_aluno(aluno_id: str):
    if not ObjectId.is_valid(aluno_id):
        raise HTTPException(status_code=400, detail="ID de aluno inválido")
    
    aluno_obj_id = ObjectId(aluno_id)
    
    aluno = await db.alunos.find_one({"_id": aluno_obj_id})
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    
    
    delete_resultado = await db.alunos.delete_one({"_id": aluno_obj_id})
    if delete_resultado.deleted_count ==0:
        raise HTTPException(status_code=500, detail="Erro ao excluir aluno")
    
    return {"messagem": "Aluno excluido e removido do curso com sucesso"}



    
