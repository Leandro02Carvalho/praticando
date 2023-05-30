def calcular_desconto(valor, desconto = 0):
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto
valor1 = calcular_desconto(15)
valor2 = calcular_desconto(15.50, 0.25)

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")