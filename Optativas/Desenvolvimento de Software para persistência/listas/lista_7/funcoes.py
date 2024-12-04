import os
from criptografia import * # Funções referentes a criptografia estão em criptografia.py

def criar_arquivo():
    nome_arquivo = input("Digite o nome do novo arquivo (sem espaços):")
        
    if " " in nome_arquivo:
        nome_arquivo = nome_arquivo.replace(" ", "_")

    if not os.path.exists(nome_arquivo + ".txt"):
        with open(nome_arquivo + ".txt", "w", encoding="utf-8") as arquivo_original:
            arquivo_original.write("Este é um teste de criptografia RSA com verificação de integridade para a disciplina de Desenvolvimento de Software para Persistência.")

        print("Arquivo criado com sucesso.")
    else:
        print("Ops, já existe um arquivo com este nome. Que tal escolher outro?")
        return False

def validar_hash():
    nome_arquivo = input("Digite o nome do arquivo original que voce deseja calcular o hash (com a extensão):")

    if nome_arquivo.endswith(".txt"):
        if os.path.exists(nome_arquivo):
            if os.path.exists(nome_arquivo + ".dec"):
                verificar_integridade(nome_arquivo, nome_arquivo + ".dec")
            else:
                print("Ops, não encontramos o arquivo decriptado. Realiza a criptografia novamente.")
        else:
            print(f"O arquivo '{nome_arquivo}' não existe. Verifique o nome e tente novamente.")
    else:
        print("Ops, este tipo de extensão ainda não aceitamos.")

def criar_arquivo_vazio():
    nome_arquivo = input("Digite o nome do novo arquivo (sem espaços):")

    if " " in nome_arquivo:
        nome_arquivo = nome_arquivo.replace(" ", "_")
    
    if not os.path.exists(nome_arquivo + ".txt"):
        with open(nome_arquivo + ".txt", "w", encoding="utf-8") as arquivo_original:
            arquivo_original.write("")

        print("Arquivo criado com sucesso.")
    else:
        print("Ops, já existe um arquivo com este nome. Que tal escolher outro?")
        return False
    
def listar_arquivos():
    arquivos_diretorio = []
    for arquivo in os.listdir():
        if(arquivo.endswith(".txt") or arquivo.endswith(".dec") or arquivo.endswith(".enc")):
           arquivos_diretorio.append(arquivo)

    if(len(arquivos_diretorio) != 0):
        for arquivo in arquivos_diretorio:
            print(arquivo)
    else:
        print("Ops, parece que não temos arquivos válidos por aqui.")

def ler_conteudo():
    nome_arquivo = input("Digite o nome do arquivo que você deseja ver o conteúdo (com a extensão):")

    if(nome_arquivo.endswith(".txt") or nome_arquivo.endswith(".dec")):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                if conteudo:
                    print("Conteúdo do arquivo:")
                    print(conteudo)
                else: 
                    print("Ops, parece que seu arquivo está vazio. Que tal adicionar conteúdo a ele?")
        else:
            print(f"O arquivo '{nome_arquivo}' não existe. Verifique o nome e tente novamente.")
    else:
        print("Ops, este tipo de extensão ainda não aceitamos.")

def validar_criptografia():
    nome_arquivo = input("Digite o nome do arquivo que você deseja criptografar (com a extensão):")

    arquivos_criptografia = ["chave_publica.pem", "chave_privada.pem"]

    if(nome_arquivo.endswith(".txt")):
        if os.path.exists(nome_arquivo):
            if not os.path.exists(arquivos_criptografia[0]) or not os.path.exists(arquivos_criptografia[1]):
                print("Ops, os arquivos necessários para criptografar o arquivo não existe no seu computador. Vamos gerar agora mesmo.")
                gerar_chaves()
                print("Inicie o processo novamente.")
                return False
            else:
                criptografar_arquivo(nome_arquivo, arquivos_criptografia[0])
        else:
            print(f"O arquivo '{nome_arquivo}' não existe. Verifique o nome e tente novamente.")
            return False
    else:
        print("Ops, este tipo de extensão ainda não aceitamos.")
        return False

def validar_descriptografia():
    nome_arquivo = input("Digite o nome do arquivo que você deseja descriptografar (com a extensão):")

    arquivos_criptografia = ["chave_publica.pem", "chave_privada.pem"]

    if(nome_arquivo.endswith(".enc")):
        if os.path.exists(nome_arquivo):
            if not os.path.exists(arquivos_criptografia[0]) or not os.path.exists(arquivos_criptografia[1]):
                print("Ops, os arquivos necessários para criptografar o arquivo não existe no seu computador. Vamos gerar agora mesmo.")
                gerar_chaves()
                print("Inicie o processo novamente.")
                return False
            else:
                decriptar_arquivo(nome_arquivo, arquivos_criptografia[1])
        else:
            print(f"O arquivo '{nome_arquivo}' não existe. Verifique o nome e tente novamente.")
            return False
    else:
        print("Ops, este tipo de extensão ainda não aceitamos.")
        return False

def apagar_conteudo():
    nome_arquivo = input("Digite o nome do arquivo que você deseja apagar o conteúdo (com a extensão):")

    if(nome_arquivo.endswith(".txt")):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                arquivo.write("")
                print("Conteúdo do arquivo deletado!")
        else:
            print(f"O arquivo '{nome_arquivo}' não existe. Verifique o nome e tente novamente.")
    else:
        print("Ops, este tipo de extensão ainda não aceitamos.")

def inserir_conteudo():
    nome_arquivo = input("Digite o nome do arquivo que você deseja inserir o conteúdo (com a extensão):")

    if(nome_arquivo.endswith(".txt")):
        if os.path.exists(nome_arquivo):
            conteudo_novo = input("Ok, e o que você deseja inserir no arquivo?")

            with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
                arquivo.write(conteudo_novo + "\n")
                print("Conteúdo gravado com sucesso!")
        else:
            print(f"O arquivo '{nome_arquivo}' não existe. Verifique o nome e tente novamente.")
    else:
        print("Ops, este tipo de extensão ainda não aceitamos.")

def apagar_arquivo():
    nome_arquivo = input("Digite o nome do arquivo que você deseja apagar (com a extensão):")

    if(nome_arquivo.endswith(".txt") or nome_arquivo.endswith(".dec") or nome_arquivo.endswith(".dec")):
        if os.path.exists(nome_arquivo):
            os.remove(nome_arquivo)
            print("Arquivo removido com sucesso!")
        else:
            print(f"O arquivo '{nome_arquivo}' não existe. Verifique o nome e tente novamente.")
    else:
        print("Ops, este tipo de extensão ainda não aceitamos.")

def limpar_tela():
    if os.name == 'nt': # Verificar se é Windows ou Linux
        os.system("cls")
    else:
        os.system("clear")
        