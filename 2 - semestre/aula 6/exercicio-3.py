import pandas as pd
import matplotlib.pyplot as plt


dados = pd.read_csv(r'C:\Users\labsfiap\Desktop\PYTHON-2026\2 - semestre\aula 6\dados_meteorologicos.csv')

# Garante que a coluna de tempo seja o índice (funciona tanto para 'data_hora' quanto para 'time')
x = dados['data_hora']
y1 = dados['temperatura']
y2 = dados['sensacao_termica']
y3 = dados['pressao']

plt.plot(x, y1, x, y2, x, y3)
plt.xlabel("Data")
plt.ylabel("Temperatura e Sensação Térmica e Pressão")
plt.legend(['Temperatura', 'Sensação Térmica', 'Pressão'])
plt.grid(True)
plt.show()