"""
Escribir una función llamada tail que recibe un archivo y un número N e imprime
las últimas N líneas del archivo. Durante el transcurso de la función no puede haber más de N
líneas en memoria.
"""
class _nodo:

    def __init__(self, dato, prox) -> None:
        self.dato = dato
        self.prox = prox

class Cola:

    def __init__(self) -> None:
        self.frente = None
        self.ultimo = None

    def encolar(self, dato):
        nuevo = _nodo(dato, None)
        if not self.frente:
            self.frente = nuevo
            self.ultimo = nuevo
        else:    
            self.ultimo.prox = nuevo
            self.ultimo = nuevo

    def desencolar(self):

        if not self.frente:
            raise ValueError('Cola vacia')
        dato = self.frente.dato
        self.frente = self.frente.prox
        if not self.frente:
            self.ultimo = None

        return dato
    
    def ver_frente(self):
        if not self.frente:
            raise ValueError('Cola vacia')
        return self.frente is None 

    def esta_vacia(self):
        return self.primero is None
    
def tail(ruta, n):

    with open(ruta) as f:
        
        contador = 0
        cola = Cola()
        
        for linea in f:
            linea = linea.rstrip()
            cola.encolar(linea)
            if contador == n:
                cola.desencolar()
            else:
                contador +=1

        while not cola.esta_vacia():
            linea = cola.desencolar()
            print(linea) 