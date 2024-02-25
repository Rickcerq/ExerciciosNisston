numero = 13
if numero >= 1:
    for fatorial in range (2, numero):
        if numero % fatorial != 0:
            print (str(numero) + ' É primo')
            break
        else:
            print (str(numero) + ' Não é primo')
elif numero == 0:
    print (str(numero) + ' É zero')
elif numero == 1:
    print (str(numero) + 'É um')
else:
    print (str(numero) + ' É negativo')
