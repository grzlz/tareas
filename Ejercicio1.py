print("¡Hola usuario!")
numero = input("Pon un número para calcular si es par o non.")

if numero.isnumeric():
    if int(numero) % 2 == 0:
        print("el número es par.")
    else:
        print("el número es non.")
else: 
    print("ingresa un número valido.")
