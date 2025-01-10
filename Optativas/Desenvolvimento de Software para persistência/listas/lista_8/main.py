from fastapi import FastAPI, HTTPException
from crud import *
from db import criar_tabela
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Criação das tabelas no banco
criar_tabela()

@app.post("/aluno/")
def inserir_aluno(nome: str, email: str, matricula: str):    
    if not email.endswith("@alu.ufc.br"):
        raise HTTPException(status_code=400, detail="Alunos devem ser cadastrado com e-mail @alu.ufc.br.")
    
    if len(matricula) != 6:
        raise HTTPException(status_code=400, detail="Matrícula deve conter 6 dígitos.")
    
    id_aluno = inserir_aluno_db(nome, email, matricula)

    return {
        "id": id_aluno, 
        "nome": nome, 
        "email": email, 
        "matricula": matricula
    }

@app.get("/alunos/")
def listar_alunos():
    return listar_alunos_db()

@app.get("/aluno/{id}")
def listar_alunos(id: int):
    return buscar_alunos_id_db(id)

@app.put("/aluno/{id}")
def atualizar_aluno(id: int, nome: str = None, email: str = None, matricula: str = None):
    if email and not email.endswith("@alu.ufc.br"):
        raise HTTPException(status_code=400, detail="Alunos devem ser cadastrado com e-mail @alu.ufc.br.")
    
    if matricula and (len(matricula) != 6):
        raise HTTPException(status_code=400, detail="Matrícula deve conter 6 dígitos.")
    
    if nome and nome.strip() == "":
        raise HTTPException(status_code=400, detail="Nome não pode ser vazio.")
    
    atualizar_aluno_db(id, nome, email, matricula)

    return{
        "message": "Aluno atualizado com sucesso"
    }

@app.post("/estoque/")
def inserir_estoque(nome: str, quantidade: int, tipo: int):
    if quantidade < 1:
        raise HTTPException(status_code=400, detail="Quantidade mínima deve ser maior ou igual a 1.")
    
    if tipo != 1 and tipo != 2:
        raise HTTPException(status_code=400, detail="Ops, tipo de produto incorreto.")
    
    id_estoque = inserir_estoque_db(nome, quantidade, tipo)

    return {
        "id": id_estoque, 
        "nome": nome, 
        "quantidade": quantidade, 
        "tipo": tipo
    }

@app.get("/estoque/")
def listar_estoque():
    return listar_estoque_db()

@app.get("/estoque/{id}")
def listar_estoque(id: int):
    return buscar_estoque_id_db(id)

@app.put("/estoque/{id}")
def atualizar_estoque(id: int, nome: str = None, quantidade: int = None, tipo: int = None):
    if quantidade and quantidade < 1:
        raise HTTPException(status_code=400, detail="Quantidade mínima deve ser maior ou igual a 1.")
    
    if tipo and (tipo != 1 and tipo != 2):
        raise HTTPException(status_code=400, detail="Ops, tipo de produto incorreto.")

    if nome and nome.strip() == "":
        raise HTTPException(status_code=400, detail="Nome não pode ser vazio.")
    
    atualizar_estoque_db(id, nome, quantidade, tipo)

    return{
        "message": "Estoque atulizado com sucesso"
    }

@app.post("/pedido/")
def cadastrar_pedido(id_aluno: int, id_estoque: int, quantidade: int):
    if quantidade < 1:
        raise HTTPException(status_code=400, detail="Quantidade deve ser maior ou igual a 1")
    
    return inserir_pedido_db(id_aluno, id_estoque, quantidade)


@app.put("/pedido/aprovar/{id}")
def aprovar_pedido(id: int):
    aprovar_pedido_id_db(id)
    
    return {
        "message": "Pedido aprovado com sucesso",
    }

@app.put("/pedido/rejeitar/{id}")
def rejeitar_pedido(id: int):
    rejeitar_pedido_id_db(id)
    
    return {
        "message": "Pedido rejeitado com sucesso",
    }

@app.get("/pedidos/aprovados")
def pedidos_aprovados():
    return buscar_usuarios_com_pedidos_aprovados_db()

@app.get("/pedidos/rejeitados")
def pedidos_rejeitados():
    return buscar_usuarios_com_pedidos_rejeitados_db()

@app.get("/pedidos/estatisticas")
def contagem_pedidos():
    return contar_pedidos_aprovados_rejeitados_db()

@app.get("/pedidos/aprovados/data")
def pedidos_por_data():
    return buscar_pedidos_aprovados_ordenados_por_data_db()