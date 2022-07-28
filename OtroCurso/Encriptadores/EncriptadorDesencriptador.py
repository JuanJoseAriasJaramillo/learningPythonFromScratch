# archivo = open('texto.txt', 'a')#agregar texto al archivo 'w'Reemplazar todo el contenido
# archivo.write('Prueba de guardado en el ardchivo')
# archivo.close()#con esto se cierra la operacion (o sea el archivo)
#
# archivo = open('texto.txt', 'r')
# print(archivo.read())

#'a'agregar texto a un archivo
#'w'Reemplazar todo el contenido
#'r'Solo lectura
'''f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()'''

#open and read the file after the appending:

def encriptar(texto):
    print('El texto a encriptar es: ' + texto)
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    return textoFinal


def desencriptar(texto):
    print('El texto a desencriptar es: ' + texto)
    textoFinal = ''
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra
        contador += 1
    return textoFinal


def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print('El archivo se encripto correctamente')

def desencriptarArchivo(textoFinal):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print('El archivo se desencripto correctamente')


respuestaEoD = input('Presione "E" para encriptar, o "D" para desencriptar')
rutaArchivo = input('Ingerese la ruta del archivo')

if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)