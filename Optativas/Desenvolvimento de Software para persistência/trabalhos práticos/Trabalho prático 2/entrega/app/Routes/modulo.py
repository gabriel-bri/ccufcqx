import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Modulo
from sqlalchemy import func
from app.Database.database import get_session  
from typing import Dict, Any

router = APIRouter()

@router.post("/modulos", response_model=Modulo)
def criar_modulo(modulo: Modulo, session: Session = Depends(get_session)):
    try:
        session.add(modulo)
        session.commit()
        session.refresh(modulo)
        logging.info(f"Módulo criado com sucesso: {modulo.id_modulo}")
        return modulo
    except Exception as e:
        logging.error(f"Erro ao criar módulo: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao criar módulo.")

@router.get("/modulos", response_model=list[Modulo])
def listar_modulos(session: Session = Depends(get_session)):
    try:
        modulos = session.exec(select(Modulo)).all()
        if not modulos:
            raise HTTPException(status_code=404, detail="Nenhum módulo encontrado.")
        
        logging.info(f"Listagem de módulos realizada com sucesso. Total de módulos: {len(modulos)}")
        return modulos
    
    except HTTPException as http_exc:
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao listar módulos: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar módulos.")

@router.put("/modulos/{id_modulo}")
def atualizar_modulo(id_modulo: int, modulo_atualizado: Modulo, session: Session = Depends(get_session)):
    try:
        modulo = session.get(Modulo, id_modulo)
        if modulo is None:
            raise HTTPException(status_code=404, detail="Módulo não encontrado")
        
        update_data = modulo_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(modulo, key, value)
        
        session.add(modulo)
        session.commit()
        session.refresh(modulo)
        logging.info(f"Módulo atualizado com sucesso: {id_modulo}")
        return modulo
    
    except HTTPException as http_exc:
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar módulo: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar módulo.")

@router.delete("/modulos/{id_modulo}")
def excluir_modulo(id_modulo: int, session: Session = Depends(get_session)):
    try:
        modulo = session.get(Modulo, id_modulo)
        if modulo is None:
            raise HTTPException(status_code=404, detail="Módulo não encontrado")
        
        session.delete(modulo)
        session.commit()
        logging.info(f"Módulo excluído com sucesso: {id_modulo}")
        return {"message": "Módulo excluído com sucesso"}
    
    except HTTPException as http_exc:
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir módulo: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir módulo.")

@router.get("/modulos/quantidade")
def quantidade_modulos(session: Session = Depends(get_session)):
    try:
        total_modulos = session.exec(select(Modulo)).all()
        quantidade = len(total_modulos)
        logging.info(f"Quantidade de módulos obtida: {quantidade}")
        return {"quantidade modulos": quantidade}
    
    except Exception as e:
        logging.error(f"Erro ao contar os módulos: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao contar os módulos: {str(e)}")

@router.get("/modulos/paginados", response_model=Dict[str, Any])
def paginacao_modulos(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        total = session.execute(select(func.count(Modulo.id_modulo))).scalar_one_or_none() or 0
        
        result = session.execute(select(Modulo).offset(offset).limit(limit))
        modulos = result.scalars().all()

        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)
        
        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": modulos,
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
