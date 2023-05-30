qntd_faltas = int(input('Quantas faltas você tem? '))
media = int(input('Qual a sua média durante o ano? '))

if qntd_faltas <= 30 and media >= 5 and media <= 10:
    print('Aluno aprovado!')
elif media > 10:
    print('Você digitou a média errada!')
else:
    print('Aluno reprovado!')