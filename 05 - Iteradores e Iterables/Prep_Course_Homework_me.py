#1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1
print("Punto 1: con while agregarle negativos a una lista vacia del -15 al -1")
print("----------")
lista2 = []
n = -15
while n != 0:
    lista2.append(n)
    n+=1
print(lista2)
print("----------\n")

#2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
print("Punto 2: Pregunta")
print("----------")
print("Si")
print("----------\n")

#3) Resolver el punto anterior sin utilizar un ciclo while
print("Punto 3: Resolver la pregunta sin usar ciclo while")
print("----------")
for i in lista2:
    if (i*(-1)) % 2 == 0:
        print(i)
print("----------\n")

#4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
print("Punto 4: imprimir los 3 primeros solo con iterable")
print("----------")
for i in lista2[:3]:
    print(i)
print("----------\n")


#5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
print("Punto 5: Utilizar enumerate para imprimir el indice al que corresponde cada elemento")
print("----------")
for i, v in enumerate(lista2):
    print(f"indice: {i}, valor: {v}")
print("----------\n")

#6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]
print("Punto 6: ")
print("----------")
lista = [1,2,5,7,8,10,13,14,15,17,20]
contador = 1
for i in range(1,20):
    if contador not in lista:
        lista.append(contador)
    contador += 1
lista.sort()
print(lista)
print("----------\n")

#7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
#n0 = 0<br>
#n1 = 1<br>
#ni = ni-1 + ni-2
#Crear una lista con los primeros treinta números de la sucesión.<br>
fibonacci = [0,1]
n = 2
while (n<30):
    fibonacci.append(fibonacci[n-1] + fibonacci[n-2])
    n += 1
print(fibonacci)
#8) Realizar la suma de todos elementos de la lista del punto anterior
suma = sum(fibonacci)
print(suma)

#9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
#Donde i es la cantidad total de elementos
#ni-1 / ni
#ni-2 / ni-1
#ni-3 / ni-2
#ni-4 / ni-3
#ni-5 / ni-4
for i in range(10,15):
    print(fibonacci[i]/fibonacci[i-1])

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
posicionesN = []
for indice, letra in enumerate(cadena):
    if letra == 'n':
        posicionesN.append(indice)
print(posicionesN)

# 11) Crear un diccionario e imprimir sus claves utilizando un iterador
dictPrincipal = {"ciudad": ['Tokyo', 'New York', 'Miami',],
                "pais": ['Venezuela', 'Brazil', 'China','EEUU'],
                "continente": ['Asia', 'Europa','Oceania','Africa']}
for clave in dictPrincipal:
    print(clave)
# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 
cadenaLista = cadena.split(" ")
for palabra in cadenaLista:
    print(palabra)

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip
lista1 = ["Hola", "como","estas"]
lista2 = ["muy", "bien","y tu?"]
lista3 = zip(lista1, lista2)
print(lista3)
print(list(lista3))

# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
listanueva = []
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
for n in lis:
    if n % 7 == 0:
        listanueva.append(n)
print(listanueva)

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lisnew = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
elementosDeLista = len(lisnew)
print(elementosDeLista)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
indice = 0
for e in lisnew:
    if type(e) != list:
        lisnew[indice] = [e]
    indice += 1
print(lisnew)