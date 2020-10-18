# importacion de librerias 
from colorama import Fore

# definicion de funciones 
def Suma():
    print(Fore.YELLOW + "**Estamos en funcion suma**\n")
    numero_1 = float(input(Fore.BLUE + 'Ingrese el primer número:\n'))
    numero_2 = float(input(Fore.BLUE + 'Ingrese el segundo número:\n'))
    suma = numero_1 + numero_2
    print(Fore.GREEN + "El resultado de la suma es: ", suma)

def Resta():
    print(Fore.YELLOW + "**Estamos en funcion resta**\n")
    numero_1 = float(input(Fore.BLUE + "Ingrese el primer numero:\n")) # int('5') => 5
    numero_2 = float(input(Fore.BLUE + "Ingrese el segundo numero:\n"))
    resta = numero_1 - numero_2
    print(Fore.GREEN + "El resultado de la resta es: ", resta)

def Multiplicacion():
    print(Fore.YELLOW + "**Estamos en funcion multiplicacion**\n")
    numero_1 = float(input(Fore.BLUE + "Ingrese el primer numero:\n")) # int('5') => 5
    numero_2 = float(input(Fore.BLUE + "Ingrese el segundo numero:\n"))
    multiplicar = numero_1 * numero_2
    print(Fore.GREEN + "El resultado de la multiplicacion es: ", multiplicar)

def Dividir():
    print(Fore.YELLOW + "**Estamos en funcion dividir**\n")
    numero_1 = float(input(Fore.BLUE + "Ingrese el primer numero:\n")) # input(Fore.BLUE + "Ingrese el primer numero:\n") => "5.4" => float("5.4") => 5.4
    numero_2 = float(input(Fore.BLUE + "Ingrese el segundo numero:\n"))
    if (numero_2 == 0):
        print(Fore.RED + "Segun el fabricante el segundo numero debe ser mayor a cero")
    else:
        dividir = numero_1 / numero_2
        print(Fore.GREEN + "El resultado de la dividir es: ", dividir)

def Welcome():
    print("#"*34)
    print(" Welcome to calculadora by Morens")
    print("#"*34)

def Menu():
    print("Opciones:")
    print("-"*34)
    print("Suma => 1")
    print("-"*34)
    print("Resta => 2")
    print("-"*34)
    print("Multiplicacion => 3")
    print("-"*34)
    print("Division => 4")
    print("-"*34)   
    print("Salida => 5")

# llamadas a funciones 
#Dividir()
#Multiplicacion()
#Resta()
#Suma()
#Welcome()
#Menu()
