bill = int(input("quanto ficou sua conta? "))
vip = str(input("voce é vip? (s/n) "))

if bill >= 200:
    if vip == "sim":
        print("voce recebe um desconto de 20%")
        print(f"sera descontado {bill*0.2} da sua conta final")
        print(f"no total vai ficar {bill*0.8}")
    else:
        print("voce recebe um desconto de 10%")
        print(f"sera descontado {bill*0.1} da sua conta final")
        print(f"no total vai ficar {bill*0.9}")
else:
    print(f"sua conta ficou{bill}")