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
      6 - Frango a Parmegiana 
      7 - Filé de Porco 
      """)

def exibir_menu(codigo_prato):
    match(codigo_prato):
        case 1:
            return "Picanha R$ 25,00",25
        case 2:
            return "Lasanha R$ 20,00",20
        case 3:
            return "Strogonoff R$ 18,00",18
        case 4:
            return "Bife acebolado R$ 15,00",15
        case 5:
            return "Pão com ovo R$ 5,00",5
        case 6:
            return "Frango a Parmegiana R$ 30,00",30
        case 7:
            return "Filé de Porco R$ 27,00",27
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

print("\n=== Pedidos realizados ===")
for item in pedido_cliente:
    print(f"-{item}")
print(f"Total a pagar: R$ {total_pedido:.2f}")
print("=== FIM ===")