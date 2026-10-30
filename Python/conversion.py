

import math




def binarioADecimal(cadena):
    #cadena 111
    n=len(cadena)-1
    j=0
    suma=0
    for i in range(n,-1,-1):
        suma +=int(cadena[i])*math.pow(2,j)
        j+=1
    return suma


def decimalABinario(n):
    binario=""
    while(n>0):
        resto=n%2
        binario=str(resto)+binario
        n=n//2
    return binario

#ca=cadena
def decimalHexadecimal(n):
    ca="0123456789ABCDEF"
    binario=""
    while(n>0):
        resto=n%16
        binario=ca[resto:resto+1]+binario
        n=n//16
    return binario


def decimalAOctal(n):
    binario=""
    while(n>0):
        resto=n&8
        binario=str(resto)+binario 
        n=n//8
    return binario

def hexaDecimalADecimal(cadena):
    ca="0123456789ABCDEF"
    n=len(cadena)-1
    suma=0
    j=0
    for i in range(n,-1,-1):
        suma +=ca.find(cadena[i:i+1])*math.pow(16,j)
        j+=1
    return suma


def octalADecimal(cadena):
    n=len(cadena)-1
    suma=0
    j=0
    for i in range(n,-1,-1):
        suma += int(cadena[i:i+1])*math.pow(8,j)
        j+=1
    return suma

if __name__ == '__main__':

    while(True):
        n=int(input("dime el numero decimal: "))
        if (n<0): break
        print(decimalABinario(n))
        print(binarioADecimal("111"))
        print(decimalHexadecimal(n))
        print(decimalAOctal(n))
        print(hexaDecimalADecimal("FF"))
        print(octalADecimal("377"))