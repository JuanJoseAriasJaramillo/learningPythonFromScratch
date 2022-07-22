import funcionesMatematicas

print("Calculadora hecha por JA")
encendido = int(input("ingrese 1 si quiere usar la calculadora"))
pregunta = 1
if encendido == 1:
    while pregunta == 1:
        n1 = int(input("Ingrese el primer numero"))
        n2 = int(input("Ingrese el segundo numero"))
        decision = input("Puedes usar suma, resta, multiplicacion, "
                         "division, potenciacion, es par utiliza sus respectivos "
                         "operadores logicos para escoger")

        if decision == '+':
            resultado = funcionesMatematicas.suma(n1, n2)
            print("Usando la f y las {}")
            print(f"Resultado {resultado}")
            str(funcionesMatematicas.suma(n1, n2))
            print("Usando cambio de tipo a string para poder concatenar")
            print("Resultado " + str(funcionesMatematicas.suma(n1, n2)))
        elif decision == '-':
            print("Resultado " + str(funcionesMatematicas.resta(n1, n2)))
        elif decision == '*':
            print("Resultado " + str(funcionesMatematicas.multiplicacion(n1, n2)))
        elif decision == '/':
            print("Resultado " + str(funcionesMatematicas.division(n1, n2)))
        elif decision == '**':
            print("Resultado " + str(funcionesMatematicas.potenciacion(n1, n2)))
        elif decision == '%':
            if funcionesMatematicas.esPar(n1, n2) == True:
                print("Resultado es par")
            else:
                print("Resultado es inpar")

        pregunta = int(input("Ingrese 1 para seguir usando la calculadora"))


