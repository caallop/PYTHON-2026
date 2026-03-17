salario = float(input("quanto o senhor(ou senhora) ganha? "))

if salario <= 1621:
    print(f"com os descontos do inss, voce ganhara{salario}")
elif salario >= 1621.01 and salario <=2902.84:
    print(f"com os decontos do inss, voce ganha{salario-24.32}")
elif salario >= 2902.85 and salario <=4354.27:
    print(f"com os decontos do inss, voce ganha{salario-111.40}")
elif salario >= 4354.28 and salario <=8475.55:
    print(f"com os decontos do inss, voce ganha{salario-198.49}")