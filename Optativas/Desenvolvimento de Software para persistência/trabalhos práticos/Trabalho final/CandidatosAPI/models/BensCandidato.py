# candidato 1:n bens
# bem 1:n candidaturas

# partir do sq_candidato
# fazer uma busca no candidato com sq_candidato egual a sq_candidato
# recuperar esse titulo e salvar no dado

from datetime import  date, time
from pydantic import BaseModel
from typing import Optional

# bem_candidato.csv
class BensCandidatoBase(BaseModel):
    id: str # mongodb
    nr_titulo_eleitoral_candidato: str
    sq_candidato: str # foreign-key - Candidatura
    nr_ordem_bem_candidato: int
    ds_tipo_bem_candidato: str
    ds_bem_candidato: str
    vr_bem_candidato: float
    dt_ult_atual_bem_candidato: date
    hh_ult_atual_bem_candidato: time

class BensCandidatoCreateMixin(BaseModel):
    pass  # Adicione campos específicos para criação, se necessário

class BensCandidatoPublicMixin(BaseModel):
    id: str

class BensCandidatoCreate(BensCandidatoBase, BensCandidatoCreateMixin):
    pass

class BensCandidatoPublic(BensCandidatoBase, BensCandidatoPublicMixin):
    pass

class BensCandidatoUpdate(BaseModel): 
    nr_titulo_eleitoral_candidato: Optional[str] = None
    sq_candidato: Optional[str] = None
    nr_ordem_bem_candidato: Optional[int] = None
    ds_tipo_bem_candidato: Optional[str] = None
    ds_bem_candidato: Optional[str] = None
    vr_bem_candidato: Optional[float] = None
    dt_ult_atual_bem_candidato: Optional[date] = None
    hh_ult_atual_bem_candidato: Optional[time] = None