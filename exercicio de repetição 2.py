# 34 faça um numero que le um valor N inteiro e positivo e que calcula e escrevwe o fatorial de N

# minha
numero = int(input("Digite um numero para o calculo de seu fatorial: "))
contador = numero
fatorial = 1

if numero < 0:
    print(" inválido")
else:



# resolução do brother
n = int(input("Digite um numero para calcular seu fatorial: "))
cont = n
f = 1
while cont > 0:
    print(f"{cont}", end=" ")
    print("x " if cont > 1 else "= ", end=" ")
    f = cont * f
    cont = cont - 1
print(f)


# do marco
n = int(input("Digite um número inteiro e positivo: "))
if n < 0:
    print("Número inválido para cálculo de fatorial")
else:
    fatorial = 1
    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    print(f"O fatorial = {fatorial}")
