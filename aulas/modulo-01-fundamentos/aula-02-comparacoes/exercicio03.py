"""
Módulo 1 - Fundamentos
Aula 2.3 - Estrutura Condicional if
Exercício 03
Autor: Gabriel Estanislau
Data: 13/07/2026
"""

idade = 15
maior_idade = 18

# Exemplo 1 - Verificação simples
if idade >= maior_idade:
    print("Você é maior de idade.")

if idade < maior_idade:
    print("Você é menor de idade.")

# Exemplo Exemplo 2 - if/else
idade = 18
if idade >= maior_idade:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exemplo 3 - Maior de idade + CNH    
idade = int(input("Digite sua idade: "))
nome = input("Digite seu nome: ")
possui_cnh = input("Você possui CNH? (s/n): ").lower()

print(
    "Pessoa:", nome,
    "Idade:", idade,
    "CNH:", possui_cnh,
    sep =" | "
    )

if idade >= maior_idade and possui_cnh == "s" :
    print(
        "É maior de idade",
        "Você pode dirigir.",
        sep =" | "
        )

print("Fim do programa.")