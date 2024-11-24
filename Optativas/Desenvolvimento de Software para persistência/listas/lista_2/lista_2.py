# -*- coding: utf-8 -*-
# Objetivo: Criar um programa que leia e processe arquivos de texto,
# escreva os resultados em um novo arquivo e compacte o arquivo de saída em um ZIP.
import os
from zipfile import ZipFile

# O código lê todos os arquivos .txt da pasta textos.
arquivos_validos = []
arquivos_zip = []
diretorio = "/content/sample_data/textos"

try:
  conteudos_diretorio = os.listdir(diretorio)

  if not conteudos_diretorio:
    print(f"O diretório {diretorio} está vazio.")

  else:
    for conteudo_diretorio in conteudos_diretorio:
        if conteudo_diretorio.endswith(".txt") | conteudo_diretorio.endswith(".zip"):
            arquivos_validos.append(conteudo_diretorio)

        if conteudo_diretorio.endswith(".zip"):
            arquivos_zip.append(conteudo_diretorio)

  if not arquivos_validos:
    print(f"Nenhum arquivo válido para processamento foi encontrado no diretório {diretorio}")
    execucao_bem_sucedida = False

  if not arquivos_zip:
    print(f"Nenhum arquivo zip foi encontrado no diretório {diretorio}")

except FileNotFoundError:
    print(f"O diretório '{diretorio}' não foi encontrado.")
    execucao_bem_sucedida = False

except PermissionError:
    print(f"Permissão negada para acessar o diretório '{diretorio}'.")
    execucao_bem_sucedida = False

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    execucao_bem_sucedida = False

# Exibe os arquivos válidos e .zip encontrados
if arquivos_validos:
    print("Arquivos válidos para processamento encontrados:", arquivos_validos)
if arquivos_zip:
    print("Arquivos válidos para processamento encontrados:", arquivos_zip)

if 'execucao_bem_sucedida' in locals() and execucao_bem_sucedida:
  estatistica_arquivos = []
  for arquivo in range(len(arquivos_validos)):
    # Junta o caminho do diretório ao nome do arquivo
    caminho_arquivo = os.path.join(diretorio, arquivos_validos[arquivo])

    # Abre o arquivo
    with open(caminho_arquivo, 'r') as arquivo:
      # Ler todas as linhas do arquivo
      linhas_arquivo = arquivo.readlines()

      # Inicialização dos contadores
      total_palavras, total_caracteres = 0, 0
      # Exibe somente as linhas não vazias
      for linha_arquivo in linhas_arquivo:
        if linha_arquivo.strip():
          # Calcula o total de caracteres
          total_caracteres += len(linha_arquivo.strip())
          # Calcula o total de palavras
          palavras = linha_arquivo.strip()
          total_palavras += len(palavras.split())
      # Armazenamento das estatísticas dos arquivos
      estatistica_arquivos.append(f"{os.path.basename(caminho_arquivo)}: {total_palavras} palavras e {total_caracteres} caracteres.")
else:
  print("Não é possível realizar o processamento no momento")

# Escreve o nome do arquivo e as estatísticas no arquivo consolidado.txt.
if 'execucao_bem_sucedida' in locals() and execucao_bem_sucedida:
  with open("consolidado.txt", "w") as relatorio:
    for dados in range(len(estatistica_arquivos)):
      relatorio.write(estatistica_arquivos[dados] + "\n")
else:
  print("Não é possível realizar o processamento no momento")

# Etapa 3: Compactar em um arquivo ZIP
if 'execucao_bem_sucedida' in locals() and execucao_bem_sucedida:
  with ZipFile("saida.zip", "w") as arquivo_zipado:
      arquivo_zipado.write("consolidado.txt")
else:
  print("Não é possível realizar o processamento no momento")