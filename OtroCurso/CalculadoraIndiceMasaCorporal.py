#Calculadora de IMC
#IMC = Peso / (Altura x ALtura)
#< 19: Delgadez
#entre 20 y 25: normal
#entre 26 y 30:sobrepeso
#> de 30: Obesidad

peso = float(input('Ingrese su peso en KG'))
alturaEnCM = int(input('Meta su altura en cm'))
alturaEnMetros = alturaEnCM / 100

def calculaIMC(peso, altura):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    estado = ''
    if imc < 20:
        estado = "Delgadez"
    if imc >= 20 and imc < 25:
        estado = 'Normal'
    if imc >= 26 and imc < 30:
        estado = 'Sobrepeso'
    if imc >= 30:
        estado = 'Obesidad'

    return print(f"Usted esta en estado de {estado}, y su indice de masa corporal es: {imc}")


calculaIMC(peso, alturaEnMetros)
