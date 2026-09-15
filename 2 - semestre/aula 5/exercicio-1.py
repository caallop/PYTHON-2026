import pandas as pd

dados = pd.read_csv(r'C:\Users\labsfiap\Desktop\PYTHON-2026\2 - semestre\aula 5\manutencao_preditiva.csv')
print(dados)

filtroL = dados[dados['Tipo'] == 'L']
filtroH = dados[dados['Tipo'] == 'H']
filtroM = dados[dados['Tipo'] == 'M']


print (filtroL)
print (filtroM)
print (filtroH)