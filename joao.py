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
escreva o código do prato para fazer o pedido:
cÓdigo = Menu                |Valor |
1      = Picanha             |25,00 |
2      = lasanha             |20,00 |
3      = Strogonoff          |18,00 |
4      = Bife acebolado      |15,00 |
5      = Pão com ovo         |5,00  |  
6      = Frango à parmegiana |30,00 |
7      = Filé de porco       |27,00 |  
      """)

Codigo_Prato =(input("Digite o Código do seu Prato: "))

resultado = 0

match(Codigo_Prato):
    case "1":
        print("Picanha R$ 25,00")
    case "2":
        print("Lasanhha R$20,00")
    case "3":
        print("Strogonoff R$18,00")
    case "4":
        print("Bife acebolado R$15,00")
    case "5":
        print("Pão com ovo R$5,00")
    case "6":
        print("Frango à parmegiana R$30,00")
    case "7":
        print("Filé de porco R$27,00")
    case "0":
        print("Opção invalida, Por favor digite um Código Valido.")

        


print("=== FIM ===")  

