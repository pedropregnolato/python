'''Faça um programa que leia o nome de um produto, a quantidade comprada, o valor 
unitário e o percentual de desconto a ser aplicado para o pagamento. Mostre o nome do 
produto e o valor total da venda'''

p = str(input("Produto: "))
q = int(input("Quantidade: "))
v = float(input("Valor: "))

conta = q * v

descontoDebito = conta - (conta * 0.05)
descontoPix = conta - (conta * 0.1)

print(
    "Você está comprando", q, "unidade(s) de", p,
    "o valor é R$", conta,
    "\n pagando no dinheiro ou débito fica R$", descontoDebito,
    "\n pagando no Pix fica R$", descontoPix)