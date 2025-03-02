import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Avaliacao
from sqlalchemy import func
from app.Database.database import get_session  
from typing import Dict, Any

router = APIRouter()

@router.post("/avaliacao", response_model=Avaliacao)
def criar_avaliacao(avaliacao: Avaliacao, session: Session = Depends(get_session)):
    try:
        session.add(avaliacao)
        session.commit()
        session.refresh(avaliacao)
        logging.info(f"Avaliação inserida com sucesso: {avaliacao.id_avaliacao}")
        return avaliacao
    except Exception as e:
        logging.error(f"Erro ao inserir avaliação: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao realizar inserção da avaliação.")

@router.get("/avaliacao", response_model=list[Avaliacao])
def listar_avaliacao(session: Session = Depends(get_session)):
    try:
        avaliacao = session.exec(select(Avaliacao)).all()
        if not avaliacao:
            raise HTTPException(status_code=404, detail="Nenhuma avaliação cadastrada.")
        
        logging.info(f"Listagem de avaliações realizada com sucesso. Total de avaliações: {len(avaliacao)}")
        return avaliacao
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao listar avaliações: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar avaliações.")

@router.put("/avaliacao/{id_avaliacao}")
def atualizar_avaliacao(id_avaliacao: int, avaliacao_atualizado: Avaliacao, session: Session = Depends(get_session)):
    try:
        avaliacao = session.get(Avaliacao, id_avaliacao)
        if avaliacao is None:
            logging.warning(f"Tentativa de atualizar avaliação inexistente: {id_avaliacao}")
            raise HTTPException(status_code=404, detail="Avaliação não encontrada")
        
        update_data = avaliacao_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(avaliacao, key, value)
        
        session.add(avaliacao)
        session.commit()
        session.refresh(avaliacao)
        logging.info(f"Avaliação atualizada com sucesso: {id_avaliacao}")
        return avaliacao
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar avaliação: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar avaliação.")

@router.delete("/avaliacao/{id_avaliacao}")
def excluir_avaliacao(id_avaliacao: int, session: Session = Depends(get_session)):
    try:
        avaliacao = session.get(Avaliacao, id_avaliacao)
        if avaliacao is None:
            logging.warning(f"Tentativa de excluir avaliação inexistente: {id_avaliacao}")
            raise HTTPException(status_code=404, detail="Avaliação não encontrada")
        
        session.delete(avaliacao)
        session.commit()
        logging.info(f"Avaliação excluída com sucesso: {id_avaliacao}")
        return {"message": "Avaliação excluída com sucesso"}
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir avaliação: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir avaliação.")

@router.get("/avaliacao/quantidade")
def quantidade_avaliacao(session: Session = Depends(get_session)):
    try:
        total_avaliacao = session.exec(select(Avaliacao)).all()
        quantidade = len(total_avaliacao)
        logging.info(f"Quantidade de avaliações obtida: {quantidade}")
        return {"quantidade avaliacao": quantidade}
    except Exception as e:
        logging.error(f"Erro ao contar as avaliações: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao contar as avaliações.")

@router.get("/avaliacao/paginados", response_model=Dict[str, Any])
def paginacao_avaliacao(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        total = session.execute(select(func.count(Avaliacao.id_avaliacao))).scalar_one_or_none() or 0
        
        result = session.execute(select(Avaliacao).offset(offset).limit(limit))
        avaliacoes = result.scalars().all()
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)
        
        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": avaliacoes,
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
