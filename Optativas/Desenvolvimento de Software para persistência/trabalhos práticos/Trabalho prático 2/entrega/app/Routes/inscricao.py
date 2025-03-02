import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Inscricao
from sqlalchemy import func
from app.Database.database import get_session  
from typing import Dict, Any
from typing import List, Optional
from datetime import datetime

router = APIRouter()

@router.post("/inscricoes", response_model=Inscricao)
def criar_inscricao(inscricao: Inscricao, session: Session = Depends(get_session)):
    try:
        session.add(inscricao)
        session.commit()
        session.refresh(inscricao)
        logging.info(f"Inscrição criada com sucesso: {inscricao.id_inscricao}")
        return inscricao
    except Exception as e:
        logging.error(f"Erro ao criar inscrição: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao realizar a inscrição.")

@router.get("/inscricoes", response_model=list[Inscricao])
def listar_inscricoes(session: Session = Depends(get_session)):
    try:
        inscricoes = session.exec(select(Inscricao)).all()
        if not inscricoes:
            raise HTTPException(status_code=404, detail="Nenhuma inscrição cadastrada.")
        
        logging.info(f"Listagem de inscrições realizada com sucesso. Total de inscrições: {len(inscricoes)}")
        return inscricoes
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao listar inscrições: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar as inscrições.")

@router.put("/inscricoes/{id_inscricao}")
def atualizar_inscricao(id_inscricao: int, inscricao_atualizado: Inscricao, session: Session = Depends(get_session)):
    try:
        inscricao = session.get(Inscricao, id_inscricao)
        if inscricao is None:
            raise HTTPException(status_code=404, detail="Inscrição não encontrada")
        
        update_data = inscricao_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(inscricao, key, value)
        
        session.add(inscricao)
        session.commit()
        session.refresh(inscricao)
        logging.info(f"Inscrição atualizada com sucesso: {id_inscricao}")
        return inscricao
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar inscrição: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar inscrição.")

@router.delete("/inscricoes/{id_inscricao}")
def excluir_inscricao(id_inscricao: int, session: Session = Depends(get_session)):
    try:
        inscricao = session.get(Inscricao, id_inscricao)
        if inscricao is None:
            raise HTTPException(status_code=404, detail="Inscrição não encontrada")
        
        session.delete(inscricao)
        session.commit()
        logging.info(f"Inscrição excluída com sucesso: {id_inscricao}")
        return {"message": "Inscrição excluída com sucesso"}
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir inscrição: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir inscrição.")

@router.get("/inscricoes/quantidade")
def quantidade_inscricoes(session: Session = Depends(get_session)):
    try:
        total_inscricoes = session.exec(select(Inscricao)).all()
        quantidade = len(total_inscricoes)
        logging.info(f"Quantidade de inscrições obtida: {quantidade}")
        return {"quantidade inscricoes": quantidade}
    
    except Exception as e:
        logging.error(f"Erro ao contar as inscrições: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao contar as inscrições: {str(e)}")

@router.get("/inscricoes/paginados", response_model=Dict[str, Any])
def paginacao_inscricoes(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        total = session.execute(select(func.count(Inscricao.id_inscricao))).scalar_one_or_none() or 0
        
        result = session.execute(select(Inscricao).offset(offset).limit(limit))
        inscricoes = result.scalars().all()

        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)
        
        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": inscricoes,
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

@router.get("/inscricoes/filtrar", response_model=List[Inscricao])
def filtrar_inscricoes(
    aluno_id: Optional[int] = None,
    curso_id: Optional[int] = None,
    status: Optional[str] = None,
    progresso_min: Optional[float] = 0.0,
    progresso_max: Optional[float] = 100.0,
    data_inicio: Optional[datetime] = None,
    data_fim: Optional[datetime] = None,
    session: Session = Depends(get_session)
):
    try:
        query = select(Inscricao)
        
        if aluno_id:
            query = query.filter(Inscricao.aluno_id == aluno_id)
            logging.info(f"Filtrando inscrições por aluno ID: {aluno_id}")
        
        if curso_id:
            query = query.filter(Inscricao.curso_id == curso_id)
            logging.info(f"Filtrando inscrições pelo curso ID: {curso_id}")
        
        if status:
            query = query.filter(Inscricao.status == status)
            logging.info(f"Filtrando inscrições com status: {status}")
        
        query = query.filter(Inscricao.progresso >= progresso_min, Inscricao.progresso <= progresso_max)
        logging.info(f"Filtrando inscrições com progresso entre: {progresso_min}% e {progresso_max}%")
        
        if data_inicio:
            query = query.filter(Inscricao.data_inscricao >= data_inicio)
            logging.info(f"Filtrando inscrições com data de inscrição após: {data_inicio}")
        
        if data_fim:
            query = query.filter(Inscricao.data_inscricao <= data_fim)
            logging.info(f"Filtrando inscrições com data de inscrição antes: {data_fim}")
        
        inscricoes = session.exec(query).all()
        logging.info(f"Total de inscrições encontradas: {len(inscricoes)}")
        return inscricoes
    except Exception as e:
        logging.error(f"Erro inesperado ao filtrar inscrições: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao filtrar inscrições")
