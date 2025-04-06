from models.Candidatura import CandidaturaCreate, CandidaturaPublic

def candidatura_entity(entity: dict) -> CandidaturaCreate:
    return {
        "sq_candidato": entity["sq_candidato"],
        "nm_candidato": entity["nm_candidato"],
        "cd_eleicao": entity["cd_eleicao"],
        "sg_uf": entity["sg_uf"],
        "ds_cargo": entity["ds_cargo"],
        "nr_candidato": entity["nr_candidato"],
        "nr_partido": entity["nr_partido"],
        "sg_partido": entity["sg_partido"],
        "nm_partido": entity["nm_partido"],
        "nr_turno": entity["nr_turno"],
        "tp_agremiacao": entity["tp_agremiacao"],
        "ds_sit_tot_turno": entity["ds_sit_tot_turno"],
        "ds_tp_motivo": entity.get("ds_tp_motivo",""),
        "ds_motivo": entity.get("ds_motivo","")
    }

def candidatura_entity_from_db(entity: dict) -> CandidaturaPublic:
    candidatura = {
        "id": str(entity["_id"]),
        **candidatura_entity(entity)
    }
    return CandidaturaPublic(**candidatura)

def candidatura_entities_from_db(entities: list) -> list[CandidaturaPublic]:
    return [candidatura_entity_from_db(entity) for entity in entities]
