import os
from db import conexao_db
from fastapi import HTTPException
from psycopg2.errors import UniqueViolation
from psycopg2.extras import RealDictCursor
from datetime import datetime

def fechar_recursos(cursor, conexao):
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()

# Alunos
def inserir_aluno_db(nome: str, email: str, matricula: str):
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO aluno (nome, email, matricula) VALUES (%s, %s, %s) RETURNING id",
            (nome, email, matricula)
        )
        ultima_insercao = cursor.fetchone()[0]
        conexao.commit()
        return ultima_insercao

    except UniqueViolation as e:
        if "aluno_email_key" in str(e):
            raise HTTPException(
                status_code=400,
                detail="E-mail já cadastrado no sistema."
            )
        elif "aluno_matricula_key" in str(e):
            raise HTTPException(
                status_code=400,
                detail="Matrícula já cadastrada no sistema."
            )
        else:
            raise HTTPException(
                status_code=400,
                detail="E-mail ou matrícula já cadastrados no sistema."
            )

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno do servidor: {str(e)}"
        )
    
    finally:
        fechar_recursos(cursor, conexao)

def listar_alunos_db():
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM aluno")
        alunos = cursor.fetchall()

        if not alunos:
            raise HTTPException(
                status_code=404,
                detail="Nenhum aluno encontrado."
            )
        
        return alunos

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao realizar a consulta ao banco de dados: {e}")

    finally:
        fechar_recursos(cursor, conexao)

def buscar_alunos_id_db(id_aluno: int):
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM aluno WHERE id = %s", (id_aluno,))
        aluno = cursor.fetchone()

        if not aluno:
            raise HTTPException(
                status_code=404,
                detail="Nenhum aluno encontrado."
            )
        
        return aluno

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao realizar a consulta ao banco de dados: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)

def atualizar_aluno_db(id: int, nome: str, email: str, matricula: str):
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM aluno WHERE id = %s", (id,))
        aluno = cursor.fetchone()

        if not aluno:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        
        if nome:
            cursor.execute("UPDATE aluno SET nome = %s WHERE id = %s", (nome, id))
        if email:
            cursor.execute("UPDATE aluno SET email = %s WHERE id = %s", (email, id))
        if matricula:
            cursor.execute("UPDATE aluno SET matricula = %s WHERE id = %s", (matricula, id))
        
        conexao.commit()

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao atualizar aluno: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)

# Estoque
def inserir_estoque_db(nome: str, quantidade: int, tipo: int):
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO estoque (nome, quantidade, tipo) VALUES (%s, %s, %s) RETURNING id",
            (nome, quantidade, tipo)
        )
        ultima_insercao = cursor.fetchone()[0]
        conexao.commit()
        return ultima_insercao

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno do servidor: {e}"
        )
    
    finally:
        fechar_recursos(cursor, conexao)

def listar_estoque_db():
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM estoque")
        estoque = cursor.fetchall()

        if not estoque:
            raise HTTPException(
                status_code=404,
                detail="Nenhum item cadastrado no estoque."
            )
        
        return estoque

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao realizar a consulta ao banco de dados: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)

def atualizar_estoque_db(id: int, nome: str, quantidade: int, tipo: int):
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM estoque WHERE id = %s", (id,))
        item = cursor.fetchone()

        if not item:
            raise HTTPException(status_code=404, detail="Item não encontrado")
        
        if nome:
            cursor.execute("UPDATE estoque SET nome = %s WHERE id = %s", (nome, id))
        if quantidade:
            cursor.execute("UPDATE estoque SET quantidade = %s WHERE id = %s", (quantidade, id))
        if tipo:
            cursor.execute("UPDATE estoque SET tipo = %s WHERE id = %s", (tipo, id))
        
        conexao.commit()

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao atualizar estoque: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)

def buscar_estoque_id_db(id_estoque: int):
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM estoque WHERE id = %s", (id_estoque,))
        estoque = cursor.fetchone()

        if not estoque:
            raise HTTPException(
                status_code=404,
                detail="Nenhum item encontrado."
            )
        
        return estoque

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao realizar a consulta ao banco de dados: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)

# Pedido
def inserir_pedido_db(id_aluno: int, id_estoque: int, quantidade: int):
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor()
        buscar_alunos_id_db(id_aluno)
        buscar_estoque_id_db(id_estoque)
        codigo_pedido = os.urandom(10).hex()
        data_atual = datetime.now()

        cursor.execute(
            "INSERT INTO pedido (id_aluno, data_pedido, codigo) VALUES (%s, %s, %s) RETURNING id, codigo",
            (id_aluno, data_atual, codigo_pedido)
        )
        id_pedido, codigo = cursor.fetchone()
        
        cursor.execute(
            "INSERT INTO pedido_detalhes (pedido_id, produto_id, quantidade_item) VALUES (%s, %s, %s)",
            (id_pedido, id_estoque, quantidade)
        )
        conexao.commit()
        return {
            "message": "Pedido cadastrado com sucesso",
            "codigo": codigo, 
            "id": id_pedido
        }


    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno do servidor: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)

def aprovar_pedido_id_db(id_pedido: int):
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT id, aprovado FROM pedido WHERE id = %s", (id_pedido,))
        pedido = cursor.fetchone()

        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")

        if pedido[1] is not None:
            raise HTTPException(status_code=400, detail="Pedido já aprovado ou rejeitado.")

        cursor.execute(
            "UPDATE pedido SET aprovado = %s WHERE id = %s RETURNING id",
            (True, id_pedido)
        )
        
        resultado = cursor.fetchone()

        if not resultado:
            raise HTTPException(status_code=500, detail="Falha ao aprovar o pedido")

        conexao.commit()
    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao aprovar pedido: {e}")

    finally:
        fechar_recursos(cursor, conexao)

