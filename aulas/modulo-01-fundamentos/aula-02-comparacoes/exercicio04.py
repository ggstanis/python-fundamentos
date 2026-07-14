"""
Módulo 1 - Fundamentos
Aula 2.4 - Estrutura Condicional if/else
Exercício 03
Autor: Gabriel Estanislau
Data: 14/07/2026
"""

# Entrada de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
possui_convite = input("Você possui o convite? (s/n): ").lower()
maior_idade = 18

# Verificação dos dados de entrada - saida de dados
print(
    "Nome:", nome,
    "Idade:", idade,
    "Convite:", possui_convite,
    sep =" | "
    )

# Processamento
if idade >= maior_idade and possui_convite == "s" :
    print(
        # Saída de dados
        "Entrada autorizada"
        )
else:
    print(
        # Saída de dados
        "Entrada negada"
        )

# Saída de dados de encerramento do programa
print("Programa encerrado")