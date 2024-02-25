soma = 0
cont = 0
numeros = [8, 3, 9, 4, 2]
for x in numeros:
    if x % 2 == 0:
     soma = soma + x
     cont = cont + 1
     media = soma/cont
     print("A media dos numeros pares deu igual á " + str(media))