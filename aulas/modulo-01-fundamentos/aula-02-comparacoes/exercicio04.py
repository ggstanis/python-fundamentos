"""
Módulo 1 - Fundamentos
Aula 2.4 - Estrutura Condicional if/else
Exercício 04
Autor: Gabriel Estanislau
Data: 14/07/2026
"""

# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
possui_convite = input("Você possui o convite? (s/n): ").lower()

# Processamento
maior_idade = 18
entrada_autorizada = (idade >= maior_idade and possui_convite == "s")

 # Saída de dados
print(
     "Nome:", nome,
     "Idade:", idade,
    "Convite:", possui_convite,
     sep=" | "
    )

if entrada_autorizada:
    print(
        "Entrada autorizada"
        )
else:
    print(
        "Entrada negada"
        )

# Saída de dados de encerramento do programa
print("Programa encerrado")