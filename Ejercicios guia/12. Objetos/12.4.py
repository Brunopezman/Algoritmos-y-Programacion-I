'''
Escribir una clase Caja para representar cuánto dinero hay en una caja de un
negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
5, 10, 20, 50, 100, 200, 500 y 1000 pesos.

>>> c = Caja({500: 6, 300: 7, 2: 4})
ValueError: Denominación "300" no permitida
>>> c = Caja({500: 6, 100: 7, 2: 4})
>>> str(c)
'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
>>> c.agregar({250: 2})
ValueError: Denominación "250" no permitida
>>> c.agregar({50: 2, 2: 1})
>>> str(c)
'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
>>> c.quitar({50: 3, 100: 1})
ValueError: No hay suficientes billetes de denominación "50"
>>> c.quitar({50: 2, 100: 1})
200
>>> str(c)
'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'

'''

class Caja:

    def __init__(self, dinero:dict) -> None:

        valores_permitidos = [1,2,5,20,30,50,100,200,500,1000]

        for valor in dinero.keys():
            if valor not in valores_permitidos:
                raise ValueError(f'Denominación "{valor}" no permitida')
            
        self.dinero = dinero

    def __str__(self) -> str:
        total = 0

        for valor, cantidad in self.dinero.items():
            total += valor * cantidad

        return f'Caja {self.dinero} total: {total}'

    def agregar(self, otro):
        
        for valor, cantidad in otro.items():
            self.dinero[valor] = self.dinero.get(valor, 0) + cantidad
        
        return Caja(self.dinero)
    
    def quitar(self, dinero_a_quitar):

        restado = 0

        for valor, cantidad in dinero_a_quitar.items():
            self.dinero [valor] = self.dinero.get(valor) - cantidad
            if self.dinero[valor] < 0:
                raise ValueError(f'No hay suficientes billetes de denominación {valor}')
            if self.dinero[valor] == 0:
                del self.dinero[valor] #Elimina una valor del dinero si su cantidad es cero.
            restado += valor * cantidad

        return restado
