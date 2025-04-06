# candidato 1:n candidaturas 1:n eleicao
# partir do sq_candidato
# fazer uma busca no motivo_cassacao com sq_candidato egual a sq_candidato
# recuperar esse titulo e salvar no dado

from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel

# consulta_cand_2024.csv
class CandidaturaBase(BaseModel):
    # Candidatura   
    sq_candidato: int # ID - id candidatura
    nm_candidato : str # nome do candidato
    cd_eleicao: int # id eleicao. from eleicao como chave estrangeira
    sg_uf: str
    ds_cargo: str # Descricao CARGO
    nr_candidato: int # numero pra votar
    nr_partido: int # numero
    sg_partido: str # sigla
    nm_partido: str # nome do partido
    nr_turno: int # INDICA SE FOI OU NAO PARA SEGUNDO TURNO - QUANTOS ELEITOS FORAM PARA SEGUNDO TURNO
    tp_agremiacao: str
    ds_sit_tot_turno: str # NÃO ELEITO | ELEITO
    ds_tp_motivo: str = ""  # from motivo_cassacao. descreve o tipo de motivo ...
    ds_motivo: str = "" # from motivo_cassacao.


class CandidaturaCreateMixin(BaseModel):
    pass  # Adicione campos específicos para criação, se necessário

class CandidaturaPublicMixin(BaseModel):
    id: str

class CandidaturaCreate(CandidaturaBase, CandidaturaCreateMixin):
    pass

class CandidaturaPublic(CandidaturaBase, CandidaturaPublicMixin):
    pass

class CandidaturaUpdate(BaseModel): 
    sq_candidato:  Optional[int] = None
    nm_candidato:  Optional[str] = None
    cd_eleicao:  Optional[int] = None
    sg_uf:  Optional[str] = None
    ds_cargo:  Optional[str] = None
    nr_candidato:  Optional[int] = None
    nr_partido:  Optional[int] = None
    sg_partido:  Optional[str] = None
    nm_partido:  Optional[str] = None
    nr_turno:  Optional[int] = None
    tp_agremiacao: Optional[str] = None
    ds_sit_tot_turno:  Optional[str] = None
    ds_tp_motivo:  Optional[str] = ""
    ds_motivo:  Optional[str] = ""
