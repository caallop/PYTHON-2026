number = int(input("qual é seu numero? "))

if number > 0:
    if number % 2 == 0:
        print("seu numero é positivo e par")
    else:
        print("seu numero é positivo e impar")
elif number == 0:
    print("seu numero é zero")
else:
    print("seu numero é negativo")
    
