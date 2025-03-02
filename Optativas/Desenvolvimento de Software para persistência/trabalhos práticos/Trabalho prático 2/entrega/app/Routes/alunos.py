import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Aluno, Inscricao
from sqlalchemy import func
from app.Database.database import get_session
from typing import Dict, Any
from typing import List, Optional

router = APIRouter()

@router.post("/alunos", response_model=Aluno)
def criar_aluno(aluno: Aluno, session: Session = Depends(get_session)):
    try:
        aluno_existente = session.get(Aluno, aluno.id_aluno)
        
        if aluno_existente:
            raise HTTPException(status_code=400, detail="ID já existe no banco de dados")
        
        session.add(aluno)
        session.commit()
        session.refresh(aluno)
        logging.info(f"Aluno inserido com sucesso: {aluno.id_aluno}")
        
        return aluno

    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.warning(f"Tentativa de inserção com ID duplicado: {aluno.id_aluno}")
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao inserir aluno: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro realizar inserção.")

@router.get("/alunos", response_model=list[Aluno])
def listar_alunos(session: Session = Depends(get_session)):
    try:
        alunos = session.exec(select(Aluno)).all()
        
        if not alunos:
            raise HTTPException(status_code=404, detail="Nenhum aluno cadastrado")
        
        logging.info(f"Listagem de alunos realizada com sucesso. Total de alunos: {len(alunos)}")
        return alunos
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao listar alunos: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar alunos.")

@router.put("/alunos/{id_aluno}")
def atualizar_aluno(id_aluno: int, aluno_atualizado: Aluno, session: Session = Depends(get_session)):
    try:
        aluno = session.get(Aluno, id_aluno)
        if aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        
        update_data = aluno_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(aluno, key, value)
        
        session.add(aluno)
        session.commit()
        session.refresh(aluno)
        logging.info(f"Aluno atualizado com sucesso: {id_aluno}")
        return aluno
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.warning(f"Tentativa de atualizar aluno inexistente: {id_aluno}")
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar aluno: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar aluno.")

@router.delete("/alunos/{id_aluno}")
def excluir_aluno(id_aluno: int, session: Session = Depends(get_session)):
    try:
        aluno = session.get(Aluno, id_aluno)
        if aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        
        session.delete(aluno)
        session.commit()
        logging.info(f"Aluno excluído com sucesso: {id_aluno}")
        return {"message": "Aluno excluído com sucesso"}
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.warning(f"Tentativa de excluir aluno inexistente: {id_aluno}")
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir aluno: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir aluno.")

@router.get("/alunos/quantidade")
def quantidade_alunos(session: Session = Depends(get_session)):
    try:
        total_alunos = session.exec(select(Aluno)).all()
        quantidade = len(total_alunos)
        logging.info(f"Quantidade de alunos obtida: {quantidade}")
        return {"quantidade alunos": quantidade}
    
    except Exception as e:
        logging.error(f"Erro ao contar os alunos: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao contar os alunos.")

@router.get("/alunos/paginados", response_model=Dict[str, Any])
def paginacao_alunos(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session),
):
    try:
        total = session.execute(select(func.count(Aluno.id_aluno))).scalar_one_or_none() or 0
        
        result = session.execute(select(Aluno).offset(offset).limit(limit))
        alunos = result.scalars().all()
        
        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)

        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": alunos,
            "pagination": {
                "total": total,
                "current_page": current_page,
                "total_pages": total_pages,
                "page_size": limit,
            },
        }
    except Exception as e:
        logging.error(f"Erro ao realizar paginação: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao realizar paginação.")

@router.get("/alunos/filtrar", response_model=List[Aluno])
def filtrar_alunos(
    nome: Optional[str] = Query(None, min_length=3),
    email: Optional[str] = None,
    curso_id: Optional[int] = None,
    session: Session = Depends(get_session)
):
    try:
        query = select(Aluno)
        
        if nome:
            query = query.filter(Aluno.nome_completo.ilike(f"%{nome}%"))
            logging.info(f"Filtrando alunos por nome: {nome}")
        
        if email:
            query = query.filter(Aluno.contato_email.ilike(f"%{email}%"))
            logging.info(f"Filtrando alunos por email: {email}")
        
        if curso_id:
            query = query.join(Inscricao).filter(Inscricao.curso_id == curso_id)
            logging.info(f"Filtrando alunos pelo curso ID: {curso_id}")
        
        alunos = session.exec(query).all()
        logging.info(f"Total de alunos encontrados: {len(alunos)}")
        return alunos
    except Exception as e:
        logging.error(f"Erro inesperado ao filtrar alunos: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao filtrar alunos")
