numero = 123456789
contador = 0

while numero >= 1:
    contador+=1
    numero = numero / 10
else:
    print("La cantidad de digitos del numero es:", contador)