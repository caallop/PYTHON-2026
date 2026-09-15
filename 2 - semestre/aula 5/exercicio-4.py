import pandas as pd

dados = pd.read_csv(r'C:\Users\labsfiap\Desktop\PYTHON-2026\2 - semestre\aula 5\manutencao_preditiva.csv')
print(dados)

df_PF = dados[dados['Tipo de Falha'] == 'Power Failure']