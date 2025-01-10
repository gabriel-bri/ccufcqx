import psycopg2
from psycopg2 import OperationalError

def conexao_db():
    return psycopg2.connect(
        database="emprestimos",
        user="postgres",
        password="admin",
        host="localhost",
        port=5432
    )

def criar_tabela():
    
    conexao = conexao_db()
    cursor = conexao.cursor()
    
    try: 
        comandos = [
            """
            CREATE TABLE IF NOT EXISTS aluno (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE NOT NULL,
                matricula VARCHAR(6) UNIQUE NOT NULL
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS estoque (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                quantidade INT NOT NULL,
                tipo INT NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS pedido (
                id SERIAL PRIMARY KEY,
                id_aluno INT REFERENCES aluno(id),
                data_pedido DATE DEFAULT CURRENT_DATE NOT NULL,
                aprovado BOOLEAN,
                codigo VARCHAR(20) NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS pedido_detalhes (
                id SERIAL PRIMARY KEY,
                pedido_id INT REFERENCES pedido(id) NOT NULL,
                produto_id INT REFERENCES estoque(id) NOT NULL,
                quantidade_item INT NOT NULL
            )
            """
        ]

        for comando in comandos:
            cursor.execute(comando)

        conexao.commit()

        print("Tabelas criadas com suceso")
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and conexao:
            conexao.close()