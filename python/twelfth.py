a = 2
b = 1

equacao = input('Digite uma formula linear: ')
print(f'\n A entrada do usuário {equacao} é do tipo {type(equacao)}')

for x in range(5):
    y = eval(equacao)
    print(f'\n Resultado da equacao para x = {x} é {y}')