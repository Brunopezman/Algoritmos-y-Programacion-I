"""
Escribir un método de la clase ListaEnlazada que invierta el orden de la lista
(es decir, el primer elemento queda como último y viceversa).

"""

class _Nodo:

    def __init__(self, dato) -> None:
        self.dato = dato
        self.prox = None

class ListaEnlazada:

    def __init__(self) -> None:
        self.prim = None
        self.len = 0

    def __str__(self) -> str:
        
        if not self.prim:
            return 'Lista vacía'

        elementos = []
        act = self.prim

        while act:
            elementos.append(str(act.dato))
            act = act.prox

        return '[' + ', '.join(elementos) + ']'

    def append(self, dato):
        
        if not self.prim:
            self.prim = _Nodo(dato)
        else:

            act = self.prim

            while act.prox:
                act = act.prox
            act.prox = _Nodo(dato)
            
        self.len += 1

    def __len__(self):
        return self.len
    
    def invertir(self):

        if not self.prim or not self.prim.prox:
            return
        
        ant = None
        act = self.prim
        
        while act:
            sig = act.prox
            act.prox = ant
            ant = act
            act = sig

        self.prim = ant

