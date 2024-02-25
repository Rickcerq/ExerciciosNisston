numero = int(input('Digite um numero inteiro positivo: '))

resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)