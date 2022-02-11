#Para utilizar condicionales debemos utilizar la siguiente palabras reservadas
# if - elif - else

# Ejemplo 1: ingresar la edad de una persona si es mayor o igual a 18 escribir "Mayor de edad" caso contrario "Menor de dedad"

edad = int(input("Ingrese edad: "))

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

#Ejemplo 2: edades
edad2 = int(input("Ingrese edad: "))
if edad2 < 0:
    print("No puede tener edad negativa")
elif edad2 >= 0 and edad2 < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")


#Ejemplo 3: ingresar dos numeros e identificar el número mayor
numero_1 = float(input("Número 1: "))
numero_2 = float(input("Número 2: "))

if numero_1 > numero_2:
    mayor = numero_1
elif numero_2 > numero_1:
    mayor = numero_2

print("Número mayor es: ", mayor)

# Ejmplo 4: ingresar número y evaluar si es par o impar

numero_3 = int(input("Ingrese número : "))
if numero_3 % 2 == 0:
    print(f"{numero_3} es par")
else:
    print(f"{numero_3} es impar")
# operadores lógicos y de comparación
#lógicos
# and "&" :para comparar si dos valores son verdaderos.
# or "|"  :para comparar si dos valores son falsos.
# not :para invertir el valor booleano.
# Comparación
# > "mayor que"   < "menor que"   >= "mayor o igual que" <= "menor o igual que"  == "igualda" != "diferente"