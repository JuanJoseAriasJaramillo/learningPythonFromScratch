from calendar import c


colors = {'red','blue','yellow','green',}
print(colors)
print('red' in colors)
colors.add('violet')
print(colors)

colors.clear()
print(colors)
del colors #esta linea elimina colors
print(colors)