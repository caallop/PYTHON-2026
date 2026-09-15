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

total = []
for i in range(len(df)):
    total.append(float(df['preco'][i] * df["qtd"][i]))


df['Total'] = total
#VERSÃO 1, FORMA 'SEM PANDAS'
df.to_csv('dados_excel.csv')
for i in range(len(df)):
    if df['Total'][i] > 1000:
     print(df['Total'][i])
     
#EX 9 
filtro = df['Total'] > 1000
acima = df['filtro']
print(acima)



df_filtro1 = df[(df['regiao'] == 'RJ') | (df["qtd"] >=5)]
df_filtro2 = df[(df['regiao'] == 'RJ') | (df["qtd"] >=5)]
df_filtro3 = df[df['regiao']]
df_filtro4 = df[(df['regiao'] == 'RJ') | (df["qtd"] >=5)]