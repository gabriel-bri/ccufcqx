from fastapi import APIRouter, HTTPException
from bson import ObjectId
from Database.database import db
from Models.models import Aluno, Curso, Modulo
from typing import Dict, Any

router = APIRouter()

@router.post("/matriculas/")
async def matricular_aluno(curso_id: str, aluno_id: str):
    if not ObjectId.is_valid(curso_id) or not ObjectId.is_valid(aluno_id):
        raise HTTPException(status_code=400, detail="ID de curso ou aluno inválido")

    curso = await db.cursos.find_one({"_id": ObjectId(curso_id)})
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    aluno = await db.alunos.find_one({"_id": ObjectId(aluno_id)})
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    await db.cursos.update_one(
        {"_id": ObjectId(curso_id)},
        {"$addToSet": {"alunos": ObjectId(aluno_id)}}
    )

    await db.alunos.update_one(
        {"_id": ObjectId(aluno_id)},
        {"$addToSet": {"cursos": ObjectId(curso_id)}}
    )

    return {"message": "Aluno matriculado com sucesso!"}

@router.get("/cursos/{curso_id}/alunos")
async def alunos_por_curso(curso_id: str) -> Dict[str, Any]:
    if not ObjectId.is_valid(curso_id):
        raise HTTPException(status_code=400, detail="ID de curso inválido")

    curso = await db.cursos.find_one({"_id": ObjectId(curso_id)})
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    if "alunos" in curso and isinstance(curso["alunos"], list):
        curso["alunos"] = [ObjectId(aluno_id) if isinstance(aluno_id, str) else aluno_id for aluno_id in curso["alunos"]]

    pipeline = [
        {"$match": {"_id": ObjectId(curso_id)}},
        
        {
            "$lookup": {
                "from": "alunos",  
                "localField": "alunos",  
                "foreignField": "_id",  
                "as": "alunos_info"  
            }
        },
        
        {
            "$lookup": {
                "from": "instrutores",  
                "localField": "instrutor_id", 
                "foreignField": "_id",  
                "as": "instrutor_info"
        }
      },
        
        {
            "$project": {
                "_id": {"$toString": "$_id"},
                "nome_curso": 1, 
                "descricao": 1, 
                "horas_totais": 1,
         
                "instrutor": { "$ifNull": [{ "$arrayElemAt": ["$instrutor_info", 0] }, {}] },
                "alunos": {
                    "$map": {
                        "input": "$alunos_info",
                        "as": "aluno",
                        "in": {
                            "_id": { "$toString": "$$aluno._id" },
                            "nome_completo": "$$aluno.nome_completo",
                            "contato_email": "$$aluno.contato_email"
                    }
                }
            }
         }
        }
    ]

    resultado = await db.cursos.aggregate(pipeline).to_list(1)

    if not resultado:
        raise HTTPException(status_code=404, detail="Nenhum aluno encontrado para este curso")

    curso_detalhado = resultado[0]

    curso_detalhado["_id"] = str(curso_detalhado["_id"])

    if "alunos" in curso_detalhado and isinstance(curso_detalhado["alunos"], list):
        for aluno in curso_detalhado["alunos"]:
            if "_id" in aluno and isinstance(aluno["_id"], ObjectId):
                aluno["_id"] = str(aluno["_id"])
            if "cursos" in aluno and isinstance(aluno["cursos"], list):
                aluno["cursos"] = [str(curso) if isinstance(curso, ObjectId) else curso for curso in aluno["cursos"]]

    return curso_detalhado


@router.get("/modulos/detalhes")
async def modulos_com_cursos_e_total_aulas():
    pipeline = [
        {
            "$lookup": {
                "from": "cursos", 
                "localField": "_id",
                "foreignField": "modulos",  
                "as": "cursos_info"
            }
        },
        {
            "$lookup": {
                "from": "aulas",  
                "localField": "_id",
                "foreignField": "modulo_id",  
                "as": "aulas_info"
            }
        },
        {
            "$addFields": {
                "total_aulas": {"$size": "$aulas_info"}  
            }
        },
        {
            "$project": {
                "_id": 1,
                "nome_modulo": 1,
                "descricao": 1,
                "curso": "$cursos_info.nome_curso",  
                "total_aulas": 1 
            }
        }
    ]
    
    resultado = await db.modulos.aggregate(pipeline).to_list(100)
    
    for modulo in resultado:
        modulo["_id"] = str(modulo["_id"])
        if "cursos_info" in modulo and isinstance(modulo["cursos_info"], list):
            modulo["cursos_info"] = [str(curso_id) for curso_id in modulo["cursos_info"]]
    
    return resultado