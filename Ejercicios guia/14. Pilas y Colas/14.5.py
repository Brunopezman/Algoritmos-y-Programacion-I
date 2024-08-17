"""
Crear una clase PilaConMaximo que soporte las operaciones de Pila
(apilar(elemento) y desapilar()), y además incluya el método obtener_maximo() en tiempo constante. Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar los máximos.
"""

class _Nodo:

    def __init__(self, dato, prox) -> None:
        self.dato = dato
        self.prox = prox

class PilaConMaximo:

    def __init__(self) -> None:
        self.items = []

    def apilar(self,x):
        self.items.append(x)

    def desapilar(self):
        return self.items.pop()
    
    def obtener_maximo(self):
        pass

class Pila:

    def __init__(self) -> None:
        self.items = []

    def apilar(self,x):
        self.items.append(x)

    def desapilar(self):
        return self.items.pop()
    
    def esta_vacia(self):
        return len(self.items) == 0
    