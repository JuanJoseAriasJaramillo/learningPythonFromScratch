#own modules
#thidy part modules
#python modules
#modules thirdy party https://pypi.org/ creados por otras empresas


#modules python free index https://docs.python.org/3/py-modindex.html
import datetime #importa todo el modulo
from datetime import timedelta #importa un metodo en especifico de la libreria

print(datetime.date.today())
print(datetime.timedelta(minutes=70))#recibe minutos y los convierte a horas

import Fmath
Fmath.add(1, 2)
Fmath.substract(1,2)

from Fmath import add, substract

substract( 95, 98)
add(223, 34)

from colorama import Fore, Style
print(Fore.RED + "Hello world")