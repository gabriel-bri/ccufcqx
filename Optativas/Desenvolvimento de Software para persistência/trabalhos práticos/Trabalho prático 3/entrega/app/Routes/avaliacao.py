from fastapi import APIRouter, Query, HTTPException
from bson import ObjectId
from typing import List, Dict, Any, Optional
from Models.models import Avaliacao
from Database.database import db 

router = APIRouter()

@router.post("/avaliacao", response_model=Avaliacao)
async def criar_avaliacao(avaliacao: Avaliacao):
    avaliacao_dict = avaliacao.dict(by_alias=True, exclude={"id"})
    
    nova_avaliacao = await db.avaliacoes.insert_one(avaliacao_dict)
    
    avaliacao_criada = await db.avaliacoes.find_one({"_id": nova_avaliacao.inserted_id})
    
    if not avaliacao_criada:
        raise HTTPException(status_code=400, detail="Erro ao criar Avaliação")

    # Converte o `_id` do MongoDB para string antes de retornar
    avaliacao_criada["_id"] = str(avaliacao_criada["_id"])

    return avaliacao_criada

@router.get("/avaliacao/quantidade")
async def quantidade_avaliacoes():
    total_avaliacoes = await db.avaliacoes.count_documents({})
    return {"quantidade avaliações": total_avaliacoes}

@router.get("/avaliacao/paginados", response_model=Dict[str, Any])
async def paginacao_avaliacao(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    try:
        total = await db.avaliacoes.count_documents({})

        avaliacoes_cursor = db.avaliacoes.find().skip(offset).limit(limit)
        avaliacoes = await avaliacoes_cursor.to_list(length=limit)
        
        for avaliacao in avaliacoes:
            avaliacao["_id"] = str(avaliacao["_id"])
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)

        return {
            "data": avaliacoes,
            "pagination": {
                "total": total,
                "current_page": current_page,
                "total_pages": total_pages,
                "page_size": limit,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao realizar paginação.")


@router.get("/avaliacao/{avaliacao_id}", response_model=Avaliacao)
async def buscar_avaliacao_por_id(avaliacao_id: str) -> Dict[str, Any]:
    filtro = {"_id": ObjectId(avaliacao_id)} if ObjectId.is_valid(avaliacao_id) else {"_id": avaliacao_id}

    avaliacao = await db.avaliacoes.find_one(filtro)

    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    avaliacao["_id"] = str(avaliacao["_id"])
    
    if "alunos" in avaliacao and isinstance(avaliacao["alunos"], list):
        avaliacao["alunos"] = [str(aluno_id) if isinstance(aluno_id, ObjectId) else aluno_id for aluno_id in avaliacao["alunos"]]

    if "cursos" in avaliacao and isinstance(avaliacao["cursos"], list):
        avaliacao["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in avaliacao["cursos"]]

    return avaliacao

@router.get("/avaliacao", response_model=List[Avaliacao])
async def listar_avaliacoes():
    avaliacoes = await db.avaliacoes.find().to_list(None)
    
    for avaliacao in avaliacoes:
        avaliacao["_id"] = str(avaliacao["_id"])
        
        if "alunos" in avaliacao and isinstance(avaliacao["alunos"], list):
            avaliacao["alunos"] = [str(aluno_id) if isinstance(aluno_id, ObjectId) else aluno_id for aluno_id in avaliacao["alunos"]]

        if "cursos" in avaliacao and isinstance(avaliacao["cursos"], list):
            avaliacao["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in avaliacao["cursos"]]

    return avaliacoes

@router.put("/avaliacao/{avaliacao_id}", response_model=Avaliacao)
async def atualizar_avaliacao(avaliacao_id: str, avaliacao: Avaliacao):
    if not ObjectId.is_valid(avaliacao_id):
        raise HTTPException(status_code=400, detail="Id inválido")
    
    avaliacao_dict = avaliacao.dict(by_alias=True, exclude={"id"})
     
    resultado = await db.avaliacoes.update_one({"_id": ObjectId(avaliacao_id)}, {"$set" : avaliacao_dict})
    
    if resultado.matched_count == 0:
        raise HTTPException (status_code=404, detail="Avaliação não encontrada")
    
    avaliacao_atualizada = await db.avaliacoes.find_one({"_id": ObjectId(avaliacao_id)})
    avaliacao_atualizada["_id"] = str(avaliacao_atualizada["_id"])
    
    return avaliacao_atualizada

@router.delete("/avaliacao/{avaliacao_id}", status_code=200)
async def excluir_avaliacao(avaliacao_id: str):
    if not ObjectId.is_valid(avaliacao_id):
        raise HTTPException(status_code=400, detail="ID de avaliação inválida")
    
    avaliacao_obj_id = ObjectId(avaliacao_id)
    
    avaliacao = await db.avaliacoes.find_one({"_id": avaliacao_obj_id})
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    
    
    delete_resultado = await db.avaliacoes.delete_one({"_id": avaliacao_obj_id})
    if delete_resultado.deleted_count ==0:
        raise HTTPException(status_code=500, detail="Erro ao excluir Avaliação")
    
    return {"messagem": "Avaliação excluida com sucesso"}



