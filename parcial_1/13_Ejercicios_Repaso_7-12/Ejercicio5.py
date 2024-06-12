# Crear una lista y un diccionario con el contenido de esta tabla: 
#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION
# imprimir la información

peliculas_y_canales = [
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]
catalogo = {
    "ACCION": peliculas_y_canales[0][0::2],
    "TERROR": peliculas_y_canales[0][1::2],
    "DEPORTES": peliculas_y_canales[1][1::2]
}
print("Lista de películas y canales:")
for fila in peliculas_y_canales:
    print(fila)
print("\nCatálogo:")
for categoria, contenido in catalogo.items():
    print(f"{categoria}:")
    for elemento in contenido:
        print(elemento)
    print()