import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Aula
from sqlalchemy import func
from app.Database.database import get_session  
from typing import Dict, Any

router = APIRouter()

@router.post("/aulas", response_model=Aula)
def criar_aula(aula: Aula, session: Session = Depends(get_session)):
    try:
        session.add(aula)
        session.commit()
        session.refresh(aula)
        logging.info(f"Aula inserida com sucesso: {aula.id_aula}")
        return aula
    except Exception as e:
        logging.error(f"Erro ao inserir aula: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao realizar inserção da aula.")

@router.get("/aulas", response_model=list[Aula])
def listar_aulas(session: Session = Depends(get_session)):
    try:
        aulas = session.exec(select(Aula)).all()
        if not aulas:
            raise HTTPException(status_code=404, detail="Nenhuma aula cadastrada.")
        
        logging.info(f"Listagem de aulas realizada com sucesso. Total de aulas: {len(aulas)}")
        return aulas
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao listar aulas: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar aulas.")

@router.put("/aulas/{id_aula}")
def atualizar_aula(id_aula: int, aula_atualizado: Aula, session: Session = Depends(get_session)):
    try:
        aula = session.get(Aula, id_aula)
        if aula is None:
            raise HTTPException(status_code=404, detail="Aula não encontrada")
        
        update_data = aula_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(aula, key, value)
        
        session.add(aula)
        session.commit()
        session.refresh(aula)
        logging.info(f"Aula atualizada com sucesso: {id_aula}")
        return aula
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar aula: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar aula.")

@router.delete("/aulas/{id_aula}")
def excluir_aula(id_aula: int, session: Session = Depends(get_session)):
    try:
        aula = session.get(Aula, id_aula)
        if aula is None:
            raise HTTPException(status_code=404, detail="Aula não encontrada")
        
        session.delete(aula)
        session.commit()
        logging.info(f"Aula excluída com sucesso: {id_aula}")
        return {"message": "Aula excluída com sucesso"}
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir aula: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir aula.")

@router.get("/aulas/quantidade")
def quantidade_aulas(session: Session = Depends(get_session)):
    try:
        total_aulas = session.exec(select(Aula)).all()
        quantidade = len(total_aulas)
        logging.info(f"Quantidade de aulas obtida: {quantidade}")
        return {"quantidade aulas": quantidade}
    
    except Exception as e:
        logging.error(f"Erro ao contar as aulas: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao contar as aulas.")

@router.get("/aulas/paginados", response_model=Dict[str, Any])
def paginacao_aulas(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        total = session.execute(select(func.count(Aula.id_aula))).scalar_one_or_none() or 0
        
        result = session.execute(select(Aula).offset(offset).limit(limit))
        aulas = result.scalars().all()
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)

        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": aulas,
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
