#declaração de variaveis
kilometros = float(input("qual a distancia que deseja saber(km)? "))

#calculos
metros = kilometros*1000
cm = kilometros*100000

#saidas
print(f"os ", kilometros, "em metro ficaram: ",metros, )
print(f"os ", kilometros, "em centimetros ficaram: ",cm, )