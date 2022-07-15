demo_list = [1, 'hello', 1.34, True, [1,2,3] ]
colors = ['red', 'green', 'blue']

# numbers_list = list((1,2,3,4))#list sirve para crear la lista, pero solo recibe un parametro par alograr el objetivo necesitamos una tupla
# print(numbers_list)
# print(type(numbers_list))

# r = list(range(1, 9))#toma dos parametros de donde a donde quiero crear
# print(r)

# print(type(colors))
# print(len(colors))
# print(colors[2])
# print(colors[-2])
# print('green' in colors)#pregunta dentro de una lista si esta un elemento x
# print('violet' in colors)
# print(colors)
# colors[1] = 'violet'
# print(colors)

#print(dir(colors)
#colors.append('violeta')#sirve para agregar un unico elemento
#colors.extend(['violeta', 'yellow'])#este tambien recibe un unico elemento, pero si le paso una TUPLA o una LISTA los va a agregar como elementos de la lista.
print(colors)
colors.insert(1, 'morcilla') #se utiliza para insertar un elemento justo despues del primer argumento dado que es la posicion
colors.insert(len(colors), 'sapote')
print(colors)
colors.pop()#quita el ultimo elemento de la lista
print(colors)
colors.pop(3)#tambien si recibe un indice elimina ese iindice de la lista
print(colors)
colors.remove('green')#te permite apuntar a un elemento que coincida con el parametro para eliminarlo
print(colors)
colors.extend(['violeta', 'yellow', 'rojopa', 'morado', 'colorvenezuela'])
colors.sort()#el metodo sin parametros ordena la lista en orden alfabetico
print(colors)
colors.sort(reverse=True)
print(colors)

print(colors.index('red'))#Encontramos el indice de este elemento

colors.clear()#limpia toda la lista
print(colors)
