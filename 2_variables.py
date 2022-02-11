#Declaración y uso de variables con python

def numeros():
    entero = 4 #numero entero
    print(entero)
    print(type(entero)) #ver el tipo de dato
    decimal = 4.5 #numero decimal o flotante
    print(decimal)
    print(type(decimal))
    entero_negativo = -4 #número entero negativo
    print(entero_negativo)
    print(type(entero_negativo))
    #multiples variables enteras
    numero_1, numero_2, numero_3 = 10, 8, 6
    resultado_1 = numero_3 ** 2 # numero_3 elevado a la potencia 2
    print(numero_1 + numero_2)
    print("Resultado 1:", resultado_1)
    # variable booleana
    verdad = True
    falso =  False
    print(verdad)


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

    #imprimir partes de una cadena
    micadena = "YONATAN"
    #[0:4:1] signigica que: empieza en la posición 0 de la cadena hasta la posición 4 conp paso 1
    print(micadena[0:4:1]) 
    #[::-1] signigica que: empieza en la posición 0 de la cadena hasta la última posición con paso -1 de forma descendente
    print(micadena[::-1]) 
    #[0:4] signigica que: empieza en la posición 0 de la cadena hasta la posición 4, cuando no menciona el paso se sobre entiende que es 1
    print(micadena[0:4]) 



def listas():
    #las listas son dinámicas
    #las listas se puede modificar durante la ejecución del programa mientras para las tuplas no es posible alterar su contenido.
    lista_1 = ["Yonatan", "Juan", "Rosa", "Lucho"] #lista de nombres
    print(lista_1) #impresión ['Yonatan', 'Juan', 'Rosa', 'Lucho']
    print(*lista_1)
    print(lista_1[0]) #imprimir el nombre de la lista con  posición 0 "Yonatan"
    lista_2 = [10, 8, 9, 3]
    print(lista_2)
    lista_3 = ["yonatan", 10, True]
    print(lista_3)
    print(type(lista_3))
    #otra forma de crear lista es con el la función o constructor list
    milista = list(("Yonatan", "Maria", "Flor"))
    print(milista)

def tuplas():
    #las tuplas son estáticas, no se puede modificar en tiempo de ejecución
    tupla_1 = ("Python", "Java", "Php")
    print(tupla_1)
    print(type(tupla_1))
    #otra forma de crear tuplas
    tupla_2 = tuple((10, 12, 20))
    print(tupla_2)
    #Convirtiendo una tupla a lista
    print(list(tupla_1))

def diccionario():
    # Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.
    # Un diccionario es una colección ordenada, modificable y que no admite duplicados.
    # Los diccionarios no pueden tener dos elementos con la misma clave:
    
    diccionario_1 = {"Nombre":"Yonatan", "Apellidos":"Mamani", "Lenguaje":"Python", "Año":2022}
    print(diccionario_1)
    print(diccionario_1["Nombre"])
    diccionario_2 = {
        "nombre":"Yonatan",        
        "apellidos":"Mamani",
        "lenguajes":["Python", "Php", "Java"]
    }
    print(diccionario_2)
    print(diccionario_2.keys()) 
    print(diccionario_2.values())
    #diccionario anidadas
    diccionario_anidadas ={
        'd0':{'nombre':'yonatan', 'lenguaje':'python'},
        'd1':{'nombre':'rosa', 'lenguaje':'java'},
        'd2':{'nombre':'coqui', 'lenguaje':'php'}
    }
    print(diccionario_anidadas)
    print(diccionario_anidadas["d0"]["nombre"])
    print(diccionario_anidadas["d1"]["nombre"])
    print("**")
    contador = 0
    variable = "d"
    for i in diccionario_anidadas.items():        
        print(diccionario_anidadas[variable + str(contador)]["nombre"] + " - " + 
                diccionario_anidadas[variable + str(contador)]["lenguaje"])
        contador+=1
        

def run():
    #numeros()
    #cadenas()
    #listas()
    #tuplas()
    diccionario()

if __name__ == '__main__':
    run()
