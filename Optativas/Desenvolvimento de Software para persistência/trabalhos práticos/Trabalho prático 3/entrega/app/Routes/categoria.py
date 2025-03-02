from fastapi import APIRouter, Query, HTTPException
from bson import ObjectId
from typing import List, Dict, Any, Optional
from Models.models import Categoria, Curso
from Database.database import db 

router = APIRouter()

@router.post("/categorias", response_model=Categoria)
async def criar_categoria(categoria: Categoria):
    categoria_dict = categoria.dict(by_alias=True, exclude={"id"})
    
    nova_categoria = await db.categorias.insert_one(categoria_dict)
    
    categoria_criada = await db.categorias.find_one({"_id": nova_categoria.inserted_id})
    
    if not categoria_criada:
        raise HTTPException(status_code=400, detail="Erro ao criar categoria")

    # Converte o `_id` do MongoDB para string antes de retornar
    categoria_criada["_id"] = str(categoria_criada["_id"])

    return categoria_criada


@router.get("/categorias/filtrar")
async def filtrar_categorias (
    nome_categoria: Optional[str] = Query(None, min_length=3),
    descricao: Optional[str] = Query(None, min_length=3)
) -> List[Dict]:
    try:
        filtros: Dict = {}
                   
        
        if nome_categoria:
            filtros["nome_categoria"] = {"$regex": nome_categoria, "$options" : "i"}
            
        
        if descricao:
            filtros["descricao"] = {"$regex": descricao, "$options" : "i"}
        
        cursor = db.categorias.find(filtros, {"_id": 0})  # Retorna um cursor assíncrono
        categorias: List[Dict] = await cursor.to_list(length=None) 
        
        return categorias
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro inesperado ao filtrar categorias")

@router.delete("/categorias/{categoria_id}", status_code=200)
async def excluir_categoria(categoria_id: str):
    if not ObjectId.is_valid(categoria_id):
        raise HTTPException(status_code=400, detail="ID de categoria inválido")
    
    categoria_obj_id = ObjectId(categoria_id)
    
    categoria = await db.categorias.find_one({"_id": categoria_obj_id})
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    
    delete_resultado = await db.categorias.delete_one({"_id": categoria_obj_id})
    if delete_resultado.deleted_count ==0:
        raise HTTPException(status_code=500, detail="Erro ao excluir Categoria")
    
    
    return {"messagem": "Categoria excluida e removida de cursos com sucesso"}

@router.get("/categorias/paginados", response_model=Dict[str, Any])
async def paginacao_categorias(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
):
    try:
        total = await db.categorias.count_documents({})

        categorias_cursor = db.categorias.find().skip(offset).limit(limit)
        categorias = await categorias_cursor.to_list(length=limit)
        
        for categoria in categorias:
            categoria["_id"] = str(categoria["_id"])
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)

        return {
            "data": categorias,
            "pagination": {
                "total": total,
                "current_page": current_page,
                "total_pages": total_pages,
                "page_size": limit,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao realizar paginação.")

@router.get("/categorias/quantidade")
async def quantidade_categorias():
    total_categorias = await db.categorias.count_documents({})
    return {"quantidade categorias": total_categorias}

@router.get("/categorias/{categoria_id}", response_model=Categoria)
async def buscar_categorias_por_id(categoria_id: str) -> Dict[str, Any]:
    filtro = {"_id": ObjectId(categoria_id)} if ObjectId.is_valid(categoria_id) else {"_id": categoria_id}

    categoria = await db.categorias.find_one(filtro)

    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    categoria["_id"] = str(categoria["_id"])

    if "cursos" in categoria and isinstance(categoria["cursos"], list):
        categoria["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in categoria["cursos"]]

    return categoria

@router.get("/categorias", response_model=List[Categoria])
async def listar_categorias():
    categorias = await db.categorias.find().to_list(None)
    
    for categoria in categorias:
        categoria["_id"] = str(categoria["_id"])
        
        # Converte os IDs dos cursos para string, se existirem
        if "cursos" in categoria and isinstance(categoria["cursos"], list):
            categoria["cursos"] = [str(curso_id) if isinstance(curso_id, ObjectId) else curso_id for curso_id in categoria["cursos"]]

    return categorias

@router.put("/categorias/{categoria_id}", response_model=Categoria)
async def atualizar_categoria(categoria_id: str, categoria: Categoria):
    if not ObjectId.is_valid(categoria_id):
        raise HTTPException(status_code=400, detail="Id inválido")
    
    categoria_dict = categoria.dict(by_alias=True, exclude={"id"})
     
    resultado = await db.categorias.update_one({"_id": ObjectId(categoria_id)}, {"$set" : categoria_dict})
    
    if resultado.matched_count == 0:
        raise HTTPException (status_code=404, detail="Categoria não encontrada")
    
    categoria_atualizada = await db.categorias.find_one({"_id": ObjectId(categoria_id)})
    categoria_atualizada["_id"] = str(categoria_atualizada["_id"])
    
    return categoria_atualizada






    
    
