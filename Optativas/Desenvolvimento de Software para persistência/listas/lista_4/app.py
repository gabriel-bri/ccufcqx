from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import xml.etree.ElementTree as ET
import configparser

# Cria o objeto ConfigParser
config = configparser.ConfigParser()

# Lê o arquivo de propriedades (config.ini)
config.read('config.ini')

# Obtém os valores das propriedades
ARQUIVO = config['DEFAULT'].get('arquivo')

app = FastAPI()

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano: int
    genero: str

# Funções auxiliares
def carregar_livros_xml():
    try:
        tree = ET.parse(ARQUIVO)
        root = tree.getroot()
        livros = []
        for livro in root.findall("livro"):
            livros.append({
                "id": int(livro.find("id").text),
                "titulo": livro.find("titulo").text,
                "autor": livro.find("autor").text,
                "ano": int(livro.find("ano").text),
                "genero": livro.find("genero").text,
            })
        return livros
    except FileNotFoundError:
        root = ET.Element("livros")
        tree = ET.ElementTree(root)
        tree.write(ARQUIVO, encoding="utf-8", xml_declaration=True) 
        return []

def salvar_livros_xml(livros):
    root = ET.Element("livros")
    
    for livro in livros:
        livro_elem = ET.SubElement(root, "livro")
        ET.SubElement(livro_elem, "id").text = str(livro["id"])
        ET.SubElement(livro_elem, "titulo").text = livro["titulo"]
        ET.SubElement(livro_elem, "autor").text = livro["autor"]
        ET.SubElement(livro_elem, "ano").text = str(livro["ano"])
        ET.SubElement(livro_elem, "genero").text = livro["genero"]
    tree = ET.ElementTree(root)
    tree.write(ARQUIVO, encoding="utf-8", xml_declaration=True)

# FastAPI
@app.post("/livros", status_code=201)
def criar_livro(livro: Livro):
    if livro.id < 0:
        raise HTTPException(status_code=400, detail="ID não pode ser negativo.")
    
    if livro.id == 0:
        raise HTTPException(status_code=400, detail="ID não pode ser zero.")
    
    if livro.ano < 0:
        raise HTTPException(status_code=400, detail="Ano não pode ser negativo.")
    
    if livro.ano == 0:
        raise HTTPException(status_code=400, detail="Ano não pode ser zero.")
    
    if len(str(livro.ano)) > 4 or len(str(livro.ano)) < 4:
        raise HTTPException(status_code=400, detail="Ano deve conter 4 caracteres.")

    livros = carregar_livros_xml()
    if any(l["id"] == livro.id for l in livros):
        raise HTTPException(status_code=400, detail="ID já existe.")

    livros.append(livro.dict())
    salvar_livros_xml(livros)
    
    return {
        "erro": False,
        "message": "Livro criado com sucesso"
    }

@app.get("/livros")
def listar_livros():
    livros = carregar_livros_xml()
    return livros

@app.get("/livros/{id}")
def buscar_livro(id: int):
    if id < 0:
        raise HTTPException(status_code=400, detail="ID não pode ser negativo.")
    
    if id == 0:
        raise HTTPException(status_code=400, detail="ID não pode ser zero.")
    
    livros = carregar_livros_xml()
    
    for livro in livros:
        if livro["id"] == id:
            return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado.")

@app.put("/livros/{id}")
def atualizar_livro(id: int, livro_atualizado: Livro):
    if id < 0:
        raise HTTPException(status_code=400, detail="ID não pode ser negativo.")
    
    if id == 0:
        raise HTTPException(status_code=400, detail="ID não pode ser zero.")
    
    livros = carregar_livros_xml()
    for livro in livros:
        if livro["id"] == id:
            if livro_atualizado.id < 0:
                raise HTTPException(status_code=400, detail="ID não pode ser negativo.")
            
            if livro_atualizado.id == 0:
                raise HTTPException(status_code=400, detail="ID não pode ser zero.")

            if livro_atualizado.ano < 0:
                raise HTTPException(status_code=400, detail="Ano não pode ser negativo.")
            
            if livro_atualizado.ano == 0:
                raise HTTPException(status_code=400, detail="Ano não pode ser zero.")
            
            if len(str(livro_atualizado.ano)) > 4 or len(str(livro_atualizado.ano)) < 4:
                raise HTTPException(status_code=400, detail="Ano deve conter 4 caracteres.")            
            
            livro.update(livro_atualizado.dict())
            salvar_livros_xml(livros)
            return {
                "erro": False,
                "message": "Livro atualizado com sucesso"
            }
    raise HTTPException(status_code=404, detail="Livro não encontrado.")

@app.delete("/livros/{id}")
def deletar_livro(id: int):
    if id < 0:
        raise HTTPException(status_code=400, detail="ID não pode ser negativo.")
    
    if id == 0:
        raise HTTPException(status_code=400, detail="ID não pode ser zero.")

    livros = carregar_livros_xml()
    livros_atualizados = []

    for livro in livros:
        if livro["id"] != id:
            livros_atualizados.append(livro)
    
    if len(livros) == len(livros_atualizados):
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    
    salvar_livros_xml(livros_atualizados)
    
    return {
        "erro": False,
        "message": "Livro deletado com sucesso"
    }
