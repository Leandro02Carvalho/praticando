a = int(input('Nota do primeiro bimestre: '))
b = int(input('Nota do segundo bimestre: '))
c = int(input('Nota do terceiro bimestre: '))
d = int(input('Nota do quarto bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Nota: {}' .format(media))
else:
    print('foi informada alguma nota errada')
    