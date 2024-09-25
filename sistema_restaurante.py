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

valor_total = 0

print("=== CARDÁPIO ===")
print("""
1 - Picanha
2 - Lasanha
3 - Strogonoff
4 - Bife acebolado
5 - Pão com ovo
6 - Frango à parmegiana
7 - Filé de porco
           """)

def exibir_menu(codigo_prato):
    match(codigo_prato):
        case 1:
            return "1 - Picanha R$ 25,00",25
        case 2:
            return "2 - Lasanha R$ 20,00",20
        case 3:
            return "3 - Strogonoff R$ 18,00",18
        case 4:
            return "4 - Bife acebolado R$ 15,00",15
        case 5:
            return "5 - Pão com ovo R$ 5,00",5
        case 6:
            return "6 - Frango a Parmegiana R$ 30,00",30
        case 7:
            return "7 - Filé de Porco R$ 27,00",27
        case _:
            return None,0
        
pedido_cliente = []
total_pedido = 0

while True:
    codigo_prato = int(input("Digite o código do prato que deseja: "))
    prato, preco = exibir_menu(codigo_prato)
    if prato is None:
        print("Código inválido, digite o código novamente: ")
    else:
        print(f"Prato escolhido: {prato}")
        pedido_cliente.append(prato)
        total_pedido += preco

    adicionar = input("Deseja adicionar mais algum prato (sim/não)? ")
    if adicionar != 'sim':
        break

print("=== FORMA DE PAGAMENTO ===")

print("""
1 - À vista 
2 - Cartão de crédito
      """)

pagamento = int(input("Digite 1 para pagamento à vista ou 2 para cartão de crédito: "))

desconto = total_pedido * 0.10
acrescimo = total_pedido * 0.10

if pagamento == 1:
    desconto_ou_acrescimo = desconto
    valor_com_desconto_ou_acrescimo = total_pedido - desconto
    forma_de_pagamento = "À vista"
else:
    desconto_ou_acrescimo = acrescimo
    valor_com_desconto_ou_acrescimo = total_pedido + acrescimo
    forma_de_pagamento = "Cartão de crédito"

print("=== PEDIDO ===")
for item in pedido_cliente:
    print(f"{item}")
print(f"Valor sem acréscimo ou desconto: R$ {total_pedido:.2f}")
print(f"Forma de pagamento: {forma_de_pagamento}")
print(f"Valor do acréscimo ou desconto: R$ {desconto_ou_acrescimo}")
print(f"Total a pagar: R$ {valor_com_desconto_ou_acrescimo}")



