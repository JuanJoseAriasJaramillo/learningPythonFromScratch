10
14.2
print(type(9))
print(type(10.1))

# print(1+1)
# print(2**3)#**es un elevador, numero a la izquierda que va a ser elevado a X cantidad
# print(2//3)#Operador Modulo, de vuelve el residuo
# print(3%2)#Operador Modulo, de vuelve el residuo
print(20 - 10 / 5 * 3**10)#python funciona con tabla de presedencia, primero (), **, *, /, +, -
print((20 - 10) / (5 * 3**10))  # primer o parentesis

age = input("Insert your age: ")  # esto sirve para tomar datos del usuario
#todo lo que insertamos al programa por input es un STRING


print(f"Esta es tu edad: {age}")
print(type(age))
newAge = int(age) + 5**3 #aqui pasamos el string a entero para poder hacer la op
print("Esta es tu edad usando format: {0}".format(newAge))
print(type(age))
print(type(newAge))
#otro ejemplo es:
#print(type(float(newAge)))
