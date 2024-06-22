def suma():
    a = int(input("Ingrese un valor para a: "))
    b = int(input("Ingrese un valor para b: "))
    
    return a+b

def resta():
    a = int(input("Ingrese un valor para a: "))
    b = int(input("Ingrese un valor para b: "))
    return a - b

def dividir():
    a = int(input("Ingrese un valor para a: "))
    b = int(input("Ingrese un valor para b: "))
    return a/b

def multiplicar():
    a = int(input("Ingrese un valor para a: "))
    b = int(input("Ingrese un valor para b: "))
    return a*b


def mostrar_menu():

    print("Seleccione la operación que desea realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la operación que desea realizar: ")
    if opcion == "1":
        print("La suma entre a y b es", suma())
    elif opcion == "2":
        print("La resta entre a y b es", resta())
    elif opcion == "3":
        print("La multiplicacion entre a y b es", multiplicar())
    elif opcion == "4":
        print("La division entre a y b es", dividir())
    elif opcion == "5":
        print("Has salido del programa")
        break
    else:
        print("Escoge una opcion valida ")

