"""
Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada y
agregue a la lista actual los elementos que se encuentran en la lista recibida.

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
        
        if self.prim is None:
            self.prim = _Nodo(dato)
        else:

            act = self.prim

            while act.prox:
                act = act.prox
            act.prox = _Nodo(dato)
            
        self.len += 1

    def extend(self, otra):

        if not isinstance(otra, ListaEnlazada):
            raise ValueError("Se debe proporcionar una instancia de ListaEnlazada")

        act = self.prim
        otra_act = otra.prim

        while act and act.prox:
            act = act.prox
        
        while otra_act:

            nodo = _Nodo(otra_act.dato)

            if not act:
                self.prim = nodo
                act = nodo
            else:
                act.prox = nodo

            act = act.prox
            otra_act = otra_act.prox

    def completar_huecos(self):

        if not self.prim or not self.prim.prox:
            return
        act = self.prim

        while act.prox:
            gap = act.prox.dato - act.dato
            print(gap)
            if gap > 1:
                nuevo_dato = act.dato + 1
                nodo = _Nodo(nuevo_dato)
                nodo.prox = act.prox
                act.prox = nodo
            elif gap < -1:
                nuevo_dato = act.dato - 1
                nodo = _Nodo(nuevo_dato)
                nodo.prox = act.prox
                act.prox = nodo
            act = act.prox

# Ejemplo de uso:
mi_lista = ListaEnlazada()
mi_lista.append(1)
mi_lista.append(4)
mi_lista.append(3)
mi_lista.append(1)
mi_lista.append(3)
mi_lista.completar_huecos()
print(mi_lista)

        