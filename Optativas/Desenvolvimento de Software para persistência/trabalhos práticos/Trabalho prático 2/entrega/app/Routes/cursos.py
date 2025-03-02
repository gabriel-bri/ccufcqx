import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Curso
from sqlalchemy import func
from app.Database.database import get_session  
from typing import Dict, Any
from typing import List, Optional
from datetime import datetime

router = APIRouter()

@router.post("/cursos", response_model=Curso)
def criar_curso(curso: Curso, session: Session = Depends(get_session)):
    try:
        session.add(curso)
        session.commit()
        session.refresh(curso)
        logging.info(f"Curso inserido com sucesso: {curso.id_curso}")
        return curso
    except Exception as e:
        logging.error(f"Erro ao inserir curso: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao realizar inserção do curso.")

@router.get("/cursos", response_model=list[Curso])
def listar_cursos(session: Session = Depends(get_session)):
    # try:
        cursos = session.exec(select(Curso)).all()
        if not cursos:
            raise HTTPException(status_code=404, detail="Nenhum curso cadastrado.")
        
        logging.info(f"Listagem de cursos realizada com sucesso. Total de cursos: {len(cursos)}")
        return cursos
    
    # except HTTPException as http_exc:
    #     # Captura a HTTPException e relança
    #     logging.error(f"Erro: {http_exc.detail}")
    #     raise http_exc
    # except Exception as e:
    #     logging.error(f"Erro ao listar cursos: {str(e)}")
    #     raise HTTPException(status_code=500, detail="Erro ao listar cursos.")

@router.put("/cursos/{id_curso}")
def atualizar_curso(id_curso: int, curso_atualizado: Curso, session: Session = Depends(get_session)):
    try:
        curso = session.get(Curso, id_curso)
        if curso is None:
            raise HTTPException(status_code=404, detail="Curso não encontrado")
        
        update_data = curso_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(curso, key, value)
        
        session.add(curso)
        session.commit()
        session.refresh(curso)
        logging.info(f"Curso atualizado com sucesso: {id_curso}")
        return curso
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar curso: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar curso.")

@router.delete("/cursos/{id_curso}")
def excluir_curso(id_curso: int, session: Session = Depends(get_session)):
    try:
        curso = session.get(Curso, id_curso)
        if curso is None:
            raise HTTPException(status_code=404, detail="Curso não encontrado")
        
        session.delete(curso)
        session.commit()
        logging.info(f"Curso excluído com sucesso: {id_curso}")
        return {"message": "Curso excluído com sucesso"}
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir curso: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir curso.")

@router.get("/cursos/quantidade")
def quantidade_cursos(session: Session = Depends(get_session)):
    try:
        total_cursos = session.exec(select(Curso)).all()
        quantidade = len(total_cursos)
        logging.info(f"Quantidade de cursos obtida: {quantidade}")
        return {"quantidade cursos": quantidade}
    
    except Exception as e:
        logging.error(f"Erro ao contar os cursos: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao contar os cursos: {str(e)}")

@router.get("/cursos/paginados", response_model=Dict[str, Any])
def paginacao_cursos(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        total = session.execute(select(func.count(Curso.id_curso))).scalar_one_or_none() or 0
        
        result = session.execute(select(Curso).offset(offset).limit(limit))
        cursos = result.scalars().all()

        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)
        
        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": cursos,
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

@router.get("/cursos/filtrar", response_model=List[Curso])
def filtrar_cursos(
    nome: Optional[str] = Query(None, min_length=3),  # Filtro por nome com mínimo de 3 caracteres
    categoria_id: Optional[int] = None,
    instrutor_id: Optional[int] = None,
    data_inicio: Optional[datetime] = None,
    data_fim: Optional[datetime] = None,
    session: Session = Depends(get_session)
):
    try:
        query = select(Curso)
        
        if nome:
            query = query.filter(Curso.nome_curso.ilike(f"%{nome}%"))
            logging.info(f"Filtrando cursos por nome: {nome}")
        
        if categoria_id:
            query = query.filter(Curso.categoria_id == categoria_id)
            logging.info(f"Filtrando cursos pela categoria ID: {categoria_id}")
        
        if instrutor_id:
            query = query.filter(Curso.instrutor_id == instrutor_id)
            logging.info(f"Filtrando cursos pelo instrutor ID: {instrutor_id}")
        
        if data_inicio:
            query = query.filter(Curso.data_criacao >= data_inicio)
            logging.info(f"Filtrando cursos com data de criação após: {data_inicio}")
        
        if data_fim:
            query = query.filter(Curso.data_criacao <= data_fim)
            logging.info(f"Filtrando cursos com data de criação antes: {data_fim}")
        
        cursos = session.exec(query).all()
        logging.info(f"Total de cursos encontrados: {len(cursos)}")
        return cursos
    except Exception as e:
        logging.error(f"Erro inesperado ao filtrar cursos: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro inesperado ao filtrar cursos")
