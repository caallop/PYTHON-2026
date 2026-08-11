def fatorial(n,memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    if n == 0:
        return 1

    memo[n] = n * fatorial(n-1, memo)
    return memo[n]

resultado = fatorial(1)
print(resultado)


#--------------------------------------------------------------------------------

time = {'A''B''C'}
vitoria = {'10''9''6'}
estado = {'SP''SP''RJ'}


#ESTRUTURA COM DICIONARIO
dic = {
    'time': ['A''B''C'],
    'vitoria': ['10''9''6'],
    'estado': ['SP''SP''RJ']
}

#ESTRUTURA COM DICIONARIO
dic = {
    'time': ['A''B''C'],
    'vitoria': ['10''9''6'],
    'estado': ['SP''SP''RJ']
}

#ESTRUTURA COM BIBLIOTECAS
import pandas as pd

dic = {
    'time': ['A''B''C'],
    'vitoria': ['10''9''6'],
    'estado': ['SP''SP''RJ']
}
dic.pop('time')
print(dic)
dataframe = pd.DataFrame(dic)
print (dataframe)