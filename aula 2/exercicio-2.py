older = int(input("quantos anos voce tem?"))

if older>=18:
    if older < 60:
        print("voce é adulto")
    else:
        print ("voce é idoso")
else:
    if older >= 12:
     print("voce é adolecente")
    else:
     print("voce é criança")