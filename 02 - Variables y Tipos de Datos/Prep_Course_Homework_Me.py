import math

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
print("Punto 1: Definido numero entero e impreso")
numero = 10
print(numero)

#2) Imprimir el tipo de dato de la constante 8.5
print("Punto 2: Imprimir el tipo de dato de la constante 8.5")
print(type(8.5))

#3) Imprimir el tipo de dato de la variable creada en el punto 1
print("Punto 3: Imprimir el tipo de dato de la variable del punto 1")
print(type(numero))

#4) Crear una variable que contenga tu nombre
print("Punto 4: Definido nombre")
nombre = "Ezziel"

#5) Crear una variable que contenga un número complejo
print("Punto 5: Definido numero complejo")
numeroComplejo = 10 + 7j

#6) Mostrar el tipo de dato de la variable crada en el punto 5
print("Punto 6: Imprimiendo numero complejo")
print(type(numeroComplejo))

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
print("Punto 7: Numero pi redondeado 4 decimales")
numeroPi = round(math.pi, 4)

#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
print("Punto 8: Creando variables con valor True y 'True'")
trueVerdadero = True
trueFalso = 'True'
#No son lo mismo, uno es tipo de dato booleano True, otro es una cadena de texto con la palabra True

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print("Punto 9: Imprimiendo el tipo de dato de las variables del punto anterior")
print(f"La variable 'True' es: {type(trueFalso)} y la variable True es: {type(trueVerdadero)}")

#10) Asignar a una variable, la suma de un número entero y otro decimal
print("Punto 10: Asignar a una variable la suma de un entero y un decimal")
numeroDecimal = 10+15.2

#11) Realizar una operación de suma de números complejos
print("Punto 11: operacion compleja con numeros complejos")
numeroComplejo2 = 45 - 12j
operacionCompleja = numeroComplejo + numeroComplejo2
print(operacionCompleja)

#12) Realizar una operación de suma de un número real y otro complejo
print("Punto 12: operacion con numero real y complejo")
print(1+2.6)

#13) Realizar una operación de multiplicación
print("Punto 13: Realizar multiplicacion")
a = 2
b = 3
print(a*b)

#14) Mostrar el resultado de elevar 2 a la octava potencia
print("Punto 14: 2 elevado a la 8 potencia")
print(2**8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
print("Punto 15: Obtener el cociente de la division de 27 / 4 en una variable y luego mostrarlo")
cociente = 27/4
print(cociente)

#16) De la división anterior solamente mostrar la parte entera
print("Punto 16: Mostrar la parte entera de la division anterior")
parteEntera = int(cociente)
print(27//4) #con // se mostrara solo la parte entera
print(parteEntera)

#17) De la división de 27 entre 4 mostrar solamente el resto
print("Punto 17: Mostrar solamente el resto de la division anterior")
print(27%4)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print("Punto 18:")
operandos = 4*6+3
print(operandos) 

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print("Punto 19:")
print('hola'+' como estas')

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("Punto 20: Evaluar si '2' es igual a 2 y por que ocurre lo que ocurre")
numdos = 2
numdosstr = '2'
print(numdosstr==numdos)
print("Es falso porque '2' es un caracter de tipo cadena de texto y 2 es un caracter de tipo numerico (entero), por lo que no son iguales.")

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print("Punto 21: ")
print(int(numdosstr)==numdos)

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
print("Punto 22: Por que arroja error? a = float('3,8')")
print("Porque para convertir un numero en flotante debe ser un tipo de dato numerico y no de cadena de texto, el numero al estar entre comillas simples se convierte en tipo string y no numerico")

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
print("Punto 23: Crea una variable con el valor 3 y utiliza el operador -= para modificar su contenido")
tres = 3
tres -= 2
print("ahora es uno", tres)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print("Punto 24: Realiza la operacion 1 << 2 y explica por que da ese resultado y di que es el sistema de numeracion binario.")
a = 1<<2
b = 1>>2

print(0b000100) #esta es a
print(a)
print("-----------------")
print(0b0001) #este es el numero principal, 25
print("-----------------")
print(0b00) #este es b
print(b)
print("-----------------")
print("El sistema binario es aquel que solo utiliza 0 y 1, utilizar los operadores << y >> nos permite transformar un numero utilizando el sistema binario para luego retornarlo en la conversion que quisimos. Para entender el primer ejemplo, debemos saber cual es la representacion de 1 en binario, la cual es 0001, para luego proceder a la explicacion: lo que hace el << 2 es que le suma dos ceros al 1, en el segundo ejemplo le resta dos numeros de la derecha a la izquierda al 1 en sistema binario, por lo que: 0001 << 2 = 000100, y 0001 >> 2 = 00")


#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
print("Punto 25: Realizar operacion 2 + '2'")
# print(numdos+numdosstr)
print("No esta permitido porque un valor es entero y otro es tipo cadena de texto, por lo que no se pueden sumar o operar con tipos de dato diferentes, si los dos tipos de dato fuesen iguales no daria el error. Si fuesen cadena de texto los dos, el resultado simplemente se concatenaria '2'+'2'=22, pero al ser numeros, se operaria con normalidad 2+2 = 4")
print(str(numdos)+numdosstr)
print(int(numdosstr)+numdos)
#26) Realizar una operación válida entre valores de tipo entero y string
print("Punto 26: Realizar una operacion valida entre valores de tipo entero y de tipo string")
texto = "Sumaremos los siguientes numeros: "
print(texto+str(numdos)+' y '+numdosstr+' y obtendremos: '+ str(int(numdosstr)+numdos))
