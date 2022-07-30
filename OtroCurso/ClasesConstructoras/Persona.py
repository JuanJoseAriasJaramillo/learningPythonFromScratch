class Persona:
    def __init__(self, nombre, apellido, dni, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
    def __str__(self): #Esta funcion es para devolver un "Resumen", la heredan las demas funciones
        return self.nombre + ' ' + self.apellido + ' - ' + self.dni