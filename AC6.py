#Hello World!
print("Hello World!")

#Extremamente Básico
a = int(input())
b = int(input())

x = a + b
print("X =", x)

#Cálculo Simples
dados1 = input().split(" ")
num_1 = int(dados1[-2])
valor_1 = float(dados1[-1])


dados2 = input().split(" ")
num_2 = int(dados2[-2])
valor_2 = float(dados2[-1])

total = (num_1*valor_1)+(num_2*valor_2)
round(total,2)

print(f"VALOR A PAGAR: R$ {total:.2f}")

#O Maior
def maior (a,b):

    maior = (a+b+abs(a-b))/2
    maior = int(maior)
    return maior
a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

if maior(a,b) == a:
    print(maior(a,c))
else:
    print(maior(b,c))

#Distância Entre Dois Pontos
def calcula(x1,x2,y1,y2):
    calc = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return calc

x1,y1= input().split()
x2, y2 = input().split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

print(f"{calcula(x1,x2,y1,y2):.4f}")
