# -*- coding: utf-8 -*-
"""Lista 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MK5fWE5XhsOXuDCTBH2XEUvBzRat0r7P
"""

!pip install beautifulsoup4
!pip install pytesseract
!apt install tesseract-ocr
!pip install PyPDF2

# Importação da bibliotecas necessárias.
from bs4 import BeautifulSoup
import requests
import pytesseract
from PyPDF2 import PdfReader
from PIL import Image

# 1. Scraping de Websites com BeautifulSoup
# Objetivo: Praticar a extração de dados de um site usando scraping.
# Tarefa: Usando a biblioteca BeautifulSoup, escreva um código que extraia e imprima o título
# e todos os links de uma página web. A URL pode ser qualquer página pública, como https://example.com.
resposta = requests.get("https://www.ufc.br")
corpo_site = BeautifulSoup(resposta.content, "html.parser")

titulo_site = corpo_site.title.string

print("O título do site é: ", titulo_site)

links = corpo_site.find_all("a")
links_tratado = []

for link in links:
    href = link.get("href")
    if href and href != '#' and href != '/':
        if href.startswith('#'):
          links_tratado.append("https://www.ufc.br/" + href)

        elif href.startswith('/'):
          links_tratado.append("https://www.ufc.br" + href)

        else:
          links_tratado.append(href)

for link_tratado in links_tratado:
  print(link_tratado)

# Pega um imagem e PDF qualquer pra baixar
!wget -O extrair_texto_imagem.jpg https://images.wondershare.com/pdfelement/ocr/ocr-test-image-04.jpg
!wget -O extrair_texto_pdf.pdf https://pdfobject.com/pdf/sample.pdf

# 2. Extração de Texto de Imagens com OCR
# Usando pytesseract e PIL, escreva um código para carregar uma imagem,
# extrair o texto nela contido e salvar o resultado num arquivo txt..
imagem = Image.open("/content/extrair_texto_imagem.jpg")
texto = pytesseract.image_to_string(imagem)

with open("texto_extraido.txt", 'w') as resultado:
  resultado.write(texto)

import os

def extrair_html(url):
  resposta = requests.get(url)
  corpo_site = BeautifulSoup(resposta.content, "html.parser")

  print("Tipo: HTML, conteúdo: \n")
  titulo_site = corpo_site.title.string

  print("O título do site é: ", titulo_site)

  links = corpo_site.find_all("a")
  links_tratado = []

  for link in links:
      href = link.get("href")
      if href and href != '#' and href != '/':
          if href.startswith('#'):
            links_tratado.append(url + "/" + href)

          elif href.startswith('/'):
            links_tratado.append(url + href)

          else:
            links_tratado.append(href)

  for link_tratado in links_tratado:
    print(link_tratado)

def extrair_pdf(caminho_pdf):
  if not os.path.exists(caminho_pdf):
      print("Arquivo não encontrado, verifique o caminho e tente novamente.")
      return

  print("Tipo: Arquivo, conteúdo:")

  arquivo_pdf = PdfReader(caminho_pdf)
  for paginas in arquivo_pdf.pages:
      print(paginas.extract_text())

def extrair_imagem(caminho_imagem):
    if not os.path.exists(caminho_imagem):
      print("Arquivo não encontrado, verifique o caminho e tente novamente.")
      return

    imagem = Image.open(caminho_imagem)
    texto = pytesseract.image_to_string(imagem)
    print("Tipo: Imagem, conteúdo: " + texto)

def validacao(entrada):
  if entrada.lower().startswith("https://") or entrada.lower().startswith("http://"):
    extrair_html(entrada)

  elif entrada.lower().endswith(".jpg") or entrada.lower().endswith(".jpeg") or entrada.lower().endswith(".png"):
      extrair_imagem(entrada)

  elif entrada.lower().endswith(".pdf"):
      extrair_pdf(entrada)

  else:
    raise ValueError("Formato não suportado. Forneça uma URL, um PDF ou uma imagem.")

entrada = input("Digite a URL ou o caminho do arquuvo a ser analisado: ")

validacao(entrada)