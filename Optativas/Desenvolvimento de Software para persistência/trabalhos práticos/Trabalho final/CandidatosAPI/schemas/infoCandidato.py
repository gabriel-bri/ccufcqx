from models.infoCandidato import InfoCandidatoCreate, InfoCandidatoPublic

def check_boolean_equals_s(value):
    return True if value == 'S' else False
    
# from csv
def info_candidato_entity(entity: dict) -> InfoCandidatoCreate:
    return {
        'nr_titulo_eleitoral_candidato': entity['nr_titulo_eleitoral_candidato'],
        'ds_nacionalidade': entity['ds_nacionalidade'],
        'nm_municipio_nascimento': entity['nm_municipio_nascimento'],
        'st_quilombola': check_boolean_equals_s(entity['st_quilombola']),
        'vr_despesa_max_campanha': entity['vr_despesa_max_campanha'],
        'st_reeleicao': check_boolean_equals_s(entity['st_reeleicao']),
        'st_declarar_bens': check_boolean_equals_s(entity['st_declarar_bens']),
        'st_prest_contas': check_boolean_equals_s(entity['st_prest_contas'])
    }

def info_candidatos_entity(entities: list) -> list[InfoCandidatoPublic]:
    return [info_candidato_entity(entity) for entity in entities]