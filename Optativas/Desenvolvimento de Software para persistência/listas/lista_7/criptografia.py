from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import hashlib

def gerar_chaves():
    chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    chave_publica = chave_privada.public_key()

    # Chave privada
    with open("chave_privada.pem", "wb") as arquivo_chave_privada:
        arquivo_chave_privada.write(
            chave_privada.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # Chave pública
    with open("chave_publica.pem", "wb") as arquivo_chave_publica:
        arquivo_chave_publica.write(
            chave_publica.public_bytes( 
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("Chaves pública e privada geradas com suceso.")

# Função para criptografar um arquivo com a chave pública
def criptografar_arquivo(caminho_arquivo, caminho_chave_publica):
    with open(caminho_arquivo, "rb") as arquivo:
        dados = arquivo.read()

    with open(caminho_chave_publica, "rb") as arquivo_chave_publica:
        chave_publica = serialization.load_pem_public_key(arquivo_chave_publica.read())

    dados_criptografados = chave_publica.encrypt(
        dados,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(caminho_arquivo + ".enc", "wb") as arquivo_encriptado:
        arquivo_encriptado.write(dados_criptografados)

    print("Arquivo criptografado com sucesso!")

# Função para decriptar um arquivo com a chave privada
def decriptar_arquivo(caminho_arquivo_criptografado, caminho_chave_privada):
    with open(caminho_arquivo_criptografado, "rb") as enc_file:
        dados_criptografados = enc_file.read()

    with open(caminho_chave_privada, "rb") as arquivo_chave_privada:
        chave_privada = serialization.load_pem_private_key(arquivo_chave_privada.read(), password=None)

    try:
        dados_original = chave_privada.decrypt(
            dados_criptografados,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        caminho_arquivo_original = caminho_arquivo_criptografado.replace(".enc", ".dec")

        with open(caminho_arquivo_original, "wb") as arquivo_original:
            arquivo_original.write(dados_original)

        print("Arquivo decriptado com sucesso!")
    except ValueError:
        print(f'Erro ao descriptografar!')

# Função para calcular o hash de um arquivo usando SHA-256
def calcular_hash(caminho_arquivo):
    sha256 = hashlib.sha256()
    with open(caminho_arquivo, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

# Função para verificar a integridade dos arquivos
def verificar_integridade(arquivo_original, arquivo_decriptado):
    hash_original = calcular_hash(arquivo_original)
    hash_decriptado = calcular_hash(arquivo_decriptado)

    print(f"Hash do arquivo original: {hash_original}")
    print(f"Hash do arquivo decriptado: {hash_decriptado}")

    if hash_original == hash_decriptado:
        print("Integridade mantida: os arquivos são idênticos!")
    else:
        print("Alteração detectada: os arquivos são diferentes.")