from fastapi import APIRouter, Query, HTTPException
from bson import ObjectId
from typing import List, Dict, Any, Optional
from Models.models import Certificado
from Database.database import db 

router = APIRouter()

@router.post("/certificados", response_model=Certificado)
async def criar_certificado(certificado: Certificado):
    certificado_dict = certificado.dict(by_alias=True, exclude={"id"})
    
    novo_certificado = await db.certificados.insert_one(certificado_dict)
    
    certificado_criado = await db.certificados.find_one({"_id": novo_certificado.inserted_id})
    
    if not certificado_criado:
        raise HTTPException(status_code=400, detail="Erro ao criar Certificado")

    certificado_criado["_id"] = str(certificado_criado["_id"])

    return certificado_criado

@router.get("/certificados/paginados", response_model=Dict[str, Any])
async def paginacao_certificados(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    try:
        total = await db.certificados.count_documents({})

        certificados_cursor = db.certificados.find().skip(offset).limit(limit)
        certificados = await certificados_cursor.to_list(length=limit)
        
        for certificado in certificados:
            certificado["_id"] = str(certificado["_id"])
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)

        return {
            "data": certificados,
            "pagination": {
                "total": total,
                "current_page": current_page,
                "total_pages": total_pages,
                "page_size": limit,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao realizar paginação.")

@router.get("/certificados/quantidade")
async def quantidade_certificados():
    total_certificados = await db.certificados.count_documents({})
    return {"quantidade certificados": total_certificados}

@router.get("/certificados/{certificado_id}", response_model=Certificado)
async def buscar_certificados_por_id(certificado_id: str) -> Dict[str, Any]:
    filtro = {"_id": ObjectId(certificado_id)} if ObjectId.is_valid(certificado_id) else {"_id": certificado_id}

    certificado = await db.certificados.find_one(filtro)

    if not certificado:
        raise HTTPException(status_code=404, detail="Certificado não encontrado")

    certificado["_id"] = str(certificado["_id"])

    if "cursos" in certificado and isinstance(certificado["cursos"], list):
        certificado["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in certificado["cursos"]
    ]
    
    if "aluno" in certificado and isinstance(certificado["aluno"], dict):
        if "cursos" in certificado["aluno"] and isinstance(certificado["aluno"]["cursos"], list):
            certificado["aluno"]["cursos"] = [
                str(curso_id) if isinstance(curso_id, ObjectId) else curso_id
                for curso_id in certificado["aluno"]["cursos"]
            ]
    if "curso_id" in certificado and isinstance(certificado["curso_id"], ObjectId): 
        certificado["curso_id"] = str(certificado["curso_id"])
    

    return certificado

@router.get("/certificados", response_model=List[Certificado])
async def listar_certificados():
    certificados = await db.certificados.find().to_list(None)
    
    for certificado in certificados:
        certificado["_id"] = str(certificado["_id"])
        
        if "cursos" in certificado and isinstance(certificado["cursos"], list):
            certificado["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in certificado["cursos"]]
    
        if "aluno" in certificado and isinstance(certificado["aluno"], dict):
            if "cursos" in certificado["aluno"] and isinstance(certificado["aluno"]["cursos"], list):
                certificado["aluno"]["cursos"] = [
                    str(curso_id) if isinstance(curso_id, ObjectId) else curso_id
                    for curso_id in certificado["aluno"]["cursos"]
            ]
            
        if "curso_id" in certificado and isinstance(certificado["curso_id"], ObjectId): 
            certificado["curso_id"] = str(certificado["curso_id"])

    return certificados

@router.put("/certificados/{certificado_id}", response_model=Certificado)
async def atualizar_certificado(certificado_id: str, certificado: Certificado):
    if not ObjectId.is_valid(certificado_id):
        raise HTTPException(status_code=400, detail="Id inválido")
    
    certificado_dict = certificado.dict(by_alias=True, exclude={"id"})
     
    resultado = await db.certificados.update_one({"_id": ObjectId(certificado_id)}, {"$set" : certificado_dict})
    
    if resultado.matched_count == 0:
        raise HTTPException (status_code=404, detail="Certificado não encontrado")
    
    certificado_atualizado = await db.certificados.find_one({"_id": ObjectId(certificado_id)})
    certificado_atualizado["_id"] = str(certificado_atualizado["_id"])
    
    return certificado_atualizado

@router.delete("/certificados/{certificado_id}", status_code=200)
async def excluir_certificado(certificado_id: str):
    if not ObjectId.is_valid(certificado_id):
        raise HTTPException(status_code=400, detail="ID de certificado inválido")
    
    certificado_obj_id = ObjectId(certificado_id)
    
    certificado = await db.certificados.find_one({"_id": certificado_obj_id})
    if not certificado:
        raise HTTPException(status_code=404, detail="Certificado não encontrado")
        
    
    delete_resultado = await db.certificados.delete_one({"_id": certificado_obj_id})
    if delete_resultado.deleted_count == 0:
        raise HTTPException(status_code=500, detail="Erro ao excluir Certificado")
    
    return {"messagem": "Certificado excluido e removido do aluno com sucesso"}



