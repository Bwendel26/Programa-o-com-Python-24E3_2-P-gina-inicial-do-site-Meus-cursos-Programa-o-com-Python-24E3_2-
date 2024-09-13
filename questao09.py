valor = float(input("Digite o valor da compra: "))
if valor > 500:
    desconto = 0.25
elif valor > 200:
    desconto = 0.15
elif valor > 100:
    desconto = 0.10
else:
    desconto = 0

valor_com_desconto = valor * (1 - desconto)
print(f"Valor com desconto: R${valor_com_desconto:.2f}")
