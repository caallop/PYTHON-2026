num = int(input("Insira um número: "))
fat = 1
i = 1


while i <= num:
    fat *= i
    i += 1
    print(f"a soma sera: {fat}")
