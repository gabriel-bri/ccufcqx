# candidato n:n eleicao
# candidato 1:n canditura n:1 elicao
# candidato 1:1 InfoCandidato

from pydantic import BaseModel
from datetime import datetime

class CandidatoBase(BaseModel):
    sq_candidato: int # chave estrangeira de candidatura
    nm_candidato: str # nome do candidato
    dt_nascimento: datetime # 16/02/1981
    ds_genero: str # MASCULINO
    ds_grau_instrucao: str # ENSINO MÉDIO COMPLETO
    ds_cor_raca: str # BRANCA
    ds_ocupacao: str # SERVIDOR PÚBLICO MUNICIPAL

class CandidatoTituloMixin(BaseModel):
    nr_titulo_eleitoral_candidato: int # ID - primary-key

class CandidatoPublic(CandidatoBase, CandidatoTituloMixin):
    pass

class CandidatoCreate(CandidatoBase, CandidatoTituloMixin):
    pass

class CandidatoUpdate(BaseModel):
    sq_candidato: int | None = None 
    nm_candidato: str | None = None
    dt_nascimento: datetime | None = None
    ds_genero: str | None = None
    ds_grau_instrucao: str | None = None
    ds_cor_raca: str | None = None
    ds_ocupacao: str | None = None