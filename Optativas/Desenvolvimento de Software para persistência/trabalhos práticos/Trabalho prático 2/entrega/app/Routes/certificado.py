import logging
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select, Session
from app.Models.models import Certificado
from sqlalchemy import func
from app.Database.database import get_session  
from typing import Dict, Any

router = APIRouter()

@router.post("/certificados", response_model=Certificado)
def criar_certificado(certificado: Certificado, session: Session = Depends(get_session)):
    try:
        session.add(certificado)
        session.commit()
        session.refresh(certificado)
        logging.info(f"Certificado inserido com sucesso: {certificado.id_certificado}")
        return certificado
    except Exception as e:
        logging.error(f"Erro ao inserir certificado: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao realizar inserção do certificado.")

@router.get("/certificados", response_model=list[Certificado])
def listar_certificados(session: Session = Depends(get_session)):
    try:
        certificados = session.exec(select(Certificado)).all()
        if not certificados:
            raise HTTPException(status_code=404, detail="Nenhum certificado cadastrado.")
        
        logging.info(f"Listagem de certificados realizada com sucesso. Total de certificados: {len(certificados)}")
        return certificados
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao listar certificados: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao listar certificados.")

@router.put("/certificados/{id_certificado}")
def atualizar_certificado(id_certificado: int, certificado_atualizado: Certificado, session: Session = Depends(get_session)):
    try:
        certificado = session.get(Certificado, id_certificado)
        if certificado is None:
            raise HTTPException(status_code=404, detail="Certificado não encontrado")
        
        update_data = certificado_atualizado.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(certificado, key, value)
        
        session.add(certificado)
        session.commit()
        session.refresh(certificado)
        logging.info(f"Certificado atualizado com sucesso: {id_certificado}")
        return certificado
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao atualizar certificado: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar certificado.")

@router.delete("/certificados/{id_certificado}")
def excluir_certificado(id_certificado: int, session: Session = Depends(get_session)):
    try:
        certificado = session.get(Certificado, id_certificado)
        if certificado is None:
            raise HTTPException(status_code=404, detail="Certificado não encontrado")
        
        session.delete(certificado)
        session.commit()
        logging.info(f"Certificado excluído com sucesso: {id_certificado}")
        return {"message": "Certificado excluído com sucesso"}
    
    except HTTPException as http_exc:
        # Captura a HTTPException e relança
        logging.error(f"Erro: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logging.error(f"Erro ao excluir certificado: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao excluir certificado.")

@router.get("/certificados/quantidade")
def quantidade_certificados(session: Session = Depends(get_session)):
    try:
        total_certificados = session.exec(select(Certificado)).all()
        quantidade = len(total_certificados)
        logging.info(f"Quantidade de certificados obtida: {quantidade}")
        return {"quantidade certificados": quantidade}
    
    except Exception as e:
        logging.error(f"Erro ao contar os certificados: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao contar os certificados: {str(e)}")

@router.get("/certificados/paginados", response_model=Dict[str, Any])
def paginacao_certificados(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    session: Session = Depends(get_session)
):
    try:
        total = session.execute(select(func.count(Certificado.id_certificado))).scalar_one_or_none() or 0
        
        result = session.execute(select(Certificado).offset(offset).limit(limit))
        certificados = result.scalars().all()  

        current_page = (offset // limit) + 1
        total_pages = (total // limit) + (1 if total % limit > 0 else 0)
        
        logging.info(f"Paginação realizada: Página {current_page}/{total_pages}, Total de registros: {total}")
        
        return {
            "data": certificados,
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
