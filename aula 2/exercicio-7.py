print("o que deseja para comer? ")
print("1. egg ")
print("2. pancakes")
print("3. wafles ")
print("4.frutas ")

resposta = int(input(""))

if resposta == 1:
    escolhas = str(input("deseja acompanhamento para seus eggs? (sim/nao) "))
    if escolhas == "sim":
        print("1. bacon ")
        print("2. linguiça ")
        print("3. queijos ")
        print("4. paes tostados ")
        acompanhamento = str(input(""))
        if acompanhamento == "1":
         print(f"seu pedido é: \n ovos com bacon!! ")
        elif acompanhamento == "2":
         print(f"seu pedido é: \n ovos com linguiça!!")
        elif acompanhamento == "3":
         print(f"seu pedido é: \n ovos com queijos!!")
        else:
            print(f"seu pedido é: \n ovos com paes tostados!!")
    else:
        print(f"seu pedido é: \n ovos!!")
elif resposta == 2:
     print(f"seu pedido é: \n pancakes!!")
elif resposta == 3:
     print(f"seu pedido é: \n wafles!!")
else:
    escolhas = str(input("deseja acompanhamento para suas frutas? (sim/nao) "))
    if escolhas == "sim":
        print("1. iogurte  ")
        print("2. queijos  ")
        print("3. castanhas ")
        print("4. mel ")
        acompanhamento = str(input(""))
        if acompanhamento == "1":
         print(f"seu pedido é: \n frutas com iogurte!! ")
        elif acompanhamento == "2":
         print(f"seu pedido é: \n frutas com queijos!!")
        elif acompanhamento == "3":
         print(f"seu pedido é: \n frutas com castanhas!!")
        else:
            print(f"seu pedido é: \n ovfrutasos com mel!!")
    else: 
        print(f"seu pedido é: \n frutas!!")