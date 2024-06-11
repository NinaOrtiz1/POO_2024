"""      
***12.56 se le suma al total***
se suma basico + intermedio
se le saca iva a la suma anterior



cantidad_kWh = int(input("Ingresa la cantida de kWh consumidos: "))
basico =  0.987 * cantidad_kWh

if cantidad_kWh > 1 and cantidad_kWh < 150:
    #Sacar IVA
    IVA = basico * .16
    #total
    Total = basico + IVA 
    
    print(f"Cantidad de kWh consumidos: {cantidad_kWh}kWh")
    print(f"Subtotal: {basico}")
    print(f"IVA: ${IVA}")
    print(f"El precio a pagar es de: ${Total}")
else:
    #Extraer el excedente
    excedente = cantidad_kWh - 150
    #Sacar el $ del excedente
    intermedio = 1.203 *  excedente
    #Suma de los $ anteriores
    kWhTotal = basico + intermedio
    #IVA de la suma
    IVA = kWhTotal * .16
    #Total
    Total = kWhTotal + IVA 
    
    print(f"Cantidad de kWh consumidos: {cantidad_kWh}kWh")
    print(f"Cantidad de kWh excedidos: {excedente}kWh")
    print(f"Subtotal: {kWhTotal}")
    print(f"IVA: {IVA}")
    print(f"El precio a pagar es de: ${Total}")
"""

def ReciboLuz():
    cantidad_kWh = int(input("Ingresa la cantida de kWh consumidos: "))
    basico =  0.987 * cantidad_kWh

    if cantidad_kWh > 1 and cantidad_kWh < 150:
        #Sacar IVA
        IVA = basico * .16
        #total
        Total = basico + IVA 

        print(f"Cantidad de kWh consumidos: {cantidad_kWh}kWh")
        print(f"Subtotal: {basico}")
        print(f"IVA: ${IVA}")
        print(f"El precio a pagar es de: ${Total}")
    else:
        #Extraer el excedente
        excedente = cantidad_kWh - 150
        #Sacar el $ del excedente
        intermedio = 1.203 *  excedente
        #Suma de los $ anteriores
        kWhTotal = basico + intermedio
        #IVA de la suma
        IVA = kWhTotal * .16
        #Total
        Total = kWhTotal + IVA 

        print(f"Cantidad de kWh consumidos: {cantidad_kWh}kWh")
        print(f"Cantidad de kWh excedidos: {excedente}kWh")
        print(f"Subtotal: {kWhTotal}")
        print(f"IVA: {IVA}")
        print(f"El precio a pagar es de: ${Total}")
ReciboLuz()