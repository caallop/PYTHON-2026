#crie uma estrutura para oslicitar o tipo de figura geometica, apos isso, mostre como calcular a area e o perimetro de cada figura geometrica


def area_triangulo(base, altura):
   area = (base * altura)/2
   return area

def area_retangulo(base, altura):
    area = (base * altura)/2
    return area

def area_quadrado(base, altura):
    area = (base * altura)/2
    return area

def area_circulo(r):
     area = 3.14*r**2
     return area
##############################
def perimetro_triangulo(comprimento, largura):
    perimetro = (comprimento + largura) * 2
    return perimetro

def perimetro_retangulo(lado1, lado2, lado3):
    perimetro = (lado1 + lado2 + lado3)
    return perimetro

def perimetro_quadrado(comprimento):
    perimetro = (comprimento) * 4
    return perimetro

def perimetro_circulo(raio):
    perimetro = 2 * 3.14 * raio
    return perimetro

opcao = input("quer calcular a area(1) ou o perimetro(2)?  ")

match opcao:

    case "1":
        opcao = input("qual forma geometrica quer calcular a area: (triangulo, quadrado, retangulo e circulo) ")

        match opcao:
           case "triangulo":
             area = area_triangulo(int(input("qual a base da figura? ")), int(input("qual a altura da figura? ")))
             print(area)
           case "quadrado":
              area = area_quadrado(int(input("qual a base da figura? ")), int(input("qual a altura da figura? ")))
              print(area)
           case "retangulo":
              area = area_retangulo(int(input("qual a base da figura? ")), int(input("qual a altura da figura? ")))
              print(area)
           case "circulo": 
              area = area_circulo(int(input("qual o raio do circulo? ")))
              print(area)
           case _:
              print("entrada invalida")
    case "2":
        opcao = input("qual forma geometrica quer calcular o perimetro: (triangulo, quadrado, retangulo e circulo) ")
        match opcao:
           case "triangulo":
             area = perimetro_triangulo(int(input("qual o comprimento da figura? ")), int(input("qual a altura da figura? ")))
             print(area)
           case "quadrado":
              area = perimetro_quadrado( int(input("qual é o tamanho do lado do quadrado? ")))
              print(area)
           case "retangulo":
              area = perimetro_retangulo(int(input("qual o comprimento da figura? ")), int(input("qual a largura da figura? ")))
              print(area)
           case "circulo": 
              area = perimetro_circulo(int(input("qual o raio do circulo? ")))
              print(area)
           case _:
              print("entrada invalida")
      
    case _:
              print("entrada invalida")