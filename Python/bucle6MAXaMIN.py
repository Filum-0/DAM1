

#primera formad de hacerlo:

if __name__ == '__main__':

#campo de existencia de -infinito a +infinito
#float es para decimales, el maximo minimo numero sirve para que todos sean igual y haga que pueda comparar bien con todo lo demas  
    for i in range(1,6):
        numero=float(input("Introduce un numero: "))
        if (i==1):
            maximo=minimo=numero
        else:
            if(numero>maximo):
                maximo=numero
            elif (numero<minimo):
                minimo=numero
    print(f'El minimo: {minimo} \ El maximo es: {maximo}')


#segunda forma de hacerlo:

numero=float(input("Introduce un numero: "))

maximo=minimo=numero
    
for i in range(2,6):
    if(numero>maximo):
        maximo=numero
    elif (numero<minimo):
        minimo=numero
        
    print(f'El minimo: {minimo} \ El maximo es: {maximo}')