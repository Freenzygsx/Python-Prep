# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor
class vehiculo():
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    
    def acelerar(self, vel):
        self.velocidad += vel
    def frenar(self, vel):
        self.velocidad -= vel
    def doblar(self, grados):
        self.direccion += grados
    def estado(self):
        print(f"Velocidad: {self.velocidad}, Direccion: {self.direccion}")
    def detalle(self):
        print(f"Color: {self.color}, Tipo de vehiculo: {self.tipo}, Cilindrada: {self.cilindrada}")

vehiculo1 = vehiculo('azul', 'moto', 500)
print(vehiculo1.color)
print(vehiculo1.tipo)
print(vehiculo1.cilindrada)
vehiculo2 = vehiculo('verde','camion',844)
vehiculo3 = vehiculo('morado','auto', 144)

vehiculo1.acelerar(50)
vehiculo1.doblar(45)
vehiculo1.estado()
vehiculo1.detalle()
# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

class funciones():
    def __init__(self) -> None:
        pass

    def verificarPrimo(self, numero):
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
    
    def valorModal(self, listNumbers, menoromayor):
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
    def conversionGrados(self, valor, primeraMedida, segundaMedida):
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
    
    def factorial(self, numero):
        if type(numero) != int:
            return "El numero no es factible para sacar su factorial, debe ser entero y no negativo."
        else:
            if numero <= 0:
                return "el numero debe ser mayor a 0"
            if numero > 1:
                numero = numero * f.factorial(numero-1)
            return numero

f = funciones()

print(f.verificarPrimo(6))


# 6) Probar las funciones incorporadas en la clase del punto 5

# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas
lista = [1,8,2,5,4,8,10,7,7,7,7]
print(f.valorModal(lista, 'menor'))
print(f.valorModal(lista, 'mayor'))

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones