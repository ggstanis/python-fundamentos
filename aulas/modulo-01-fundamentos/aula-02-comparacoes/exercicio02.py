"""
Módulo 1 - Fundamentos
Aula 2.1 - Operadores Lógicos
Exercício 02
Autor: Gabriel Estanislau
Data: 12/07/2026
"""

idade = 18
maior = idade >= 18 and idade <= 30
print(maior)

nome = "Gabriel"
resultado = nome == "Gabriel Estanislau" or nome == "Gabriel"
print(resultado)

menor_de_idade = not (idade >= 18)

print(menor_de_idade)