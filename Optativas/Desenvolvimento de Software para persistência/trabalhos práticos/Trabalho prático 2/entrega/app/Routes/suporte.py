import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Suporte
from sqlalchemy import func
from app.Database.database import get_session  
from typing import Dict, Any
from typing import List, Optional
from datetime import datetime

router = APIRouter()

@router.post("/suportes", response_model=Suporte)
def criar_suporte(suporte: Suporte, session: Session = Depends(get_session)):
    try:
        session.add(suporte)
        session.commit()
        session.refresh(suporte)
        logging.info(f"suporte criado com sucesso: {suporte.id_suporte}")
        return suporte
    except Exception as e:
        logging.error(f"Erro ao criar suporte: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao criar suporte.")

@router.get("/suportes", response_model=list[Suporte])
def listar_suportes(session: Session = Depends(get_session)):
    try:
        suportes = session.exec(select(Suporte)).all()
        if not suportes:
            raise HTTPException(status_code=404, detail="Nenhum suporte encontrado.")
        
        logging.info(f"Listagem de suportes realizada com sucesso. Total de suportes: {len(suportes)}")
        return suportes
    
    except HTTPException as http_exc:
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao listar suportes: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar suportes.")

@router.put("/suportes/{id_suporte}")
def atualizar_suporte(id_suporte: int, suporte_atualizado: Suporte, session: Session = Depends(get_session)):
    try:
        suporte = session.get(Suporte, id_suporte)
        if suporte is None:
            raise HTTPException(status_code=404, detail="Suporte não encontrado")
        
        update_data = suporte_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(suporte, key, value)
        
        session.add(suporte)
        session.commit()
        session.refresh(suporte)
        logging.info(f"Suporte atualizado com sucesso: {id_suporte}")
        return suporte
    
    except HTTPException as http_exc:
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar suporte: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar suporte.")

@router.delete("/suportes/{id_suporte}")
def excluir_suporte(id_suporte: int, session: Session = Depends(get_session)):
    try:
        suporte = session.get(Suporte, id_suporte)
        if suporte is None:
            raise HTTPException(status_code=404, detail="Suporte não encontrado")
        
        session.delete(suporte)
        session.commit()
        logging.info(f"Suporte excluído com sucesso: {id_suporte}")
        return {"message": "Suporte excluído com sucesso"}
    
    except HTTPException as http_exc:
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir suporte: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir suporte.")

@router.get("/suportes/quantidade")
def quantidade_suportes(session: Session = Depends(get_session)):
    try:
        total_suportes = session.exec(select(Suporte)).all()
        quantidade = len(total_suportes)
        logging.info(f"Quantidade de suportes obtida: {quantidade}")
        return {"quantidade suportes": quantidade}
    
    except Exception as e:
        logging.error(f"Erro ao contar os suportes: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao contar os suportes: {str(e)}")

@router.get("/suportes/paginados", response_model=Dict[str, Any])
def paginacao_suportes(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        total = session.execute(select(func.count(Suporte.id_suporte))).scalar_one_or_none() or 0
        
        result = session.execute(select(Suporte).offset(offset).limit(limit))
        suportes = result.scalars().all()

        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)
        
        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": suportes,
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

@router.get("/suportes/filtrar", response_model=List[Suporte])
def filtrar_suportes(
    aluno_id: Optional[int] = None,
    curso_id: Optional[int] = None,
    status: Optional[str] = None,
    data_inicio: Optional[datetime] = None,
    data_fim: Optional[datetime] = None,
    session: Session = Depends(get_session)
):
    try:
        query = select(Suporte)
        
        if aluno_id:
            query = query.filter(Suporte.aluno_id == aluno_id)
            logging.info(f"Filtrando suportes por aluno ID: {aluno_id}")
        
        if curso_id:
            query = query.filter(Suporte.curso_id == curso_id)
            logging.info(f"Filtrando suportes pelo curso ID: {curso_id}")
        
        if status:
            query = query.filter(Suporte.status == status)
            logging.info(f"Filtrando suportes com status: {status}")
        
        if data_inicio:
            query = query.filter(Suporte.data_abertura >= data_inicio)
            logging.info(f"Filtrando suportes com data de abertura após: {data_inicio}")
        
        if data_fim:
            query = query.filter(Suporte.data_abertura <= data_fim)
            logging.info(f"Filtrando suportes com data de abertura antes: {data_fim}")
        
        suportes = session.exec(query).all()
        logging.info(f"Total de suportes encontrados: {len(suportes)}")
        return suportes
    except Exception as e:
        logging.error(f"Erro inesperado ao filtrar suportes: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao filtrar suportes")
