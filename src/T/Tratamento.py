import os
import pandas as pd
import re
from io import StringIO
from util.caputura_tabela import trat_tabelas_texto

def trat_excel(texto, num_pag, output):
    tabelas = trat_tabelas_texto(texto)
    if len(tabelas)>0:
        #ler a tabela
        for i, t in enumerate(tabelas):
            tabela = pd.read_csv(StringIO(t), sep='|', encoding='cp1252', engine='python')
            tabela = tabela.dropna(how='all', axis=1) # exclui linhas vazias
            tabela = tabela.dropna(how='all', axis=0) # exclui colunas vazias
            #salva a tabela
            tabela.to_excel(f'{output}/pagina_{num_pag}_tabela_{i+1}.xlsx', index=False)
