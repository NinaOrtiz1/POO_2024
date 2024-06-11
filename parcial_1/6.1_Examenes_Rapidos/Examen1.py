new_paciente = "SI"
paciente = 0
sSis = 0
sDia = 0
m = 1
while new_paciente == "SI" or new_paciente == "S":
    paciente += 1
    name = input("Ingresa el nombre: ")
    ts = input("Ingresa el tipo de sangre: ")
    for i in range(3):
        print(f"MEDICION {m}")
        sis = int(input("Ingresa el valor de SIStolica: "))
        sSis += int(sis)
        dia = input("Ingresa el valor de DIAtolica: ")
        sDia += int(dia)
        m +=1
    
    #Add Input to record the last measurement
    mSISFinal = input("Ingresa la medicion final:") #ADD
    mDIAFinal = input("Ingresa la medicion final:") #ADD
    
    promedioSis = sSis / 3
    promedioDia = sDia / 3

    print(f"Nombre: {name}")
    print(f"Tipo de sangre: {ts}")
    #Add lines to print the las measurement
    print(f"Ultima medicion SIS: {mSISFinal}") #ADD
    print(f"Ultima medicion DIA: {mDIAFinal}") #ADD
    if promedioSis <= 120 and promedioDia <= 80:
        print("Presenta una precion normal")

    print(f"El promedio de la SIStolica es de: {promedioSis}")
    print(f"El promedio de la DIAtolica es de: {promedioDia}")

    new_paciente = input("Desea agregar otra captura? (SI/NO): ").upper()


print(f"El numero de pacientes fue de: {paciente}")