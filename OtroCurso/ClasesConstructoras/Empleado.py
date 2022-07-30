from Persona import Persona

class Empleado(Persona):#De esta forma hereda todos los atributos de persona
    def __init__(self, nombre, apellido, dni, telefono, salario):
        super().__init__(nombre, apellido, dni, telefono)#para no repertir todos los atributos self.nombre = nombre etc se coloca super()
        self.salario = salario