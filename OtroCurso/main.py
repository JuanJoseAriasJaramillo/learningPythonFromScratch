import funcionesMatematicas
from colorama import Fore, Back, Style, init
init(autoreset=True)


print(Fore.RED + "Calculadora hecha por JA")
encendido = int(input(Back.WHITE + "ingrese 1 si quiere usar la calculadora"))
pregunta = 1
if encendido == 1:
    while pregunta == 1:
        n1 = int(input(Fore.GREEN + "Ingrese el primer numero"))
        n2 = int(input(Fore.LIGHTGREEN_EX + "Ingrese el segundo numero"))
        decision = input(Style.BRIGHT + "Puedes usar suma, resta, multiplicacion, "
                         "division, potenciacion, es par utiliza sus respectivos "
                         "operadores logicos para escoger")

        if decision == '+':
            resultado = funcionesMatematicas.suma(n1, n2)
            print("Usando la f y las {}")
            print(f"Resultado {resultado}")
            str(funcionesMatematicas.suma(n1, n2))
            print("Usando cambio de tipo a string para poder concatenar")
            print(Fore.LIGHTYELLOW_EX + Back.BLUE + "Resultado " + str(funcionesMatematicas.suma(n1, n2)))
        elif decision == '-':
            print(Fore.LIGHTYELLOW_EX + Back.BLUE + "Resultado " + str(funcionesMatematicas.resta(n1, n2)))
        elif decision == '*':
            print(Fore.LIGHTYELLOW_EX + Back.BLUE + "Resultado " + str(funcionesMatematicas.multiplicacion(n1, n2)))
        elif decision == '/':
            print(Fore.LIGHTYELLOW_EX + Back.BLUE + "Resultado " + str(funcionesMatematicas.division(n1, n2)))
        elif decision == '**':
            print(Fore.LIGHTYELLOW_EX + Back.BLUE + "Resultado " + str(funcionesMatematicas.potenciacion(n1, n2)))
        elif decision == '%':
            if funcionesMatematicas.esPar(n1, n2) == True:
                print(Fore.LIGHTYELLOW_EX + Back.BLUE + "Resultado es par")
            else:
                print(Fore.LIGHTYELLOW_EX + Back.BLUE + "Resultado es inpar")

        pregunta = int(input(Back.WHITE + "Ingrese 1 para seguir usando la calculadora"))
