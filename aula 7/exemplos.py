import pandas as pd

dados = {
    'produto': ['notebook', 'mouse', 'teclado', 'monitor', 'webcam'],
    'vendas': [1200, 300, 500, 600, None],
    'lucro': [300, 50, 80, 200, 40],
    'ano': ['2022', '2020', '1947', '2001', '1']
}
print (dados)

dataframe = pd.DataFrame(dados) #mostra em tabela

#calculo da media
media = dataframe['vendas'].mean()
print(media)

try:
    media = dataframe['vendas'].mean()
    print(f"A media de lucro é: {media}")
except KeyError:
    print("essa coluna nao existe")

print("================================")
print("================================")
print("================================")

try:
    dataframe['relacao_vendas_lucro'] = dataframe['lucro']/dataframe['vendas']
    print(dataframe['relacao_vendas_lucro'])
except ZeroDivisionError:
    print("não é possivel dividir por 0")
else:
    print("Margem calculada com sucesso")

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################

    #try/except

#%%
try:
    numero = int(input("Digite um numero "))
except ValueError:
    print("digite um numero, não uma letra")


##########################################
#%%
try:
    a = int(input("Digite um numero "))
    b = int(input("Digite um numero "))

    soma = a + b
    sub = a - b
    div = a/b
    print(soma)
    print(sub)
    print(div)

except ValueError: 
    print("Valor não númerico!!")

except ZeroDivisionError:
    print("Erro: divisão por 0!!!")



##########################################
#%%

def entrada_numero():
    try: 
        numero = int(input("Digite um numero ")) 
        print(numero)
    except ValueError:
        print("valor não numerico!!")

entrada_numero()
# %%
