def leer_archivo (nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
       contenido = archivo.read()
    return contenido
print(leer_archivo("datos.txt"))

def calculo_promedio (nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        suma_total=0
        contenido = archivo.read()
        for linea in contenido:
            numero = nombreArchivo.splitlines()
            for numeros in linea:
                convertir = [int (i) for i in numeros]
                print(convertir)
                numero = convertir
                suma_total= suma_total+numero
           return suma_total
        
print(calculo_promedio("datos.txt"))
import statistics as st
def leerArchivo(nombreArchivo):
    with open(nombreArchivo, "r") as archivo:
        numero = archivo.read().splitlines()
        intconvertir = [int (i) for i in numero]
        numero = intconvertir

        mediana = st.median(numero)
        promedio = sum(numero) /len(numero)
        modas = st.mode(numero)
        return promedio, mediana, modas, numero
    
print(leerArchivo('datos.txt'))