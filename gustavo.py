import os
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
