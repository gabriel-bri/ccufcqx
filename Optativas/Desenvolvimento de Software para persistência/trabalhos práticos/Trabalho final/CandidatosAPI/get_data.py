import os
import requests

def baixar_zips(urls):
    pasta = "resources"
    os.makedirs(pasta, exist_ok=True)
    
    for url in urls:
        nome_arquivo = os.path.join(pasta, url.split("/")[-1])
        print(f"Baixando {url}...")
        
        resposta = requests.get(url, stream=True)
        if resposta.status_code == 200:
            with open(nome_arquivo, "wb") as arquivo:
                for chunk in resposta.iter_content(chunk_size=1024):
                    arquivo.write(chunk)
            print(f"Arquivo salvo: {nome_arquivo}")
        else:
            print(f"Erro ao baixar {url}: Código {resposta.status_code}")

urls = [
    "https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2024.zip",
    "https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand_complementar/consulta_cand_complementar_2024.zip",
    "https://cdn.tse.jus.br/estatistica/sead/odsele/motivo_cassacao/motivo_cassacao_2024.zip",
    "https://cdn.tse.jus.br/estatistica/sead/odsele/bem_candidato/bem_candidato_2024.zip"

]
baixar_zips(urls)
