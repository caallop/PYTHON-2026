import pandas as pd

df = pd.DataFrame({
    "pedido":    [1001, 1002, 1003, 1004, 1005, 1006],
    "produto":   ["Notebook", "Mouse", "Monitor",
                  "Teclado", "Notebook", "Webcam"],
    "categoria": ["Informatica", "Acessorio",
                  "Informatica", "Acessorio",
                  "Informatica", "Acessorio"],
    "regiao":    ["SP", "RJ", "SP", "MG", "RJ", "SP"],
    "preco":     [4200.0, 89.9, 1350.0,
                  210.0, 3990.0, 149.9],
    "qtd":       [2, 10, 3, 5, 1, 4],
})

#Ex.1
def soma_ate(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

#Ex.2
def soma_ate_n(n):
    return n * (n + 1) // 2

# Ex.3

import pandas as pd

df = pd.DataFrame({
    "pedido":    [1001, 1002, 1003, 1004, 1005, 1006],
    "produto":   ["Notebook", "Mouse", "Monitor",
                  "Teclado", "Notebook", "Webcam"],
    "categoria": ["Informatica", "Acessorio",
                  "Informatica", "Acessorio",
                  "Informatica", "Acessorio"],
    "regiao":    ["SP", "RJ", "SP", "MG", "RJ", "SP"],
    "preco":     [4200.0, 89.9, 1350.0,
                  210.0, 3990.0, 149.9],
    "qtd":       [2, 10, 3, 5, 1, 4],
})

#df.to_excel('dados_excel.xlsx')
#df.to_csv('dados_excel.csv')

total = []
for i in range(len(df)):
    total.append(float(df['preco'][i] * df['qtd'][i]))
print(total)

#Inserir valores em uma nova coluna
df['Total'] = total

# Ex.4
df['Total'] = df['preco'] * df['qtd']

# Ex.5

import matplotlib.pyplot as plt

x = df['pedido']
y = df['preco']

plt.plot(x, y)
plt.show()

#Ex.6 - Como criar uma estrutura de condição para
trazer apenas valores
de total > 1000? Utilize estrutura de repetição e condição.

filtro_total = []

for i in range(len(df)):
    if df['Total'][i] > 1000:
        filtro_total.append(df['Total'][i])

# Ex.7
filtro = df['Total'] > 1000
acima = df[filtro]
print(acima)

# Ex.8
df_filtro1 = df[(df['Total'] > 1000) & (df['regiao'] == 'SP')]
df_filtro2 = df[df['preco'].between(100, 500)]
df_filtro3 = df[df['regiao'].isin(['SP', 'RJ'])]

df_filtro4 = df[(df['regiao'] == 'RJ') | (df['qtd'] >= 5)]

############################################################

dados = pd.read_csv('C:/Users/labsfiap/Downloads/manutencao_preditiva.csv')


Exercícios
1. Faça um filtro para retornar apenas máquinas do tipo L, depois
H, depois M.

dados_L =  dados[dados['Tipo'] == 'L']
dados_M = dados[dados['Tipo'] == 'M']
dados_H =  dados[dados['Tipo'] == 'H']

2. Verifique quantos registros há para cada tipo de máquina.

dados['Tipo'].value_counts()

3. Verique quantos registros existem para cada tipo de falha.

dados['Tipo da Falha'].value_counts()

4. Faça um filtro para mostrar apenas as informações da falha do
tipo power failure.

df_PF = dados[dados['Tipo da Falha'] == 'Power Failure']

5. Verifique quantos registros há de cada tipo de máquina quando
houver apenas o tipo de falha power failure.

df_PF['Tipo'].value_counts()

6. Plote a curva de temperatura do processo, depois a velocidade
de rotação, depois o torque levando em conta o exercício 5.

import matplotlib.pyplot as plt

x = dados['UDI']
y1 = dados['Temperatura Processo [K]']
y2 = dados['Velocidade Rotacao [rpm]']
y3 = dados['Torque [Nm]']

plt.plot(x, y3)
plt.show()

7. Será que é correto plotar os gráficos do exercício anterior?
Porque sim ou não?

dados1 = dados[(dados['Tipo da Falha'] == 'Power Failure') & (dados['Tipo'] == 'M')]



8. Plote os gráficos do exercício anterior da forma correta.














