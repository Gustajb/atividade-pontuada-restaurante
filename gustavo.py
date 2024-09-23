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

opcao = int(input("Digite o número do prato desejado: "))

while True:
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
    break
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

