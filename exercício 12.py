# Faça um algoritmo para verificar e imprimir entre 4 números lidos qual é o menor.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número : "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número  : "))

if num1 < num2 and num1 < num3 and num1 < num4:
    menor = num1
else:
    if num2 < num3 and num2 < num4:
        menor = num2
    else:
        if num3 < num4:
            menor = num3
        else:
            menor = num4

print(f"O menor número é: {menor}")
