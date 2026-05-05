#Exercício 2: crie uma estrtura com try/except a qual cacule e traga uma erri oara calcular a area de um retangulo e circulo com estrutura input para o usuario. além dissso, o usuario deve escolher a figura geometica

try:
    opcao = int(input("Digite a forma que voce quer calcular: (1.circulo | 2.retangulo)\n "))
    if opcao == 1:
        raio = float(input("Digite o raio do circulo "))
        area_circulo = 3.14 * raio**2
        print(f"o raio do circulo é: {area_circulo}")
    elif opcao == 2:
        base = float(input("Digite a base do retangulo "))
        altura = float(input("Digite a altura do retangulo "))
        area_retangulo = base *altura
        print(f"a area do retangulo é: {area_retangulo}")

    else:
        print("\ndigite uma das opções")
    
except ValueError:
    print("ERRO: Digite um valor numerico.")
