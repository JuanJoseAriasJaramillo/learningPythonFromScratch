                            #si no pasan un argumento con ="person"agregamos un argumento por defecto
def hello(name ="person"): #para declarar una funcion usamos la palabra def
    print('helloworld ' + name)

hello("SAM-05MP")

def add(n1, n2):
    return n1 + n2

print(add(10,30))

suma = lambda numberOne, numberTwo: numberOne + numberTwo
print(add(50, 50))