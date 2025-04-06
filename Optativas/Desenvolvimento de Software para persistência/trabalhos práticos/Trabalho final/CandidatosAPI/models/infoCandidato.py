# partir do sq_candidato
# fazer uma busca no candidato com sq_candidato egual a sq_candidato
# recuperar esse titulo e salvar no dado

from pydantic import BaseModel

class InfoCandidatoCreateMixin(BaseModel):
    nr_titulo_eleitoral_candidato: int # chave estrangeira do Candidato

class InfoCandidatoPublicMixin(BaseModel):
    nr_titulo_eleitoral_candidato: int # chave estrangeira do Candidato

class InfoCandidatoBase(BaseModel):
    ds_nacionalidade: str
    nm_municipio_nascimento: str
    st_quilombola: bool
    vr_despesa_max_campanha: float
    st_reeleicao: bool # porcentagem de candidatos que tem sim e se reelegem e virse versa
    st_declarar_bens: bool
    st_prest_contas: bool

class InfoCandidatoPublic(InfoCandidatoBase, InfoCandidatoPublicMixin):
    pass

class InfoCandidatoCreate(InfoCandidatoBase, InfoCandidatoCreateMixin):
    pass

class InfoCandidatoUpdate(BaseModel):
    ds_nacionalidade: str | None = None
    nm_municipio_nascimento: str | None = None
    st_quilombola: bool | None = None
    vr_despesa_max_campanha: float | None = None
    st_reeleicao: bool | None = None
    st_declarar_bens: bool | None = None
    st_prest_contas: bool | None = None