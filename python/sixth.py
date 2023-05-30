lista = [1, 22, 2, 34]
lista_animais = ['cachorra', 'panda', 'leoncio']

a = input('Escreva o nome de algum animal: ')

if a in lista_animais:
    print('tem {} aqui, corre' .format(a))
else:
    print('Não tem {} aqui, pode encostar!' .format(a))