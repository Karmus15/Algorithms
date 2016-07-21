vNumBuscar = input("Ingrese un numero\n")
print ""

a, b = 0, 1
print a
print b

while b < vNumBuscar:
    c = b + a
    a = b
    b = c
    print c
    if c == vNumBuscar:
        print "Encontrado!"
    elif c > vNumBuscar:
        print "El numero no esta en la serie Fibonacci"
        
        

    


