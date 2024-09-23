"""
Informe o número da turma: 
Turma - G93313

Nome completo dos componentes.
1 - Gustavo Batista
2 - João Gabriel
"""

import os

# Limpa o terminal.
os.system("cls || clear") 

print("""
1 - Picanha
2 - Lasanha
3 - Strogonoff
4 - Bife acebolado
5 - Pão com ovo
6 - Frango à parmegiana
7 - Filé de porco
           """)

opcao = int(input("Digite o número do prato desejado: "))

match(opcao):
    case 1:
        resultado = "Picanha - R$ 25,00"
    case 2:
        resultado = "Lasanha - R$ 20,00"
    case 3:
        resultado = "Strogonoff - R$ 18,00"
    case 4:
        resultado = "Bife acebolado - R$ 15,00"
    case 5:
        resultado = "Pão com ovo - R$ 5,00"
    case 6:
        resultado = "Frango à parmegiana - R$ 30,00"
    case 7:
        resultado = "Filé de porco - R$ 27,00"
    case _:
        print("Opção inválida. Digite novamente: ")

print(f"{resultado}")