def rejeitar_pedido_id_db(id_pedido: int):
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT id, aprovado FROM pedido WHERE id = %s", (id_pedido,))
        pedido = cursor.fetchone()

        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")

        if pedido[1] is not None:
            raise HTTPException(status_code=400, detail="Pedido já aprovado ou rejeitado.")

        cursor.execute(
            "UPDATE pedido SET aprovado = %s WHERE id = %s RETURNING id",
            (False, id_pedido)
        )
        
        resultado = cursor.fetchone()

        if not resultado:
            raise HTTPException(status_code=500, detail="Falha ao rejeitar o pedido")

        conexao.commit()
    
    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao rejeitar pedido: {e}")

    finally:
        fechar_recursos(cursor, conexao)

def buscar_usuarios_com_pedidos_aprovados_db():
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        
        usuarios_pedido_aprovado = """
        SELECT
            a.id AS aluno_id,
            a.nome AS aluno_nome,
            a.email AS aluno_email,
            a.matricula AS aluno_matricula,
            p.id AS pedido_id,
            p.codigo AS pedido_codigo,
            p.data_pedido AS pedido_data,
            p.aprovado AS pedido_aprovado,
            pd.id AS pedido_detalhes_id,
            pd.quantidade_item AS pedido_detalhes_quantidade,
            e.id AS estoque_id,
            e.nome AS estoque_nome
        FROM
            aluno a
        INNER JOIN
            pedido p ON a.id = p.id_aluno
        INNER JOIN
            pedido_detalhes pd ON p.id = pd.pedido_id
        INNER JOIN
            estoque e ON pd.produto_id = e.id
        WHERE
            p.aprovado = TRUE;
        """
        
        cursor.execute(usuarios_pedido_aprovado)
        resultados = cursor.fetchall()

        if not resultados:
            raise HTTPException(
                status_code=404,
                detail="Nenhum pedido aprovado encontrado."
            )
        
        return resultados
    
    except HTTPException as http_err:
        raise http_err
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar pedidos aprovados: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)

def buscar_usuarios_com_pedidos_rejeitados_db():
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)
        
        usuarios_pedido_rejeitado = """
        SELECT
            a.id AS aluno_id,
            a.nome AS aluno_nome,
            a.email AS aluno_email,
            a.matricula AS aluno_matricula,
            p.id AS pedido_id,
            p.codigo AS pedido_codigo,
            p.data_pedido AS pedido_data,
            p.aprovado AS pedido_aprovado,
            pd.id AS pedido_detalhes_id,
            pd.quantidade_item AS pedido_detalhes_quantidade,
            e.id AS estoque_id,
            e.nome AS estoque_nome
        FROM
            aluno a
        INNER JOIN
            pedido p ON a.id = p.id_aluno
        INNER JOIN
            pedido_detalhes pd ON p.id = pd.pedido_id
        INNER JOIN
            estoque e ON pd.produto_id = e.id
        WHERE
            p.aprovado = FALSE;
        """
        
        cursor.execute(usuarios_pedido_rejeitado)
        resultados = cursor.fetchall()

        if not resultados:
            raise HTTPException(
                status_code=404,
                detail="Nenhum pedido rejeitado encontrado."
            )
        
        return resultados
    
    except HTTPException as http_err:
        raise http_err
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar pedidos rejeitados: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)

def contar_pedidos_aprovados_rejeitados_db():
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)

        contar_pedidos_aprovados_rejeitados = """
        SELECT 
            COUNT(*) FILTER (WHERE aprovado = TRUE) AS pedidos_aprovados,
            COUNT(*) FILTER (WHERE aprovado = FALSE) AS pedidos_rejeitados
        FROM pedido;
        """

        cursor.execute(contar_pedidos_aprovados_rejeitados)
        resultado = cursor.fetchone()

        if not resultado:
            raise HTTPException(
                status_code=404,
                detail="Erro ao contar os pedidos."
            )
        
        return resultado
    
    except HTTPException as http_err:
        raise http_err
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao contar pedidos aprovados e rejeitados: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)

def buscar_pedidos_aprovados_ordenados_por_data_db():
    conexao = None
    cursor = None
    try:
        conexao = conexao_db()
        cursor = conexao.cursor(cursor_factory=RealDictCursor)

        pedidos_por_data = """
        SELECT 
            p.id,
            p.id_aluno,
            a.nome AS nome_aluno,
            p.codigo,
            p.aprovado,
            p.data_pedido,
            e.nome AS nome_item
        FROM pedido p
        INNER JOIN aluno a ON p.id_aluno = a.id
        INNER JOIN pedido_detalhes pd ON p.id = pd.pedido_id
        INNER JOIN estoque e ON pd.produto_id = e.id
        WHERE p.aprovado = true
        ORDER BY p.data_pedido DESC;
        """
        
        cursor.execute(pedidos_por_data)
        resultados = cursor.fetchall()

        if not resultados:
            raise HTTPException(
                status_code=404,
                detail="Nenhum pedido aprovado encontrado."
            )
        
        return resultados
    
    except HTTPException as http_err:
        raise http_err
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao buscar pedidos aprovados: {e}"
        )

    finally:
        fechar_recursos(cursor, conexao)