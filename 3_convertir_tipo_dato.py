#convertir un dato a un tipo diferente

#ingresar número por el teclado
numero_1 = input("ingrese un número: ")
print(numero_1) #imprime el número en tipo texto

#ahora el numero ingresado convertir a entero
numero_entero = int(float(numero_1)) # función int para convertir a entero
print("Número entero: ", numero_entero)

#ahora el numero ingresado convertir a un flotante o decimal
numero_flotante = float(numero_1)
print("Número decimal: ", numero_flotante)

#ahora el numero flotante o decimal vamos a convertir a texto o cadena
numero_texto = str(numero_flotante)
print("Número en texto: ", numero_flotante)
