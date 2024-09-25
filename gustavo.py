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
pagamento = int(input("Digite 1 para pagamento à vista ou 2 para cartão de crédito"))

if pagamento == 1:
    valor_final = valor_total * 0,10
else:
    valor_final = valor_total + (valor_total * 0,10)

