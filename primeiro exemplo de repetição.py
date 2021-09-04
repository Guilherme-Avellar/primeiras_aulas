
total = int(input("Digite o número de alunos: "))
soma = 0
contador = 0

while contador < total:
    nota = float(input(f"Digite a nota do aluno {contador + 1:.2f}: "))
    soma = soma + nota
    contador = contador + 1

print(soma / contador)