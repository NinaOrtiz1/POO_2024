paises = ['Colombia', 'Perú', 'Argentina', 'Chile']
numeros = [100, 80, 3.1416, 75]
varios = ["UTD", True, 100, 0.100]

#Ordenar listas 
print(paises)
paises.sort()
numeros.sort()



#Agregar eleementos 
print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros, 200))
print(numeros)

#Remover elementos
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2)
print(numeros) 


#Dar vuelta a los elementos
try:
    print(varios)
    varios.reverse()
    print(varios)
except Exception as e:
    print(f"Ha ocurrido un error: {e}")

#Buscar valores
encontro = "Colombia" in varios
print(encontro)

#Borrar una lista 
paises = ['Colombia', 'Perú', 'Argentina', 'Chile']
print(paises)
paises.clear()
print(paises)

#Unir listas
print(varios)
varios.extend(numeros)
print(varios)