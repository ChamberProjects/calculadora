numero1 = int(input("ingrese numero 1 : "))
numero2 = int(input("ingrese numero 2 : "))

opcion = 0 

while True:
    
    opcion = int(input("opciones : "))
    if opcion == 1:
        print(numero1,"+",numero2, "la suma es",numero1+numero2)
    elif opcion == 2:
        print(numero1, "-", numero2, "la resta es",numero1+numero2)
    elif opcion == 3: 
        print(numero1, "*", numero2, "la multiplicacion es", numero1+numero2)
    elif opcion == 4:
        print(numero1, "%", numero2, "la division es ", numero1+numero2)
        
    else:
        print("opcion incorrecta...")
