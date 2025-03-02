import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Categoria
from sqlalchemy import func
from app.Database.database import get_session  
from typing import Dict, Any

router = APIRouter()

@router.post("/categoria", response_model=Categoria)
def criar_categoria(categoria: Categoria, session: Session = Depends(get_session)):
    try:
        session.add(categoria)
        session.commit()
        session.refresh(categoria)
        logging.info(f"Categoria inserida com sucesso: {categoria.id_categoria}")
        return categoria
    except Exception as e:
        logging.error(f"Erro ao inserir categoria: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao realizar inserção da categoria.")

@router.get("/categoria", response_model=list[Categoria])
def listar_categoria(session: Session = Depends(get_session)):
    try:
        categoria = session.exec(select(Categoria)).all()
        if not categoria:
            raise HTTPException(status_code=404, detail="Nenhuma categoria cadastrada.")
        
        logging.info(f"Listagem de categorias realizada com sucesso. Total de categorias: {len(categoria)}")
        return categoria
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao listar categorias: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar categorias.")

@router.put("/categoria/{id_categoria}")
def atualizar_categoria(id_categoria: int, categoria_atualizado: Categoria, session: Session = Depends(get_session)):
    try:
        categoria = session.get(Categoria, id_categoria)
        if categoria is None:
            raise HTTPException(status_code=404, detail="Categoria não encontrada")
        
        update_data = categoria_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(categoria, key, value)
        
        session.add(categoria)
        session.commit()
        session.refresh(categoria)
        logging.info(f"Categoria atualizada com sucesso: {id_categoria}")
        return categoria
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar categoria: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar categoria.")

@router.delete("/categoria/{id_categoria}")
def excluir_categoria(id_categoria: int, session: Session = Depends(get_session)):
    try:
        categoria = session.get(Categoria, id_categoria)
        if categoria is None:
            raise HTTPException(status_code=404, detail="Categoria não encontrada")
        
        session.delete(categoria)
        session.commit()
        logging.info(f"Categoria excluída com sucesso: {id_categoria}")
        return {"message": "Categoria excluída com sucesso"}
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir categoria: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir categoria.")

@router.get("/categoria/quantidade")
def quantidade_categoria(session: Session = Depends(get_session)):
    try:
        total_categoria = session.exec(select(Categoria)).all()
        quantidade = len(total_categoria)
        logging.info(f"Quantidade de categorias obtida: {quantidade}")
        return {"quantidade categorias": quantidade}
    
    except Exception as e:
        logging.error(f"Erro ao contar as categorias: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao contar as categorias: {str(e)}")

@router.get("/categoria/paginados", response_model=Dict[str, Any])
def paginacao_categoria(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        total = session.execute(select(func.count(Categoria.id_categoria))).scalar_one_or_none() or 0
        
        result = session.execute(select(Categoria).offset(offset).limit(limit))
        categorias = result.scalars().all()  

        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)
        
        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": categorias,
            "pagination": {
                "total": total,
                "current_page": current_page,
                "total_pages": total_pages,
                "page_size": limit
            }
        }
    
    except Exception as e:
        logging.error(f"Erro ao realizar paginação: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao realizar paginação.")
