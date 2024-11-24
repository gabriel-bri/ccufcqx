import logging
import json
import yaml
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Carregar configurações do arquivo YAML
with open('config.yaml', 'r') as yaml_file:
    configuracao_log = yaml.safe_load(yaml_file)

ARQUIVO_JSON = configuracao_log['data']['file']

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

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    genero: str

# Funções auxiliares
def carregar_livros_json():
    try:
        # Carregar o arquivo JSON
        with open(ARQUIVO_JSON, 'r') as json_file:
            livros = json.load(json_file)
        logging.info(f"Arquivo JSON '{ARQUIVO_JSON}' carregado com sucesso.")
        return livros
    except FileNotFoundError:
        logging.error(f"Arquivo JSON '{ARQUIVO_JSON}' não encontrado.")
        return []
    except json.JSONDecodeError:
        logging.error(f"Erro ao decodificar o arquivo JSON '{ARQUIVO_JSON}'.")
        return []

def salvar_livros_json(livros):
    try:
        with open(ARQUIVO_JSON, 'w') as json_file:
            json.dump(livros, json_file, indent=4)
        logging.info(f"Arquivo JSON '{ARQUIVO_JSON}' salvo com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao salvar o arquivo JSON '{ARQUIVO_JSON}': {e}")

# FastAPI
@app.post("/livros", status_code=201)
def criar_livro(livro: Livro):
    if livro.id < 0:
        logging.error(f"Erro: ID não pode ser negativo. Recebido: {livro.id}")
        raise HTTPException(status_code=400, detail="ID não pode ser negativo.")
    
    if livro.id == 0:
        logging.error(f"Erro: ID não pode ser zero.")
        raise HTTPException(status_code=400, detail="ID não pode ser zero.")
    
    if livro.ano < 0:
        logging.error(f"Erro: Ano não pode ser negativo. Recebido: {livro.ano}")
        raise HTTPException(status_code=400, detail="Ano não pode ser negativo.")
    
    if livro.ano == 0:
        logging.error(f"Erro: Ano não pode ser zero.")
        raise HTTPException(status_code=400, detail="Ano não pode ser zero.")
    
    if len(str(livro.ano)) > 4 or len(str(livro.ano)) < 4:
        logging.error(f"Erro: Ano deve conter 4 caracteres.")
        raise HTTPException(status_code=400, detail="Ano deve conter 4 caracteres.")

    livros = carregar_livros_json()
    if any(l["id"] == livro.id for l in livros):
        logging.warning(f"ID já existe.")
        raise HTTPException(status_code=400, detail="ID já existe.")
    
    livros.append(livro.dict())
    salvar_livros_json(livros)
    
    logging.info(f"Livro criado com sucesso: {livro.dict()}")
    
    return {
        "erro": False,
        "message": "Livro criado com sucesso"
    }

@app.get("/livros")
def listar_livros():
    livros = carregar_livros_json()
    return livros

@app.get("/livros/{id}")
def buscar_livro(id: int):
    if id < 0:
        logging.error(f"Erro: ID não pode ser negativo. Recebido: {id}")
        raise HTTPException(status_code=400, detail="ID não pode ser negativo.")
    
    if id == 0:
        logging.error(f"Erro: ID não pode ser zero.")
        raise HTTPException(status_code=400, detail="ID não pode ser zero.")
    
    livros = carregar_livros_json()
    
    for livro in livros:
        if livro["id"] == id:
            logging.info(f"Livro encontrado: {livro}")
            return livro
    logging.warning(f"Livro com ID {id} não encontrado.")
    raise HTTPException(status_code=404, detail="Livro não encontrado.")

@app.put("/livros/{id}")
def atualizar_livro(id: int, livro_atualizado: Livro):
    if id < 0:
        logging.error(f"Erro: ID não pode ser negativo. Recebido: {id}")
        raise HTTPException(status_code=400, detail="ID não pode ser negativo.")
    
    if id == 0:
        logging.error(f"Erro: ID não pode ser zero.")
        raise HTTPException(status_code=400, detail="ID não pode ser zero.")
    
    livros = carregar_livros_json()
    for livro in livros:
        if livro["id"] == id:
            livro.update(livro_atualizado.dict())
            salvar_livros_json(livros)
            logging.info(f"Livro atualizado com sucesso: {livro_atualizado.dict()}")
            return {
                "erro": False,
                "message": "Livro atualizado com sucesso"
            }
        
    logging.warning(f"Livro com ID {id} não encontrado para atualização.")
    raise HTTPException(status_code=404, detail="Livro não encontrado.")

@app.delete("/livros/{id}")
def deletar_livro(id: int):
    if id < 0:
        logging.error(f"Erro: ID não pode ser negativo. Recebido: {id}")
        raise HTTPException(status_code=400, detail="ID não pode ser negativo.")
    
    if id == 0:
        raise HTTPException(status_code=400, detail="ID não pode ser zero.")

    livros = carregar_livros_json()
    livros_atualizados = []

    for livro in livros:
        if livro["id"] != id:
            livros_atualizados.append(livro)
    
    if len(livros) == len(livros_atualizados):
        logging.warning(f"Livro com ID {id} não encontrado para exclusão.")
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    
    salvar_livros_json(livros_atualizados)
    
    logging.info(f"Livro com ID {id} deletado com sucesso.")
    
    return {
        "erro": False,
        "message": "Livro deletado com sucesso"
    }