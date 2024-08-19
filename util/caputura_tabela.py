import re
def trat_tabelas_texto(texto):
    regex_tabelas = re.compile(r'((?:\|.+\|(?:\n|\r))+)', re.MULTILINE)
    tabelas = regex_tabelas.findall(texto)
    return tabelas