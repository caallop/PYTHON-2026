import pandas as pd

dados = pd.read_csv(r'C:\Users\labsfiap\Desktop\PYTHON-2026\2 - semestre\aula 6\dados_meteorologicos.csv')

for i in dados['temperatura']:
    mediana = dados['temperatura'].median()
    if i > mediana:
        print("maior")
    elif i < mediana:
        print("menor")
    else:
        print("igual")
