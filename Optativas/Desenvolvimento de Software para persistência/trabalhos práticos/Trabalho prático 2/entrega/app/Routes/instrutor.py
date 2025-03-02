import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Instrutor, Curso
from sqlalchemy import func
from app.Database.database import get_session  
from typing import Dict, Any, Optional, List

router = APIRouter()

@router.post("/instrutores", response_model=Instrutor)
def criar_instrutor(instrutor: Instrutor, session: Session = Depends(get_session)):
    try:
        session.add(instrutor)
        session.commit()
        session.refresh(instrutor)
        logging.info(f"Instrutor criado com sucesso: {instrutor.id_instrutor}")
        return instrutor
    except Exception as e:
        logging.error(f"Erro ao criar instrutor: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao criar instrutor.")

@router.get("/instrutores", response_model=list[Instrutor])
def listar_instrutores(session: Session = Depends(get_session)):
    try:
        instrutores = session.exec(select(Instrutor)).all()
        if not instrutores:
            raise HTTPException(status_code=404, detail="Nenhum instrutor cadastrado.")
        
        logging.info(f"Listagem de instrutores realizada com sucesso. Total de instrutores: {len(instrutores)}")
        return instrutores
    
    except HTTPException as http_exc:
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao listar instrutores: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar instrutores.")

@router.put("/instrutores/{id_instrutor}")
def atualizar_instrutor(id_instrutor: int, instrutor_atualizado: Instrutor, session: Session = Depends(get_session)):
    try:
        instrutor = session.get(Instrutor, id_instrutor)
        if instrutor is None:
            raise HTTPException(status_code=404, detail="Instrutor não encontrado")
        
        update_data = instrutor_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(instrutor, key, value)
        
        session.add(instrutor)
        session.commit()
        session.refresh(instrutor)
        logging.info(f"Instrutor atualizado com sucesso: {id_instrutor}")
        return instrutor
    
    except HTTPException as http_exc:
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar instrutor: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar instrutor.")

@router.delete("/instrutores/{id_instrutor}")
def excluir_instrutor(id_instrutor: int, session: Session = Depends(get_session)):
    try:
        instrutor = session.get(Instrutor, id_instrutor)
        if instrutor is None:
            raise HTTPException(status_code=404, detail="Instrutor não encontrado")
        
        session.delete(instrutor)
        session.commit()
        logging.info(f"Instrutor excluído com sucesso: {id_instrutor}")
        return {"message": "Instrutor excluído com sucesso"}
    
    except HTTPException as http_exc:
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir instrutor: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir instrutor.")

@router.get("/instrutores/quantidade")
def quantidade_instrutores(session: Session = Depends(get_session)):
    try:
        total_instrutores = session.exec(select(Instrutor)).all()
        quantidade = len(total_instrutores)
        logging.info(f"Quantidade de instrutores obtida: {quantidade}")
        return {"quantidade instrutores": quantidade}
    
    except Exception as e:
        logging.error(f"Erro ao contar os instrutores: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao contar os instrutores: {str(e)}")

@router.get("/instrutores/paginados", response_model=Dict[str, Any])
def paginacao_instrutores(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        total = session.execute(select(func.count(Instrutor.id_instrutor))).scalar_one_or_none() or 0
        
        result = session.execute(select(Instrutor).offset(offset).limit(limit))
        instrutores = result.scalars().all()

        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)
        
        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": instrutores,
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

@router.get("/instrutores/filtrar", response_model=List[Instrutor])
def filtrar_instrutores(
    nome: Optional[str] = Query(None, min_length=3),
    especialidade: Optional[str] = None,
    curso_id: Optional[int] = None,
    session: Session = Depends(get_session)
):
    try:
        query = select(Instrutor)
        
        if nome:
            query = query.filter(Instrutor.nome_completo.ilike(f"%{nome}%"))
            logging.info(f"Filtrando instrutores por nome: {nome}")
        
        if especialidade:
            query = query.filter(Instrutor.especialidade.ilike(f"%{especialidade}%"))
            logging.info(f"Filtrando instrutores por especialidade: {especialidade}")
        
        if curso_id:
            query = query.join(Curso).filter(Curso.id_curso == curso_id)
            logging.info(f"Filtrando instrutores pelo curso ID: {curso_id}")
        
        instrutores = session.exec(query).all()
        logging.info(f"Total de instrutores encontrados: {len(instrutores)}")
        return instrutores
    except Exception as e:
        logging.error(f"Erro inesperado ao filtrar instrutores: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao filtrar instrutores")
