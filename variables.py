#Declaración y uso de variables con python

def numeros():
    entero = 4 #numero entero
    print(entero)
    print(type(entero))
    decimal = 4.5 #numero decimal o flotante
    print(decimal)
    print(type(decimal))
    entero_negativo = -4 #número entero negativo
    print(entero_negativo)
    print(type(entero_negativo))

def cadenas():
    texto = "Hola soy texto en python"
    print(texto)
    print(type(texto))
    #concatenación
    texto_1 = "Hola"
    texto_2 = "python"
    print(texto_1 + " " + texto_2)
    #mutiples variables de texto
    cadena_1, cadena_2, cadena_3 = "Hola", "python", "yonatan"
    print(cadena_1)
    print(cadena_1+" "+cadena_2+" saludos de "+cadena_3)

def run():
    #numeros()
    cadenas()

if __name__ == '__main__':
    run()
