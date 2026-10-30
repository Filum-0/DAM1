n=10

for i in range(1,n+1):
    print(" "*(n-i)+"*"*i+"*"*(i-1))
    

print ("----------------------")

for i in range(1,n+1):
    print(" "*(i-1)+"*"*(n-(i-1))+"*"*(n-i))