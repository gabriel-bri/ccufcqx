from models.eleicao import EleicaoCreate, EleicaoPublic
from datetime import datetime

def eleicao_entity(entity: dict) -> EleicaoCreate:
    return {
        "cd_eleicao" : entity['cd_eleicao'],  # Transformando para string
        "ds_eleicao" : entity['ds_eleicao'],  # Descrição da eleição
        "dt_eleicao" : entity['dt_eleicao'],  # Convertendo string para datetime
        "ano_eleicao" : entity['ano_eleicao'],  # Convertendo para string
        "cd_tipo_eleicao" :entity['cd_tipo_eleicao'],  # Convertendo para string
        "nm_tipo_eleicao" : entity['nm_tipo_eleicao'],  # Nome do tipo de eleição
        "tp_abrangencia" : entity['tp_abrangencia'],  # Tipo de abrangência da eleição
        "nr_turno" : entity['nr_turno'],  # Convertendo para string
    }

def eleicao_entity_from_db(entity: dict) -> EleicaoPublic:
    eleicao = {
        'id': str(entity['_id']),
        **eleicao_entity(entity)
    }
    
    return eleicao

def eleicao_entities_from_db(entities: list) -> list[EleicaoPublic]:
    return [eleicao_entity_from_db(entity) for entity in entities]