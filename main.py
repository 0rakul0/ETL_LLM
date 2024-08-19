# -*- coding: utf-8 -*-
import os
import time

from src.E.exctrat import extrai
from src.T.Tratamento import trat_excel

def main():
    fonte = r'D:/github/ETL_LLM/lake'

    os.makedirs(r'D:/github/ETL_LLM/data/input', exist_ok=True) # onde serão salvos os arquivos convertidos de pdf para md
    os.makedirs(r'D:/github/ETL_LLM/data/output', exist_ok=True) # onde serão salvos os arquivos convertidos de md para excel

    pasta_arquivos = r'D:/github/ETL_LLM/data/input'
    output = r'D:/github/ETL_LLM/data/output'

    extrai(fonte, pasta_arquivos)
    time.sleep(1)
    lista_input = os.listdir(pasta_arquivos)

    for i, l in enumerate(lista_input):
        with open(f'{pasta_arquivos}/{l}', 'r', encoding='cp1252') as arq:
            texto = arq.read()
        trat_excel(texto, i+1, output)

if __name__ == '__main__':
    main()

