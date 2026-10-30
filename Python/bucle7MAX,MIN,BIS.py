
#es el ejercicio bucle 6 pero optimizado

if __name__ == '__main__':

    numero=float(input("Introduce un numero: "))
    maximo=minimo=numero
    
    for i in range(2,6):
        numero=float(input("Introduce un numero: "))

        if(numero>maximo):
            maximo=numero
        elif (numero<minimo):
            minimo=numero

    print(f'El minimo: {minimo} \ El maximo es: {maximo}')
