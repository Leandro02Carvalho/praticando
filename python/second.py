a = int(input('Primeiro valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior valor inserido foi {}' .format(a))
elif b > a and b > c:
    print('O maior valor inserido foi {}' .format(b))
else: 
    print('O maior inserido foi {}' .format(c))

print('Final do programa')