from fastapi import FastAPI, HTTPException, Response, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import csv
import os
from http import HTTPStatus
import hashlib
from zipfile import ZipFile # Criar zip  
from io import BytesIO
import logging
import yaml

# Carregar configurações do arquivo YAML
with open('config.yaml', 'r') as yaml_file:
    configuracao_log = yaml.safe_load(yaml_file)

# Configurações de logging a partir do YAML
log_config = configuracao_log['logging']
nivel_log = log_config['level']
arquivo_log = log_config['file']
formato_log = log_config['format']
codificacao_log = log_config['encoding']

# Configurando o logging
logging.basicConfig(
    filename = arquivo_log,
    level = getattr(logging, nivel_log.upper(), logging.INFO),
    format = formato_log,
    datefmt = "%Y-%m-%d %H:%M:%S",
    encoding = codificacao_log
)

app = FastAPI()

CSV_file = configuracao_log['data']['file']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Aqui você pode colocar apenas os domínios que você deseja permitir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Evento(BaseModel):
    id: int
    titulo: str
    descricao: str
    data: datetime
    local: str
    publicoEsperado: int

def lerDadosCSV():
    try:
        with open(CSV_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            eventos = []
            for row in reader:
                row['data'] = datetime.fromisoformat(row['data'])
                eventos.append(Evento(**row))
        return eventos
    except FileNotFoundError:
        logging.error(f"Arquivo CSV '{CSV_file}' não encontrado.")
        return []
    except csv.Error as e:
        logging.error(f"Erro ao decodificar o arquivo CSV '{e}'.")
        return []
    except UnicodeDecodeError:
        logging.error("O arquivo CSV contém caracteres que não pdem ser decoficados")
        return []
    except Exception as e:
        logging.error(f"Erro inesperado '{e}'.")
        return []

def escreverDadosCSV(eventos):
    try:
        with open(CSV_file, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "titulo", "descricao", "data", "local", "publicoEsperado"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for evento in eventos:
                evento_dict = evento.dict()
                evento_dict["data"] = evento.data.isoformat()
                writer.writerow(evento.dict())
    except Exception as e:
        logging.error(f"Erro ao salvar o arquivo CSV '{CSV_file}': {e}")

def calcular_hash():
    sha256 = hashlib.sha256()
    with open(CSV_file, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

@app.get("/eventos", response_model=list[Evento])
def listarEventos():
    logging.info(f"Listando eventos. Total de eventos: {len(lerDadosCSV())}")
    return lerDadosCSV()

@app.post("/eventos", response_model=Evento, status_code=HTTPStatus.CREATED)
def criarEvento(evento: Evento):
    if(evento.publicoEsperado < 1):
        logging.warning(f"Tentativa de criação de evento com público esperado inválido: {evento.publicoEsperado}")
        raise HTTPException(status_code=400, detail="Erro ao criar evento: Publico esperado deve ser maior ou igual a 1.")

    try:            
        eventos = lerDadosCSV()
        if eventos:
            evento.id = max(evento.id for evento in eventos) + 1
        else:
            evento.id = 1  # Caso seja o primeiro evento
        eventos.append(evento)
        escreverDadosCSV(eventos)
        logging.info(f"Evento criado com sucesso: {evento.id} - {evento.titulo}")
        return evento
    except Exception as e:
        logging.error(f"Erro ao criar evento: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Erro ao criar evento: {str(e)}")

@app.put("/eventos/{id}", response_model=Evento)
def atualizarEvento(id: int, eventoAtualizado: Evento):
    if(eventoAtualizado.publicoEsperado < 1):
        logging.warning(f"Tentativa de atualização de evento com público esperado inválido: {eventoAtualizado.publicoEsperado}")
        raise HTTPException(status_code=400, detail="Erro ao atualizar evento: Publico esperado deve ser maior ou igual a 1.")
    
    eventos = lerDadosCSV()
    for i, evento in enumerate(eventos):
        if evento.id == id:
            eventos[i] = eventoAtualizado
            escreverDadosCSV(eventos)
            logging.info(f"Evento atualizado com sucesso: {id} - {eventoAtualizado.titulo}")
            return eventoAtualizado
    logging.error(f"Erro ao atualizar evento: Evento com ID {id} não encontrado.")
    raise HTTPException(status_code=404, detail="Evento não encontrado")


@app.delete("/eventos/{id}")
def removerEventos(id: int):
    eventos = lerDadosCSV()

    for i, evento in enumerate(eventos):
        if evento.id == id:
            eventos.pop(i)
            escreverDadosCSV(eventos)
            logging.info(f"Evento deletado com sucesso: {id} - {evento.titulo}")
            return {"id": id, "message": "Evento deletado"}
        
    logging.error(f"Erro ao deletar evento: Evento com ID {id} não encontrado.")
    raise HTTPException(status_code=404, detail="Evento não encontrado")

@app.get("/eventos/quantidade")
def quantidadeTotalEventos():
    if not os.path.exists(CSV_file):
        logging.error("Nenhum evento encontrado, arquivo CSV inexistente.")
        return {"quantidade" : 0}
    with open(CSV_file, mode="r", newline="") as file:
        reader = csv.reader(file)
        total = sum(1 for _ in reader) - 1
    logging.info(f"Total de eventos: {total}")
    return {"quantidade": total if total > 0 else 0}
    
@app.get("/integridade")
def verificarIntegridade():
    logging.info(f"Verificação de integridade realizada. Hash: {calcular_hash()}")
    return {"hash" : calcular_hash()}

@app.get("/backup")
def download_zip():
    NOME_ZIP = "backup.zip"

    if not os.path.exists(CSV_file):
        logging.error(f"Arquivo CSV {CSV_file} não encontrado para backup.")
        return {"error": f"O arquivo {CSV_file} não foi encontrado."}
    
    hash_csv = calcular_hash()
    
    copia_memoria_zip = BytesIO()
    with ZipFile(copia_memoria_zip, "w") as arquivo_backup:
        arquivo_backup.write(CSV_file, arcname=CSV_file)
        arquivo_backup.comment = hash_csv.encode("utf-8") # Copiei a ideia de como o Github faz quando baixa arquivo .zip

    copia_memoria_zip.seek(0)

    logging.info(f"Backup do arquivo CSV realizado com sucesso.")
    
    return Response(
        copia_memoria_zip.getvalue(),
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename={NOME_ZIP}"}
    )

@app.get("/eventos/filtro", response_model=list[Evento])
def filtrarEventos(
    titulo: Optional[str] = Query(None, alias="nome", description="Filtrar pelo título do evento"),
    data_inicio: Optional[datetime] = Query(None, description="Filtrar eventos a partir dessa data"),
    data_fim: Optional[datetime] = Query(None, description="Filtrar eventos até essa data")
):
    eventos = lerDadosCSV()
    
    # Filtros
    if titulo:
        filtro_busca = []
        for evento in eventos:
            if titulo.lower() in evento.titulo.lower():
                filtro_busca.append(evento)
        eventos = filtro_busca 
    
    if data_inicio:
        filtro_busca = []
        for evento in eventos:
            if evento.data.date() >= data_inicio.date():
                filtro_busca.append(evento)
        eventos = filtro_busca

    if data_fim:
        filtro_busca = []
        for evento in eventos:
            if evento.data.date() <= data_fim.date():
                filtro_busca.append(evento)
        eventos = filtro_busca

    if not eventos:
        parametros_filtro = {
            "titulo": titulo,
            "data_inicio": data_inicio,
            "data_fim": data_fim
        }
        logging.warning(f"Nenhum evento encontrado com os filtros fornecidos. {parametros_filtro}")
        raise HTTPException(status_code=404, detail="Nenhum evento encontrado utilizando os filtros atuais. Que tal fazer uma nova busca?")
    
    logging.info(f"Eventos filtrados com sucesso. Total: {len(eventos)}")
    return eventos

# pegar os dados de um evento especifico para atualizar
@app.get("/eventos/{id}", response_model=Evento)
async def buscarEvento(id: int):
    eventos = lerDadosCSV()
    evento = next((evento for evento in eventos if evento.id == id), None)
    if evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return evento