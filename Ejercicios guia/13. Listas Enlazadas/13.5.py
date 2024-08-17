"""
Implementar el método filter(f) de ListaEnlazada, que recibe una función y
devuelve una nueva lista enlazada con los elementos para los cuales la aplicación de f devuelve
True. La nueva lista debe ser construida recorriendo los nodos una sola vez (es decir, no se
puede llamar a append). Ejemplo:
L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
L.filter(es_primo) -> L2 = 5 -> 2

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
    
    def filter(self,f):

        nueva = ListaEnlazada()
        if not self.prim:
            return nueva
        
        act = self.prim
        n_act = nueva.prim

        while act:

            if not f(act.dato):
                act = act.prox
                continue    
            if f(act.dato) and not nueva.prim:
                nuevo = _Nodo(act.dato)
                nueva.prim = nuevo
                n_act = nueva.prim
                nueva.cant += 1
                act = act.prox
                continue
            if f(act.dato):
                nuevo = _Nodo(act.dato)
                n_act.prox = nuevo
                n_act = n_act.prox
                nueva.cant += 1
                act = act.prox
                continue

        return nueva
    
def f(numero):
    return numero % 2 == 0

lista = ListaEnlazada()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.filter(f)
print(lista)