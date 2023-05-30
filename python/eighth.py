a = int(input('Coloque um número: '))
b = int(input('Coloque outro número diferente: '))

if a == b:
    print('Os números são iguais!')
elif a < b:
    print('O {} é o menor número digitado!' .format(a))
elif a > b:
    print('O {} é o menor número digitado!' .format(b))
else:
    print('Você digitou um número?')