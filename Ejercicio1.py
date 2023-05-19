from random import(randint)
print("¡Hola usuario!")
numero1 = input("Elige un número del 1 al 10 para que la computadora adivine.")

numero_random = randint(1,1)

if numero1.isnumeric():
    if numero_random == int(numero1):
        print("La computadora adivinó el número")
    else:
        print("La computadora no adivinó el número")
else:
    print("ingresa un número valido.")






