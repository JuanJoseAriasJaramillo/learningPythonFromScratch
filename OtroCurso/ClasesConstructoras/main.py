from Empleado import Empleado
from Cliente import Cliente
'''emp = Empleado("DonJairo", "Velez", "703231457", "3105250736", "100'000.000")
cli = Cliente("Lucas", "gomez", "1001414652", "3187911885", "MasterVIP")'''

def cargar():
    respuesta = input('Va a agregar un empleado?')
    nombre = input('Ingrese el nombre')
    apellido = input('Ingrese el apellido')
    dni = input('Ingrese el dni')
    telefono = input('Ingrese el telefono')

    if(respuesta == 'si'):
        salario = input("Ingrese el salario")
        emp = Empleado(nombre, apellido, dni, telefono, int(salario))
        personas.append(emp)
    else:
        categoria = input("Ingrese la categoria")
        cli = Cliente(nombre, apellido, dni, telefono, categoria)
        personas.append(cli)

personas = []
cargar()
cargar()

for persona in personas:
    print(persona)



