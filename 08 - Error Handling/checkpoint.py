# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    # if type(numero) == int:
    #     if numero <=0:
    #         return "Debe ser mayor a 0"
    #     if numero > 1:
    #         numero = numero * Factorial(numero-1)
    #         return numero
    # else:
    #     return 'Nulo' 
    #Para que mi yo del futuro descubra por que esta version no sirve y la de abajo si
    
    if type(numero) != int:
        return "El numero no es factible para sacar su factorial, debe ser entero y no negativo."
    else:
        if numero <= 0:
            return "el numero debe ser mayor a 0"
        if numero > 1:
            numero = numero * Factorial(numero-1)
        return numero
    
print(Factorial(4))
print(Factorial(-2))

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    contador = 0
    contadorFinal = valor
    while contadorFinal != 1:
        if valor % contadorFinal == 0:
            contador += 1
        contadorFinal -= 1
    if contador > 1:
        return False
    else:
        return True
print(EsPrimo(7))
print(EsPrimo(8))
    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal:
        def __init__(self, especie,color):
            self.especie = especie
            self.color = color
            self.edad = 0
        def cumplirAnios(self):
            self.edad += 1
            print(self.edad)
    
    a = Animal(especie, color)

    return a


AnimalSabrosote = ClaseAnimal('Rata', 'Roja oscura')
print(AnimalSabrosote.color)
AnimalSabrosote.cumplirAnios()
AnimalSabrosote.cumplirAnios()
AnimalSabrosote.cumplirAnios()
AnimalSabrosote.cumplirAnios()
AnimalSabrosote.cumplirAnios()
AnimalSabrosote.cumplirAnios()