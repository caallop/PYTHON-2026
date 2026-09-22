import pandas as pd

# Carregando os dados
dados = pd.read_csv(r'C:\Users\labsfiap\Desktop\PYTHON-2026\2 - semestre\aula 6\dados_meteorologicos.csv')

# Definindo as colunas e o dicionário de funções
colunas = ["temperatura", "sensacao_termica", "umidade", "chuva_mm"]

funcoes = {
    'min': lambda x: x.min(),
    'max': lambda x: x.max(),
    'mean': lambda x: x.mean(),
    'median': lambda x: x.median(),
} 

# Loop aninhado: para cada coluna, calcula todas as métricas do dicionário
for coluna in colunas:
    print(f'--- Coluna: {coluna} ---')
    
    for nome_funcao, funcao in funcoes.items():
        # Aplica a função lambda na coluna específica do DataFrame
        resultado = funcao(dados[coluna])
        print(f'{nome_funcao}: {resultado}')
    
    print() # Linha em branco para separar as colunas