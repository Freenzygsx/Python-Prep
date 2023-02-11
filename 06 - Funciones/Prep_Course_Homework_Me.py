
# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
def getPrimeOrNot(numero: int) -> bool:
    """Funcion que retorna si el numero ingresado es primo o no, con un booleano

    Args:
        numero (int): numero a verificar si es primo o no

    Returns:
        bool: True o False
    """
    contadorPrincipal = numero
    contadorSecundario = 0

    while contadorPrincipal != 1:
        if numero % contadorPrincipal == 0:
            contadorSecundario += 1
        contadorPrincipal -= 1
    if contadorSecundario > 1:
        return False
    else:
        return True
print(getPrimeOrNot(4))

# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
def getPrimeNumbersList(lista: list) -> list:
    """Funcion que recibe una lista y devuelve otra con solo los numeros primos, utilizando la funcion anterior

    Args:
        lista (list): Lista con numeros

    Returns:
        list: lista con numeros primos
    """
    listaNueva = []
    for elemento in lista:
        if getPrimeOrNot(elemento):
            listaNueva.append(elemento)
        else:
            continue
    return listaNueva

print(getPrimeNumbersList([29,23,4,5,18,13]))

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
def getRepetitionNumber(listNumbers: list) -> dict:
    """Funcion que recibe una lista de numeros y retorna los mas repetidos y cuantas veces se repitio

    Args:
        listNumbers (list): Lista de numeros

    Returns:
        string: string mencionando cual fue el numero mas repetido y con cuantas repeticiones
    """
    dict = {}
    tempList = []
    for elemento in listNumbers:
        if elemento in tempList:
            dict[elemento] += 1
        else:
            dict[elemento] = 1
            tempList.append(elemento)
    temp_ma_key = 0
    temp_ma_value = 0
    for clave, valor in dict.items():
        if valor > temp_ma_value:
            temp_ma_value = valor
            temp_ma_key = clave

    return f"El numero que mas se repitio fue {temp_ma_key} con {temp_ma_value} repeticiones."
print(getRepetitionNumber([1,1,1,2,1,5,4,9,78,54,62,3,15,4]))

# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.
def getRepetitionNumberImproved(listNumbers: list, menoromayor):
    """Funcion que recibe una lista de numeros y retorna los mas repetidos y cuantas veces se repitio

    Args:
        listNumbers (list): Lista de numeros

    Returns:
         string: string mencionando cual fue el numero mas repetido o menor repetido dependiendo de la condicion del usuario y con cuantas repeticiones
    """
    dict = {}
    tempList = []
    for elemento in listNumbers:
        if elemento in tempList:
            dict[elemento] += 1
        else:
            dict[elemento] = 1
            tempList.append(elemento)
    if menoromayor.lower() == 'mayor':
        temp_ma_key = 0
        temp_ma_value = 0
        for clave, valor in dict.items():
            if valor > temp_ma_value:
                temp_ma_value = valor
                temp_ma_key = clave

        return f"El numero que mas se repitio fue {temp_ma_key} con {temp_ma_value} repeticiones."
    elif menoromayor.lower() == 'menor':
        temp_me_key = 0
        temp_me_value = 1000000000000000000000
        for clave, valor in dict.items():
            if valor < temp_me_value:
                temp_me_value = valor
                temp_me_key = clave
        return f"El numero que menos se repitio fue {temp_me_key} con {temp_me_value} repeticiones."
    else:
        return "Algo ocurrio mal, por favor intente de nuevo ingresando 'menor' o 'mayor' para retornarle el numero que mas/menos se repita."

print(getRepetitionNumberImproved([1,1,1,2,1,5,4,9,78,54,62,3,15,4],'menor'))

# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
def transformTemperature(valor, primeraMedida, segundaMedida):
    """Funcion que recibe un valor en grados de temperatura, una primera medida que sera la principal y una segunda medida que sera a la que transformaremos la primera medida.

    Args:
        valor (numeric): Valor numerico que representa la temperatura con la que trabajaremos
        primeraMedida (string): Nombre de la primera medida
        segundaMedida (string): Nombre de la segunda medida
    Returns:
        valor (numeric): El valor de la conversion de la primera medida a la segunda, o sino un mensaje de error.
    """
    #Transformando celsius a farenheit o kelvin
    if primeraMedida.lower() == 'celsius':
        if segundaMedida.lower() == 'farenheit':
            return (valor * 9/5)+32
        elif segundaMedida.lower() == 'kelvin':
            return (valor + 273.15)
        else:
            return "Algo ha ocurrido mal, por favor asegurate de que la segunda medida a convertir esta bien escrita o no sea la misma que la primera"
    
    #Transformando farenheit a celsius o kelvin
    elif primeraMedida.lower() == 'farenheit':
        if segundaMedida.lower() == 'celsius':
            return (valor - 32)*5/9
        elif segundaMedida.lower() == 'kelvin':
            return (valor - 32) * 5/9 + 273.15
        else:
            return "Algo ha ocurrido mal, por favor asegurate de que la segunda medida a convertir esta bien escrita o no sea la misma que la primera"
    
    #Transformando kelvin a celsius o farenheit
    elif primeraMedida.lower() == 'kelvin':
        if segundaMedida.lower() == 'celsius':
            return (valor - 273.15)
        elif segundaMedida.lower() == 'farenheit':
            return (valor - 273.15) * 9/5 + 32
        else:
            return "Algo ha ocurrido mal, por favor asegurate de que la segunda medida a convertir esta bien escrita o no sea la misma que la primera"
    else:
        return "Algo ha ocurrido mal, por favor asegurate de que la primera medida a convertir esta bien escrita"

print(transformTemperature(11,'farenheit','celsius'))



# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:
medidas = ['celsius', 'farenheit', 'kelvin']
for i in range(0, 3):
    for j in range(0, 3):
        print(f"10 grados {medidas[i]} a {medidas[j]}: {transformTemperature(10,medidas[i],medidas[j])}")


# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo
def getFactorial(numero: int) -> int:
    """Funcion que recibe un numero y devuelve su factorial

    Args:
        numero (int): Numero entero

    Returns:
        int: Factorial del numero
    """
    if type(numero) != int:
        return "El numero no es factible para sacar su factorial, debe ser entero y no negativo."
    else:
        if numero <= 0:
            return "el numero debe ser mayor a 0"
        if numero > 1:
            numero = numero * getFactorial(numero-1)
        return numero
print(getFactorial(3))
print(getFactorial(-2))
