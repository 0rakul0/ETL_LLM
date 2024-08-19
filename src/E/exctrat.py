import os

from llama_parse import LlamaParse
from dotenv import load_dotenv

load_dotenv()
def extrai(caminho, destino):
    lista_arquivos = os.listdir(caminho)
    for arquivo in lista_arquivos:
        arq_pdf = f'{caminho}/{arquivo}'
        docs = LlamaParse(result_type="markdown",
                      parsing_instruction="this file contains text and tables, I'd like to get only the tables from file").load_data(arq_pdf)

    for i, doc in enumerate(docs):
        with open(fr"{destino}/arquivo_{i+1}.md", "w", encoding='cp1252', errors='replace') as arq:
            arq.write(doc.text)