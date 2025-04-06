from models.BensCandidato import BensCandidatoCreate, BensCandidatoPublic

def bens_candidato_entity(entity: dict) -> BensCandidatoCreate:
    return {
        "nr_titulo_eleitoral_candidato": entity['nr_titulo_eleitoral_candidato'],
        "sq_candidato": entity['sq_candidato'],
        "nr_ordem_bem_candidato": entity['nr_ordem_bem_candidato'],
        "ds_tipo_bem_candidato": entity['ds_tipo_bem_candidato'],
        "ds_bem_candidato": entity['ds_bem_candidato'],
        "vr_bem_candidato": entity['vr_bem_candidato'],
        "dt_ult_atual_bem_candidato": entity['dt_ult_atual_bem_candidato'],
        "hh_ult_atual_bem_candidato": entity['hh_ult_atual_bem_candidato']
    }

def bens_candidato_entity_from_db(entity: dict) -> BensCandidatoPublic:
    bens_candidato = {
        'id': str(entity['_id']),
        **bens_candidato_entity(entity)
    }
    
    return BensCandidatoPublic(**bens_candidato)

def bens_candidato_entities_from_db(entities: list) -> list[BensCandidatoPublic]:
    return [bens_candidato_entity_from_db(entity) for entity in entities]