from pymongo import MongoClient

# Conecte-se ao MongoDB na VM (substitua o IP pelo da sua VM)
client = MongoClient('mongodb://192.168.120.139:27017')

# Verifique se a conexão foi bem-sucedida verificando o status do servidor
try:
    # Acesse a instância do MongoDB e verifique a conexão
    print("Conectando ao MongoDB...")
    client.admin.command('ping')  # Comando simples para testar a conexão

    print("Conexão bem-sucedida!")
except Exception as e:
    print("Erro ao conectar ao MongoDB:", e)

# Agora você pode interagir com o banco de dados
db = client.test  # Exemplo de acesso a um banco de dados chamado 'test'
