"""
Implementar el método duplicar(elemento) de ListaEnlazada, que recibe un
elemento y duplica todas las apariciones del mismo. Ejemplo:
"""
class _Nodo:

    def __init__(self, dato, prox = None) -> None:
        self.dato = dato
        self.prox = prox

class ListaEnlazada:

    def __init__(self) -> None:
        self.prim = None
        self.len = 0

    def __str__(self) -> str:
        if not self.prim:
            return 'Lista vacia'
        
        act = self.prim
        elementos = []

        while act:
            elementos.append(str(act.dato))
            act = act.prox

        return '[' + ', '.join(elementos) + ']'

    def append(self, dato):

        if not self.prim:
            self.prim = _Nodo(dato, None)
        else:
            act = self.prim

            while act.prox:
                act = act.prox
            act.prox = _Nodo(dato, None)

        self.len += 1

    def duplicar(self, elemento):

        if not self.prim:
            return 
        
        act = self.prim

        while act:
            if act.dato == elemento:
                nuevo_nodo = _Nodo(elemento)
                nuevo_nodo.prox = act.prox
                act.prox = nuevo_nodo
                act = nuevo_nodo.prox
            else:
                act = act.prox

    def nplicar(self, elemento, n):

        if not self.prim:
            return 
        
        act = self.prim

        while act:
            if act.dato == elemento:
                for i in range(n):
                    nuevo_nodo = _Nodo(elemento)
                    nuevo_nodo.prox = act.prox
                    act.prox = nuevo_nodo
                    act = nuevo_nodo  # Move act to the newly added node
            else:
                act = act.prox

            # Move to the next node in the original list
            if act:
                act = act.prox

l1 = ListaEnlazada()
l1.append(1)
l1.append(2)
l1.append(3)
l1.nplicar(2,3)
print(l1)