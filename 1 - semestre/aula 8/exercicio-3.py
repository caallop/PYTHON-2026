#crie um algoritmo para solicitar a temperatura em celcius e transformar para fareihneit

def temp(c):
    fahreinht = (c * 9/5) + 32

    return fahreinht

a = temp(int(input('')))

print(a)