#1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
print("Punto 1: Lista de ciudades del mundo")
print("----------")
ciudades = ['Tokyo', 'New York', 'Los Angeles', 'Caracas',' Falcon']
for ciudad in ciudades:
    print(ciudad)
print(ciudades)
print("----------\n")
#2) Imprimir por pantalla el segundo elemento de la lista
print("Punto 2: Imprimir el segundo elemento de la lista")
print("----------")
print(ciudades[1])
print("----------\n")

#3) Imprimir por pantalla del segundo al cuarto elemento
print("Punto 3: Imprimir el tercer elemento de la lista")
print("----------")
print(ciudades[3])
print("----------\n")

#4) Visualizar el tipo de dato de la lista
print("Punto 4: Ver el tipo de dato de la lista")
print("----------")
print(type(ciudades))
print("----------\n")

#5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print("Punto 5: Ver todos los elementos desde el tercer elemento en adelante")
print("----------")
print(ciudades[2:])
print("----------\n")

#6) Visualizar los primeros 4 elementos de la lista
print("Punto 6: Visualizar los primeros 4 elementos de la lista")
print("----------")
print(ciudades[:4])
print("----------\n")

#7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
print("Punto 7: Agrega una ciudad que este en la lista y otra que no, da error?")
print("----------")
ciudades.append("New York")
ciudades.append("Cuba")
print("No")
print(ciudades)
print("----------\n")

#8) Agregar otra ciudad, pero en la cuarta posición
print("Punto 8: Agrega otra ciudad en la cuarta posicion")
print("----------")
ciudades.insert(3, "Miami")
print(ciudades)
print("----------\n")

#9) Concatenar otra lista a la ya creada
print("Punto 9: Concatenar la lista a otra creada")
print("----------")
otras_ciudades = ['Londres', 'Copenhague', 'Barcelona', 'Viena', 'Madrid']
ciudades_concatenadas = ciudades + otras_ciudades
print(ciudades_concatenadas)
print("----------\n")

#10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print("Punto 10: Indice de cuba")
print("----------")
print(ciudades_concatenadas.index('Cuba'))
print("----------\n")

#11) ¿Qué pasa si se busca un elemento que no existe?
print("Punto 11: Indice de elemento que no existe")
print("----------")
# print(ciudades_concatenadas.index('Paris'))
print("Dara ValueError: 'Object' is not in list")
print("----------\n")

#12) Eliminar un elemento de la lista
print("Punto 12: Eliminar elemento de la lista")
print("----------")
ciudades_concatenadas.remove('Cuba')
print(ciudades_concatenadas)
print("----------\n")

#13) ¿Qué pasa si el elemento a eliminar no existe?
print("Punto 13: Y si el elemento no existe?")
print("----------")
# ciudades_concatenadas.remove('Paris')
print("Dara ValueError: list.remove(): 'object' not in list")
print("----------\n")

#14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
print("Punto 14: Ultimo elemento de la lista guardarlo en una variable")
print("----------")
ultElement = ciudades_concatenadas[-1]
print(ultElement)
print("----------\n")
#15) Mostrar la lista multiplicada por 4
print("Punto 15: La lista multiplicada * 4")
print("----------")
print(ciudades_concatenadas*4)
print("----------\n")

#16) Crear una tupla que contenga los números enteros del 1 al 20
print("Punto 16: Tupla con los numeros enteros del 1 al 20")
print("----------")
tuplaEntera = tuple([i for i in range(1,21)])
print(tuplaEntera)
print("----------\n")

#17) Imprimir desde el índice 10 al 15 de la tupla
print("Punto 17: Imprimir desde el indice 10 al 15 de la tupla")
print("----------")
print(tuplaEntera[10:15])
print("----------\n")

#18) Evaluar si los números 20 y 30 están dentro de la tupla
print("Punto 18: Evaluar si los numeros 20 y 30 estan dentro de la tupla")
print("----------")
if 20 in tuplaEntera:
    print("El 20 esta dentro de la tupla")
if 30 in tuplaEntera:
    print("El 30 esta en la tupla")
print("----------\n")

#19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
print("Punto 19: Agregar paris a la primera lista si no existe")
print("----------")
ciudad_nueva = 'Paris'
if ciudad_nueva not in ciudades:
    ciudades.append(ciudad_nueva)
    print("La ciudad {0} ha sido agregada a la lista de ciudades principal.".format(ciudad_nueva))
else:
    print(f"La ciudad {ciudad_nueva} ya se encuentra en la lista de ciudades principal.")
print("----------\n")

#20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print("Punto 20: Mostrar la cantidad que se repite un elemento dentro de la lista")
print("----------")
elemento = input("Que ciudad quiere ver cuantas veces esta en la lista?: ")
if elemento.title() not in ciudades_concatenadas:
    print("La ciudad no existe en la lista.")
else:
    contador = 0
    for ciudad in ciudades_concatenadas:
        if ciudad.lower() == elemento.lower():
            contador += 1
    print("La ciudad {0} se encuentra {1} veces en la lista.".format(elemento, contador))
print("----------\n")

#21) Convertir la tupla en una lista
print("Punto 21: Convertir la tupla en una lista")
print("----------")
tuplaToList = list(tuplaEntera)
print(tuplaToList)
print("----------\n")

#22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
print("Punto 22: Desempaquetar los primeros 3 elementos de la tupla en 3 variables")
print("----------")
# var1, var2, var3 = tuplaToList[0], tuplaToList[1], tuplaToList[2]
var1, var2, var3 = tuplaToList[:3]
print(var1, var2, var3)
print("----------\n")

#23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
print("Punto 23: Crear diccionario con la lista principal")
print("----------")
dictPrincipal = {"ciudad": ciudades, 
                "pais": ['Venezuela', 'Brazil', 'China','EEUU'],
                "continente": ['Asia', 'Europa','Oceania','Africa']}
print(dictPrincipal)
print("----------\n")

#24) Imprimir las claves del diccionario
print("Punto 24: Imprimir las claves del diccionario")
print("----------")
print(dictPrincipal.keys())
print("----------\n")

#25) Imprimir las ciudades a través de su clave
print("Punto 25: Imprimir las ciudades a traves de su clave")
print("----------")
print(dictPrincipal['ciudad'])
print("----------\n")