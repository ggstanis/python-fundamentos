"""
Módulo 1 - Fundamentos
Aula 2.5 - Estrutura Condicional if/elif/else
Exercício 05
Autor: Gabriel Estanislau
Data: 21/07/2026
"""

# Entrada de dados
nome_aluno = input("Digite o nome do Aluno: ")
nota_aluno = input(f"Digite a nota de {nome_aluno} (0 a 100): ")

# Processamento
if nota_aluno >= 90:
    situacao_aluno = "Excelente"
elif nota_aluno >= 70:
    situacao_aluno = "Aprovado"
elif nota_aluno >= 50:
    situacao_aluno = "Recuperação"
else:
    situacao_aluno = "Reprovado"

# Saída de dados
print(
     "Nome do aluno:", nome_aluno,
     "Nota:", nota_aluno,
     sep=" | "
    )

print(
     "Situação:", situacao_aluno
    )

print(
     "Programa encerrado"
    )