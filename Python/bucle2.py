

if __name__ == '__main__':

#contador de pares e impares
    cpares=cimpares=0

    while(True):
        n=int(input("Dieme un numero: "))     
        if (n<0):break
        if (n%2==0):
            cpares +=1
        else:
            cimpares +=1


    print(f'Numero de pares: {cpares} \ Numero de impares: {cimpares}')