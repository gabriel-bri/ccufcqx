from pydantic import BaseModel
from datetime import datetime

# consulta_cand_2024.csv + consulta_vagas_2024.csv
class EleicaoBase(BaseModel):
    #Eleicao
    # Pegar somente 1 de cada código
    ds_eleicao: str # descricao eleicao
    dt_eleicao: datetime # data eleicao
    ano_eleicao: int
    cd_tipo_eleicao: int
    nm_tipo_eleicao: str
    tp_abrangencia: str # tipo abrangencia eleicao
    nr_turno: int

class EleicaoPublicMixin(BaseModel):
    id: str # ID - primary-key
    cd_eleicao: int # id eleicao, único por eleição e por turno
        
class EleicaoCreateMixin(BaseModel):
    cd_eleicao: int # id eleicao, único por eleição e por turno

class EleicaoPublic(EleicaoBase, EleicaoPublicMixin):
    pass

class EleicaoCreate(EleicaoBase, EleicaoCreateMixin):
    pass

class EleicaoUpdate(BaseModel):
    ds_eleicao: str | None = None # descricao eleicao
    dt_eleicao: datetime | None = None # data eleicao
    ano_eleicao: int | None = None
    cd_tipo_eleicao: int | None = None
    nm_tipo_eleicao: str | None = None
    tp_abrangencia: str | None = None # tipo abrangencia eleicao
    nr_turno: int | None = None
    qt_vaga: int | None = None # from vagas - NAO TEM no Candidato, tá em vagas