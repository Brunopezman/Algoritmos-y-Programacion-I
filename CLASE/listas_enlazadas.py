class _Nodo:
    def __init__(self, dato, prox) -> None:
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self) -> None:
        
        # referencia al primer Nodo de la LE
        # invariante:
        # lista vacia => prim == None
        # lista no vacia => prim == un Nodo
        self.primero = None

        # invariante:
        # self.cantidad  == cantidad de nodos de la LE
        self.cantidad = 0

    def append(self, dato):
        
        if self.primero is None:
            # lista vacia
            self.primero = _Nodo(dato, None)
        else:
            act = self.primero

            while act.proximo is not None:
                act = act.proximo

            # act.proximo == None
            # act es el ultimo _Nodo de la lista
            act.proximo = _Nodo(dato, None)
        self.cantidad += 1
    
    def __len__(self):
        return self.cantidad