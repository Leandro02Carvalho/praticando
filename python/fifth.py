#PARA SABER SE O NÚMERO DIGITADO É PRIMO

#a = int(input('Entre com um número: '))
#div = 0
#for x in range(1, a+1):
#    resto = a % x
#    print(x, resto)
#if resto == 0:
#    div += 1

#if div ==2:
#    print('Número {} é primo' .format(a))
#else:
#    print('Número {} não é primo' .format(a))




#PARA SABER OS NÚMEROS ENTRE 1 E 100 QUE SÃO PRIMOS

for num in range(101):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1 
    if div == 2:
        print(num)
