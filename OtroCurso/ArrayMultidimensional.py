historial = [
    [34.5, 45.6, "2022/28/07  3:26pm"],
    [34.5, 45.6, "2022/28/07  3:28pm"],
    [34.5, 45.6, "2022/28/07  3:29pm"],
    [34.5, 45.6, "2022/28/07  3:03pm"],
    [34.5, 45.6, "2022/28/07  3:23pm"],
    [34.5, 45.6, "2022/28/07  3:6pm"]
]
indiceLongitud = 0
indiceLatitud = 1
indiceFecha = 2
for coordenada in historial:
    print(coordenada[indiceLongitud])#recorre y recibe un "parametro" para escoger que vector
