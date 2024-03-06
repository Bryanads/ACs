def e_triangulo(a,b,c):
    if a+b > c and a+c>b and c+b>a:
        return True
    return False
def determina_tipo_triangulo(a,b,c):
    triangulo = "Não é triangulo"
    if e_triangulo(a,b,c):
        if a == b and b==c and a==c:
            triangulo = "Equilatero"
            return triangulo
        elif a!=b and b!=c and a!=c:
            triangulo = "Escaleno"
            return triangulo
        else:
            triangulo = "Isoceles"
            return triangulo
    else:
        return triangulo
def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

def dia_semana(a):
    match a:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terçca"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sábado"
        case _:
            return "String Vazia"
def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
def divisao (a,b):
    return a/b
def interface():
    a = float(input("Informe um numero: "))
    b = float(input("Informe outro numero: "))
    c = input("Informe a operação: ")

    if c == "soma":
        print("Resultado: ",soma(a,b))
    elif c == "subtracao":
        print("Resultado: ",subtracao(a,b))
    elif c == "multiplicacao":
        print("Resultado: ",multiplicacao(a,b))
    elif c == "divisao":
        print("Resultado: ",divisao(a,b))
    else:
        print("Operação Inválida")

def main():
    print("Exercicio 1:\n")
    testa_triangulo()
    print("-"*30)
    print("Exercicio 2:\n")
    testa_dia_semana()
    print("-"*30)
    print("Exercicio 3:\n")
    interface()
    print("-"*30)

main()
