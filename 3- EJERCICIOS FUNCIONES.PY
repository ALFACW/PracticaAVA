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
