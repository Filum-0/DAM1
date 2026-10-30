
#En el rango se pone 2 y n para saber si divido entre esos dos 

def IsPrimo(n):
    for i in range(2,n):
        if (n%i==0): return False
    return True


if __name__ == '__main__':
    numero=int(input("Dieme un numero: "))
    c=0
    while(c<5):
        if (IsPrimo(numero)):
            c+=1
            print(f'{c} {numero}')
        numero+=1

# c es la cantidad de primos que hay y numero para saber que numero se trata