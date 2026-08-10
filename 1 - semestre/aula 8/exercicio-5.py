import pandas as pd

dados = {
    "nome": ["joao", "pedro", "lucas"],
    "idade": [20,30,40],
    "salario": [2000, 4000, 6000]
}

df = pd.DataFrame(dados)


#ex 1 
def mosttrar_dataframe():
    print(df["nome"])
    print(df["idade"])
    print(df["salario"])

mosttrar_dataframe()

#ex 2

def mostrar_linhas_specificas():
    print(df.head())

mostrar_linhas_specificas()

#ex 3 

def mostrar_inf():
    print(df.info())

#ex 4

def media_idade():
    print("a media das idades é:", df["idade"].mean())

media_idade()

#ex 5

def min_max_mean_salarial():
    print(df["salario"].min())
    print(df["salario"].max())
    print(df["salario"].max())
min_max_mean_salarial()

#ex 6

def filtro_idade():
    print(df["idade"]>30)
filtro_idade()

#ex 7
def adicionar_bonus():
    df["Bonus"] = df ["salario"]*1.1

adicionar_bonus()

#ex 8

def ordenar_salario():
    print(df.sort_values("salario", ascending=False))

ordenar_salario

#ex 9

def contar_registro():
    print(f"Quantidade de registros",len(df))

contar_registro()

#ex 10 

def estatistica():
    print(df.describe())

estatistica()


#ex 11

def registros_nao_numericos ():
    print(df["nome"].values)

registros_nao_numericos