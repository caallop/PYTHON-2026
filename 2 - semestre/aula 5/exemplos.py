#ex 1
def soma_ate(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(soma_ate(10))

#ex 2
def soma_ate2(b):
    return b * (b + 1) // 2

print(soma_ate2(10))


#EX3

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
    total.append(float(df['preco'][i] * df["qtd"][i]))
print(total)


df['Total'] = total

print(total)
df.to_csv('dados_excel.csv')


#ex 5
import matplotlib.pyplot as plt

x = df['pedido']
y = df['preco']

plt.bar(x,y)
plt.show()