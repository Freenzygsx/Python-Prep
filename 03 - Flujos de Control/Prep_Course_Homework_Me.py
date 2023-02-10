
#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
print("Punto 1")
print("----------")
numeroEntero = 15
numeroEnteroMenor = -2
print(f"El primer numero entero {numeroEntero} es menor a 0? {numeroEntero<0}. Y el segundo? {numeroEnteroMenor}, pues es: {numeroEnteroMenor<0}")
print("----------\n")

#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
print("Punto 2")
print("----------")
var1 = '2'
var2 = 2
if type(var1) == type(var2):
    print("Si son el mismo tipo de dato")
else:
    print("Nop, no lo son")
print("----------\n")

#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
print("Punto 3")
print("----------")
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} par")
    else:
        print(f"{i} Impar")
print("----------\n")

#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
print("Punto 4")
print("----------")
for i in range(6):
    print(f"{str(i)} a la 3era potencia: {i**3}")
print("----------\n")

#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
print("Punto 5")
print("----------")
varEnteros = 8
for num in range(1, varEnteros+1):
    print("El for se realizara por {0} veces. Cuenta: {1}".format(varEnteros,num))
print("----------\n")

#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
print("Punto 6")
print("----------")
numeroFact = 5
numeroTemp = numeroFact
contador = numeroFact - 1
if type(numeroTemp) == int and numeroTemp > 0:
    while contador != 1:
        numeroTemp *= contador
        contador -= 1
    print("Factorial de {0} es: {1}".format(numeroFact, numeroTemp))
else:
    print("Verifique que la variable sea un entero y que este sea mayor a 0, por favor.")


print("----------\n")

#7) Crear un ciclo for dentro de un ciclo while
print("Punto 7")
print("----------")
while True:
    for i in range(11):
        print(7*i)
    break
print("----------\n")

#8) Crear un ciclo while dentro de un ciclo for
print("Punto 8")
print("----------")
for i in range(11):
    while i % 2 == 0:
        print(i)
        break
print("----------\n")

#9) Imprimir los números primos existentes entre 0 y 30
print("Punto 9")
print("----------")
for i in range(2, 31):
    n = i
    counter = 0
    while n != 1:
        if i % n == 0:
            counter+=1
        n-=1
    if counter > 1:
        print("El numero {0} es compuesto".format(i))
    else:
        print("El numero {0} es primo".format(i))

print("----------\n")

#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
print("Punto 10")
print("----------")
for i in range(2, 31):
    n = i
    counter = 0
    while n != 1:
        if i % n == 0:
            counter+=1
        n-=1
        continue
    if counter > 1:
        print("El numero {0} es compuesto".format(i))
    else:
        print("El numero {0} es primo".format(i))

print("----------\n")

#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
print("Punto 11")
print("----------")
print("La forma que conozco de saber si se optimizo un codigo o no es corriendo los dos y calculando cuanto tiempo tarda en correr cada codigo para saber cual es mas optimo")
print("----------\n")

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
print("Punto 12")
print("----------")
print("La optimizacion deberia ser porcentual en medida de los datos que se inserten")
print("----------\n")

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
print("Punto 13")
print("----------")
inicio = 100
while inicio != 300:
    if inicio % 12 != 0:
        inicio += 1
        continue
    else:
        print(inicio)
        inicio += 1
print("----------\n")

#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
print("Punto 14")
print("----------")
continuar = True
contadorFinal = 0

while continuar == True:
    numero: int = int(input("Inserte un numero para ver si es primo: "))
    for i in range(2, numero):
        if numero % i == 0:
            contadorFinal += 1
    if contadorFinal > 1:
        print("El numero es compuesto.")
    else:
        print("El numero es primo.")

    verificarContin = input("Desea verificar otro numero? (Y/n): ")
    while verificarContin.lower() != 'y' and verificarContin.lower() != 'n':
        verificarContin = input("Desea verificar otro numero? (Y/n): ")

    if verificarContin.lower() == 'n':
        continuar = False
        break
    elif verificarContin.lower() == 'y':
        contadorFinal = 0
        print("\n----------\n")
        continue

print("----------\n")

#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
iniciov2 = 100
while iniciov2 != 300:
    if iniciov2 % 3 == 0:
        if iniciov2 % 6 == 0:
            print(iniciov2)
            break
    iniciov2 += 1
