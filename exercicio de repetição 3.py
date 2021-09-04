# 35 A prefeitura de uma cidade fez um ap esquisa entre seus habitantes,
# coletando dados sobre o salário e número de filhos.
# A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário;
# d) percentual de pessoas com salário até R$100,00;
# O final da leitura de dados se dará com a entrada de um salário negativo.


soma_salario = 0
soma_filhos = 0
qtde_pessoas = 0
qtde_pessoas_100 = 0
salario = float(input("Digite o salário: "))
maior_salario = salario
while salario >= 0:
    filhos = int(input("Digite o número de filhos: "))
    soma_salario = soma_salario + salario
    soma_filhos = soma_filhos + filhos
    qtde_pessoas = qtde_pessoas + 1
    if salario > maior_salario:
        maior_salario = salario
    if salario <= 100:
        qtde_pessoas_100 = qtde_pessoas_100 + 1

    salario = float(input("Digite o salário: "))

if qtde_pessoas > 0:
    print(f"Média dos salários = {soma_salario / qtde_pessoas:.2f}")
    print(f"Média do número de filhos = {soma_filhos / qtde_pessoas}")
    print(f"Maior salário = {maior_salario:.2f}")
    print(f"Percentual de pessoas até R$ 100,00: {qtde_pessoas_100 * 100 /qtde_pessoas:.2f}%")
